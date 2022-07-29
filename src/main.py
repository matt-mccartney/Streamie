from datetime import datetime
import random
from flask import Flask, jsonify, render_template, url_for
import requests
from flask_login import LoginManager


login_manager = LoginManager()
app = Flask(__name__)


data = {}

for i in range(1, 10):
    discover_movie = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key=54b11847ec5a5d11786bc93459712931&with_release_type=4&with_watch_providers=8,9,390,384,531,15&include_video=true&page={i}&release_date.gte={datetime.now().year - 10}")
    discover_tv = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key=54b11847ec5a5d11786bc93459712931&with_release_type=4&with_watch_providers=8,9,390,384,531,15&include_video=true&page={i}&release_date.gte={datetime.now().year - 10}")

    if i == 1:
        data.update({"popular tv": discover_tv.json()['results'], "popular movies": discover_movie.json()['results']})
    else:
        [data['popular movies'].append(i) for i in discover_movie.json()['results']]
        [data['popular tv'].append(i) for i in discover_tv.json()['results']]

random_select = lambda: random.randint(0, len(data["popular movies"]))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", signed_in=True, data=data, random_select=random_select()), 200


@app.route("/watch/<id>")
def watch(id):
    resp = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=54b11847ec5a5d11786bc93459712931&append_to_response=videos,images,recommendations").json()
    return {"id": id, "data": resp}, 200


@app.route("/browse/genre/<id>")
def browse_genre(id):
    return {"data": id}, 200


@app.route("/data")
def data_view():
    return {"data": data}, 200


if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)