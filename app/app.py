from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from sinling import SinhalaTokenizer

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    response = None
    query = request.form.get("query")
    print(query)
    if query is not None:
        response = es.search(
            index="sinhala_songs",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["artist", "lyrics", "title", "musicArtist", "lyricsArtist"]
                    }
                }
            }
        )
        print(response['hits']['hits'])
        return render_template('index.html', query=query, response= response)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
