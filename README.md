Movie Recommender System
Welcome to the Movie Recommender System — a user-friendly web application designed to help you discover movies similar to your favorites by analyzing their genres.

Overview
Simply enter the name of a movie you like, and this app will suggest 5 other movies with similar genre profiles. It’s a quick and effective way to find new films you might enjoy!

Features
Intuitive search: Type in any movie title and get instant recommendations.

Genre-based matching: Recommendations are based on movie genres to ensure relevance.

Powered by MovieLens 100k dataset: Uses a well-known and reliable dataset with detailed movie information.

Simple and clean interface: Built using Streamlit for easy use and quick responses.

Data Source
The app leverages the MovieLens 100k dataset, a widely used dataset in movie recommendation research that includes thousands of movies and their genre attributes.

Technology Stack
Python: Core programming language.

Streamlit: For creating the interactive web interface.

Pandas: Handling and processing the movie data.

scikit-learn: Computing similarity scores using cosine similarity on genre vectors.

How to Use
Try the live demo here:
👉 https://movie-recommender-td.streamlit.app/

Enter any movie title exactly as it appears in the dataset (including case and punctuation). For example:
Toy Story (1995)
Note: The search is case-sensitive, so be sure to match the title’s capitalization.

The app will then return 5 movies with similar genres instantly.


Running Locally
To run the app on your local machine, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Launch the Streamlit app:

bash
Copy
Edit
streamlit run app.py
About the Author
Created by Dharani Kosuru. Contributions, suggestions, and issue reports are welcome!