
# coding: utf-

from songLyrics import song_lyrics
import Algorithmia

def swear_dict(song_name):
    lyrics = song_lyrics(song_name)
    input = [
      lyrics
    ]
    client = Algorithmia.client('sim75MbSTx0U75XD1VPhjc1rQyX1')
    algo = client.algo('nlp/ProfanityDetection/1.0.0')
    return algo.pipe(input).result
