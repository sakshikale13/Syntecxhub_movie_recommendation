# Syntecxhub_movie_recommendation
🍿 Netflix-Style Movie Recommendation System

A Machine Learning based **Movie Recommendation System** with a **Netflix-style UI** built using **Streamlit**.
This project recommends similar movies based on content using **Cosine Similarity**.

---

# 🚀 Project Demo

🎬 Select a movie → Click Recommend → Get Top 5 Similar Movies

---

# 📌 Features

✅ Content-Based Movie Recommendation
✅ Netflix-Style Dark UI
✅ Movie Poster Integration (TMDB API)
✅ Top 5 Similar Movie Suggestions
✅ Interactive Streamlit Web App
✅ Clean & Responsive Layout

---

# 🧠 Machine Learning Approach

This project uses **Content-Based Filtering**:

* Movie Overview
* Genres
* Keywords
* Cast
* Crew

These features are combined into a **tags column** and processed using:

* Count Vectorizer
* Cosine Similarity

---

# 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* TMDB API
* Pickle

---

# 📂 Project Structure

```
Movie-Recommender/
│
├── streamlit_app.py
├── movies.pkl
├── similarity.pkl
├── notebook.ipynb
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/movie-recommender.git
```

Navigate to project folder

```
cd movie-recommender
```

Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Run Application

```
streamlit run streamlit_app.py
```

---

# 🎬 How It Works

1. User selects a movie
2. Model finds similar movies
3. Fetch movie posters using TMDB API
4. Display results in Netflix-style UI

---

# 📌 Week 4 Internship Project

This project was completed as part of **Week 4 Task** during my **Machine Learning Internship at SyntecxHub**.

---



