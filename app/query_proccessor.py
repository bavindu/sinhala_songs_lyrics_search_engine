from sinling import SinhalaTokenizer, word_splitter

tokenizer = SinhalaTokenizer()
artist_consider = [ 'කීව', 'කී','ගයන', 'ගායනා','ගේ','ගැයූ']


def query_process(query):
    artist_flag = False
    splited_sentence = tokenizer.tokenize(query)
    print(splited_sentence)
    for word in splited_sentence:
        if word in artist_consider:
            artist_flag = True
            break
        else:
            print(word_splitter.split(word))
            affix = word_splitter.split(word)['affix']
            base = word_splitter.split(word)['base']
            print(affix)
            if affix in artist_consider:
                artist_flag = True
                query = query+' '+base
                break
    print(artist_flag)
    if artist_flag:
        body = {
            "query": {
                "multi_match": {
                    "type": "most_fields",
                    "query": query,
                    "fields": ["artist^3.0",
                               "lyrics^1.0",
                               "title^1.0",
                               "musicArtist^1.0",
                               "lyricsArtist^1.0",
                               "genre^1.0",
                               "movie^1.0"
                               ]
                }
            },
            "aggs": {
                "rate_range": {
                    "range": {
                        "field": "rate",
                        "ranges": [
                            {
                                "from": 0,
                                "to": 1000
                            },
                            {
                                "from": 1000,
                                "to": 2000
                            },
                            {
                                "from": 2000,
                                "to": 3000
                            },
                            {
                                "from": 3000,
                                "to": 4000
                            },
                            {
                                "from": 4000,
                                "to": 5000
                            },
                            {
                                "from": 5000,
                                "to": 6000
                            },
                            {
                                "from": 6000,
                                "to": 7000
                            },
                            {
                                "from": 7000,
                                "to": 8000
                            },
                            {
                                "from": 8000,
                                "to": 9000
                            },
                            {
                                "from": 9000,
                                "to": 10000
                            }
                        ]
                    }
                }
            }
        }
    else:
        body = {
            "query": {
                "multi_match": {
                    "type": "most_fields",
                    "query": query,
                    "fields": ["artist",
                               "lyrics",
                               "title",
                               "musicArtist",
                               "lyricsArtist",
                               "genre",
                               "movie"
                               ]
                }
            },
            "aggs": {
                "rate_range": {
                    "range": {
                        "field": "rate",
                        "ranges": [
                            {
                                "from": 0,
                                "to": 1000
                            },
                            {
                                "from": 1000,
                                "to": 2000
                            },
                            {
                                "from": 2000,
                                "to": 3000
                            },
                            {
                                "from": 3000,
                                "to": 4000
                            },
                            {
                                "from": 4000,
                                "to": 5000
                            },
                            {
                                "from": 5000,
                                "to": 6000
                            },
                            {
                                "from": 6000,
                                "to": 7000
                            },
                            {
                                "from": 7000,
                                "to": 8000
                            },
                            {
                                "from": 8000,
                                "to": 9000
                            },
                            {
                                "from": 9000,
                                "to": 10000
                            }
                        ]
                    }
                }
            }
        }
    return body
