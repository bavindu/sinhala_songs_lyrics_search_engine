from elasticsearch import Elasticsearch, helpers
import json

with open('proccessed_lyrics.json',encoding='utf-8') as file:
    song_list = json.load(file)
with open('mapping.json',encoding='utf-8') as mapping_file:
    mapping = json.load(mapping_file)
es = Elasticsearch(HOST="http://localhost", PORT=9200)
if es.indices.exists(index="sinhala_songs"):
    es.indices.delete(index="sinhala_songs")
response = es.indices.create(index="sinhala_songs", body=mapping)
helpers.bulk(es, song_list, index='sinhala_songs')
# print(response)


