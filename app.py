from flask import Flask, jsonify
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def search_movie(title):
    name = search_by_name(title)
    if name != []:
        return f"<pre><h2>Название фильма {name['title']}</h2></pre>" \
               f"<pre>Страна производства {name['country']}</pre>" \
               f"<pre>Год выпуска {name['release_year']}</pre>" \
               f"<pre>Жанры: {name['genre']}</pre>" \
               f"<pre>Краткое описание {name['description']}</pre>"
    else:
        return "<h1>Такого фильма нет в базе данных</h1>"


@app.route("/movie/<year1>/to/<year2>")
def page_search_movies_by_year(year1, year2):
    return jsonify(search_movies_by_year(int(year1), int(year2)))


@app.route("/rating/<rating>")
def page_search_by_rating(rating):
    return jsonify(search_by_rating(rating))


@app.route("/genre/<genre>")
def page_search_by_genre(genre):
    return jsonify(search_by_genre(genre))


if __name__ == '__main__':
    app.run()
