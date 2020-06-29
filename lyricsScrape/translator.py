import json
from googletrans import Translator
from googletrans import  LANGUAGES

print("Hello")
data = None
trans = Translator()
with open("lyrics.json", "r") as read_file:
    data = json.load(read_file)

for item in data:
    artistEn = item['artist']
    lyricsArtistEn = item['lyricsArtist']
    musicArtistEn = item['musicArtist']
    if artistEn is not None:
        artistSin = trans.translate(artistEn, src='en', dest='si')
        item['artist'] = artistSin.text
    if lyricsArtistEn is not None:
        lyricsArtistSin = trans.translate(lyricsArtistEn, src='en', dest='si')
        item['lyricsArtist'] = lyricsArtistSin.text
    if musicArtistEn is not None:
        musicArtistSin = trans.translate(musicArtistEn, src='en', dest='si')
        item['musicArtist'] = musicArtistSin.text
    print(item['artist'], item['lyricsArtist'], item['musicArtist'])

with open("proccessed_lyrics.json", "w") as write_file:
    json.dump(data, write_file)

