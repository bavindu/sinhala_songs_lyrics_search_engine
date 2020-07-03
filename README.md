# Sinhala Songs Search Engine
This repository contains the source code for a sinhala songs search engine built using ElasticSearch and Python.

## Get Started
1. Download and run <a href="https://www.elastic.co/downloads/elasticsearch">Elasticsearch</a><br>
2. Install [ICU analysis plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html)
3. Install [Kbana](https://www.elastic.co/downloads/kibana). (This is optional. Using this tool you can execute different type of queries)
4. Download and setup [Sinling](https://github.com/nlpc-uom/Sinling). Follow the instruction given in that repository

## Setup
1. Start the  Search engine instance using fallowing instruction
    - Run elastic_search.py file in the elasticSearch folder
2. Start the flask server
    - Run app.py file in the app folder
    - Visit the http://localhost:8000
3. Enter the search query in the search box in the website


## Quickstart:
To start the search engine follow the instructions given below.
* Start an ElasticSearch Instance on the port 9200
* Run the command `python3 backend.py`
* Visit http://localhost:5000 
* Enter the search query in the search box in the website

## Usage Example

1. search for song lyrics
<img src="https://github.com/bavindu/sinhala_songs_lyrics_search_engine/blob/master/images/search%20by%20song.jpg">

2. Search by artist name
<img src="https://github.com/bavindu/sinhala_songs_lyrics_search_engine/blob/master/images/search%20by%20artis.jpg">

3. Advance search
<img src="https://github.com/bavindu/sinhala_songs_lyrics_search_engine/blob/master/images/search%20by%20advance.jpg">
