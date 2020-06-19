import bs4
import requests

s = requests.get('https://play.tavr.media/radiorelax/int/')
b = bs4.BeautifulSoup(s.text, 'html.parser')
track_tag_singer = b.select('#singer0')
track_tag_song = b.select('#song0')
track = track_tag_singer[0].getText() + ' ' + track_tag_song[0].getText()
print(track)
