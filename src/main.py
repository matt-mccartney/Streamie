from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", signed_in=True), 200


@app.route("/watch/<id>")
def watch(id):
    return {"data": id}, 200


@app.route("/browse/genre/<id>")
def browse_genre(id):
    return {"data": id}, 200


if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)