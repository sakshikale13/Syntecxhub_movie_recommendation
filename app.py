from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


@app.route('/recommend', methods=['GET'])
def recommend_api():
    movie = request.args.get('movie')
    return jsonify(recommend(movie))


if __name__ == '__main__':
    app.run(debug=True)