from flask import Flask, jsonify, render_template, url_for
import requests

app = Flask(__name__)

data = {}

for i in range(1, 10):
    discover_movie = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key=54b11847ec5a5d11786bc93459712931&with_release_type=4&with_watch_providers=8,9,390,384,531,15&include_video=true&include_adult=true&page={i}")
    discover_tv = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key=54b11847ec5a5d11786bc93459712931&with_release_type=4&with_watch_providers=8,9,390,384,531,15&include_adult=true&include_video=true&page={i}")

    if i == 1:
        data.update({"popular tv": discover_tv.json()['results'], "popular movies": discover_movie.json()['results']})
    else:
        [data['popular movies'].append(i) for i in discover_movie.json()['results']]
        [data['popular tv'].append(i) for i in discover_tv.json()['results']]
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", signed_in=True, data=data), 200


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