import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from streamlit_lottie import st_lottie

# --------------------------- LOTTIE HELPER ---------------------------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --------------------------- PAGE CONFIG & STYLE ---------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #ffe6f0, #fefefe);
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput>div>div>input {
            border: 2px solid #FF4B4B;
            border-radius: 10px;
            padding: 10px;
        }
        h1 {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------- HEADER ---------------------------
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎬 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a movie name below and we'll suggest 5 similar ones!</p>", unsafe_allow_html=True)

# --------------------------- INPUT BOX ---------------------------
st.markdown("""
    <div style="background-color:#ffffff; padding: 30px; border-radius: 15px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.1); width: 80%; margin:auto;">
        <h3 style='text-align: center; color: #333;'>🔍 Search a Movie</h3>
""", unsafe_allow_html=True)

movie_input = st.text_input("", placeholder="e.g., Toy Story (1995)", label_visibility="collapsed")

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------- DATA LOAD ---------------------------
item_file = './ml-100k/u.item'
columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
           'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
           'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
           'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies_df = pd.read_csv(item_file, sep='|', names=columns, encoding='latin-1')

genre_columns = ['unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
                 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
                 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies_df['genres_combined'] = movies_df[genre_columns].apply(
    lambda row: ' '.join([genre for genre, val in zip(genre_columns, row) if val == 1]),
    axis=1
)

cv = CountVectorizer()
genre_matrix = cv.fit_transform(movies_df['genres_combined'])

movies_df['title_lower'] = movies_df['title'].str.lower()

similarity = cosine_similarity(genre_matrix)

# --------------------------- RECOMMENDATION FUNCTION ---------------------------
def recommend(movie_title):
    movie_title = movie_title.strip().lower()
    print("Searching for movie:", movie_title)
    print("Sample movie titles available:", movies_df['title_lower'].head(10).tolist())

    if movie_title not in movies_df['title_lower'].values:
        print("Movie not found in dataset.")
        return ["Movie not found."]
    idx = movies_df[movies_df['title_lower'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended_titles = [movies_df.iloc[i[0]]['title'] for i in sorted_scores]
    print("Recommendations:", recommended_titles)
    return recommended_titles

# --------------------------- SHOW RECOMMENDATIONS ---------------------------
if movie_input:
    with st.spinner("🎞️ Finding best matches..."):
        recommendations = recommend(movie_input)
        st.markdown("<br>", unsafe_allow_html=True)
        if recommendations == ["Movie not found."]:
            st.error("🚫 Movie not found. Please check the title and try again.")
        else:
            st.markdown("### 🍿 Recommended Movies:")
            for i, movie in enumerate(recommendations, 1):
                st.markdown(f"""
                    <div style="padding: 15px; margin: 10px 0; background-color: #fff3f6;
                                border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                        <p style="font-size: 18px;"><strong>🎥 {i}. {movie}</strong></p>
                    </div>
                """, unsafe_allow_html=True)

# --------------------------- FOOTER ---------------------------
st.markdown("""
    <hr style="border-top: 1px solid #ccc;">
    <p style='text-align: center; font-size: 13px; color: gray;'>
        Built by Dharani 💡 | Powered by AI + Streamlit | Movie Data: MovieLens
    </p>
""", unsafe_allow_html=True)

