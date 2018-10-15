
# coding: utf-

import songLyrics
import Algorithmia

def swear_dict(song_name):
    lyrics = songLyrics.song_lyrics(song_name)
    input = [
      lyrics
    ]
    client = Algorithmia.client('sim75MbSTx0U75XD1VPhjc1rQyX1')
    algo = client.algo('nlp/ProfanityDetection/1.0.0')
    return algo.pipe(input).result
