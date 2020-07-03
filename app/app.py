from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from query_proccessor import query_process

app = Flask(__name__)
es = Elasticsearch()


@app.route('/', methods=["GET", "POST"])
def index():
    response = None
    query = request.form.get("query")
    if query is not None:
        query_body = query_process(query)
        response = es.search(
            index="sinhala_songs",
            body= query_body
        )
        print("Buckets")
        print(response["aggregations"]["rate_range"]["buckets"])
        print("\n")
        print("Search Results Count")
        print(response['hits']['total']['value'])
        print("\n")
        print(response['hits']['hits'])

        return render_template('index.html', query=query, response= response)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
