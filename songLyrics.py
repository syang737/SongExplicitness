
# coding: utf-

import requests
import re
from bs4 import BeautifulSoup
import Algorithmia

base_url = 'http://api.genius.com'
genius_id = 'XO--EfuCoziq7UGdadut1RyRIhT9Wg4QyxvXaatsaHdjdAm8_-uKzHc4i8wPgW5F'
genius_secret = 'YLbuxciWe8utBFEqgzNKd6UhhhOqIfSGrC763rnGtMedlmiLEnIYB0MJkFLdHYrTL-5le5Z9QH5CVdOUpfa4jw'
genius_token = 'l2HmJPxr3YN9uFzKeUy4gPCSYSZnkBtdSd0EJ3vJZbRBBX5evlCm1rp-Q-_X_yFl'

headers = {
    'Authorization': 'Bearer {token}'.format(token=genius_token)
}

def song_lyrics(song_name):
  api_path = genius_search(song_name)
  lyrics = lyrics_from_song_api_path(api_path)
  return lyrics

def genius_search(song_name):
  parameters = {
      'q': song_name
  }
  search_url = base_url + '/search'
  response = requests.get(search_url, params=parameters, headers=headers)
  data = response.json()
  api_path = data['response']['hits'][0]['result']['api_path']
  return api_path


def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  #gotta go regular html scraping... come on Genius
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  #remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script')]
  #at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find('div', class_='lyrics').get_text() #updated css where the lyrics are based in HTML
  return lyrics
