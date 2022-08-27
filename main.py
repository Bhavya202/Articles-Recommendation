from flask import Flask, request, jsonify
import csv

all_articles = []

with open("articles.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        "Articles": all_articles[0],
        "Status": "Success!"
    }), 200

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "Status": "Successfully Pushed article To Liked articles!!"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "Status": "Successfully Pushed article To Unliked articles!!"
    }), 202

if __name__ == "__main__":
    app.run()