# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LyricsscrapeItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    lyricsArtist = scrapy.Field()
    lyrics = scrapy.Field()
    musicArtist = scrapy.Field()
    genre = scrapy.Field()
    rate = scrapy.Field()
    movie = scrapy.Field()
    share = scrapy.Field()
