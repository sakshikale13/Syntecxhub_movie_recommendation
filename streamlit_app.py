#  Movie Recommender UI


import streamlit as st
import pickle
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🍿",
    layout="wide"
)

# ---------------- Custom Netflix CSS ----------------
st.markdown("""
<style>
body {
    background-color: #141414;
}

.title {
    color: #E50914;
    font-size: 50px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    color: white;
    text-align: center;
    font-size: 18px;
}

.movie-card img {
    border-radius: 10px;
    transition: 0.3s;
}

.movie-card img:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)


# ---------------- Load Model ----------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


# ---------------- Fetch Poster ----------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b3cecea46a997459e7b74a21eb365297&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"

    except:
        return "https://via.placeholder.com/300x450?text=Error"


# ---------------- Recommend Function ----------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- Netflix Header ----------------
st.markdown("<div class='title'>NETFLIX Movie Recommender 🍿</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Discover movies you'll love</div>", unsafe_allow_html=True)

st.write("")

# ---------------- Movie Selector ----------------
selected_movie = st.selectbox(
    "Choose Your Favorite Movie",
    movies['title'].values
)

st.write("")

# ---------------- Recommend Button ----------------
if st.button("🎬 Show Recommendations"):

    names, posters = recommend(selected_movie)

    st.markdown("## ⭐ Recommended For You")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.caption(names[0])

    with col2:
        st.image(posters[1])
        st.caption(names[1])

    with col3:
        st.image(posters[2])
        st.caption(names[2])

    with col4:
        st.image(posters[3])
        st.caption(names[3])

    with col5:
        st.image(posters[4])
        st.caption(names[4])


# ---------------- Footer ----------------
st.markdown("---")
st.markdown("<center style='color:gray'>Built with ❤️ | Netflix‑Style UI</center>", unsafe_allow_html=True)

