import scrapy
import re
from ..items import LyricsscrapeItem
import locale



def lyrics_processor(block):
    tempLirics = []
    if block is not None:
        lyrics = block.split("\n")
        for line in lyrics:
            isChodeContain = re.search('[a-zA-Z]', line)
            line = line.strip()
            if isChodeContain is None and len(line) > 0:
                tempLirics.append(line)
    return tempLirics


class LyricsSpider(scrapy.Spider):
    name = 'lyrics'
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    counter =1

    def start_requests(self):
        url = 'https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page='
        for page in range(1, 23):
            yield scrapy.Request(url=url+str(page), callback=self.link_parse)

    def link_parse(self, response):
        songLinks = response.xpath("//a[@class='_blank']/@href").extract()
        if len(songLinks) != 0:
            for link in songLinks:
                yield response.follow(link, callback=self.parse)

    def parse(self, response):
        unknown = "Unknown"
        song = LyricsscrapeItem()
        lyrics = []
        title = response.xpath('//span[@class = "sinTitle"]/text()').extract_first()
        if title is None:
            title = response.xpath(
                '//h1[@class = "entry-title"]/text()').extract_first()
            temp = title.split("–")
            if temp is not None and len(temp) == 1:
                temp = title.split("-")
            title = temp[1].strip()
        artist = response.xpath(
            '//span[@class = "entry-categories" and contains(text(),"Artist: ")]/a/text()').extract_first()
        lyricsArtist = response.xpath('//span[@class = "lyrics"]/a/text()').extract_first()
        musicArtist = response.xpath('//span[@class = "music"]/a/text()').extract_first()
        genre = response.xpath('//span[@class = "entry-tags"]/a/text()').extract_first()
        rate = response.xpath('//div[@class = "tptn_counter"]/text()').extract_first()
        rate = rate[3:-6]
        rate = locale.atoi(rate)
        movie = response.xpath('//span[@class = "movies"]/a/text()').extract_first()
        share = response.xpath('//span[@class = "swp_count "]/text()').extract_first().strip()
        share = locale.atoi(share)
        chorus = response.xpath('//span[contains(text(),"CHORUS")]/following-sibling::text()').extract_first()
        verse = response.xpath('//span[contains(text(),"VERSE")]/following-sibling::text()').extract_first()
        if verse is None:
            verse = response.xpath('//span[contains(text(),"VEARSE")]/following-sibling::text()').extract_first()
        verse1 = response.xpath('//span[contains(text(),"VERSE 1")]/following-sibling::text()').extract_first()
        if verse1 is None:
            verse1 = response.xpath('//span[contains(text(),"VEARSE 1")]/following-sibling::text()').extract_first()
        verse2 = response.xpath('//span[contains(text(),"VERSE 2")]/following-sibling::text()').extract_first()
        if verse2 is None:
            verse2 = response.xpath('//span[contains(text(),"VEARSE 2")]/following-sibling::text()').extract_first()
        verse3 = response.xpath('//span[contains(text(),"VERSE 3")]/following-sibling::text()').extract_first()
        if verse3 is None:
            verse3 = response.xpath('//span[contains(text(),"VEARSE 3")]/following-sibling::text()').extract_first()
        if artist == "Unknown":
            artist = None
        if lyricsArtist == "Unknown":
            lyricsArtist = None
        if musicArtist == "Unknown":
            musicArtist = None
        if genre == "Unknown":
            genre = None
        if movie == "Unknown":
            movie = None
        lyrics = lyrics + lyrics_processor(chorus)
        lyrics += lyrics_processor(verse)
        lyrics += lyrics_processor(verse1)
        lyrics += lyrics_processor(verse2)
        lyrics += lyrics_processor(verse3)

        song['id'] = self.counter
        song['title'] = title
        song['artist'] = artist
        song['lyricsArtist'] = lyricsArtist
        song['lyrics'] = lyrics
        song['musicArtist'] = musicArtist
        song['genre'] = genre
        song['rate'] = rate
        song['movie'] = movie
        song['share'] = share
        self.counter = self.counter + 1

        yield song

