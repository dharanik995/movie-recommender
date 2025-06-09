import pandas as pd

# Path to the 'u.item' file inside your dataset folder
item_file = './ml-100k/u.item'

# MovieLens 'u.item' columns (based on dataset documentation)
columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
           'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
           'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
           'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

# Load the dataset with proper encoding
movies_df = pd.read_csv(item_file, sep='|', names=columns, encoding='latin-1')

# Check the first 5 rows
print(movies_df.head())


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Combine all genre columns into a single string for each movie
genre_columns = ['unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
                 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
                 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

def combine_genres(row):
    genres = []
    for genre in genre_columns:
        if row[genre] == 1:
            genres.append(genre)
    return ' '.join(genres)

movies_df['combined_genres'] = movies_df.apply(combine_genres, axis=1)

# Vectorize the combined genre strings
count_vectorizer = CountVectorizer()
genre_matrix = count_vectorizer.fit_transform(movies_df['combined_genres'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

print("Cosine similarity matrix created!")
def get_recommendations(title, movies_df, cosine_sim):
    # Create a Series mapping movie titles to their indices
    indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()

    # Get the index of the movie that matches the title
    idx = indices.get(title)

    if idx is None:
        return f"Sorry, '{title}' not found in the database."

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Skip the first movie (itself), get the scores of the 5 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movie titles
    return movies_df['title'].iloc[movie_indices].tolist()

# Example usage
movie_input = "Four Rooms (1995)"
recommended_movies = get_recommendations(movie_input, movies_df, cosine_sim)

print(f"Top 5 movies similar to '{movie_input}':")
for movie in recommended_movies:
    print(movie)
