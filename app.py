import bs4
import requests
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def track_belarus():
    s = requests.get('https://onlineradiobox.com/by/radiorelax/')
    b = bs4.BeautifulSoup(s.text, 'html.parser')
    track_tag = b.select('.active td:nth-child(2)')
    track = track_tag[0].getText()
    return track


def track_ukraine():
    s = requests.get('https://play.tavr.media/radiorelax/int/')
    b = bs4.BeautifulSoup(s.text, 'html.parser')
    track_tag_singer = b.select('#singer0')
    track_tag_song = b.select('#song0')
    track = track_tag_singer[0].getText() + ' - ' + track_tag_song[0].getText()
    return track


class Station:
    def __init__(self, url, title, picture):
        self.url = url
        self.title = title
        self.picture = picture


relax_belarus = Station(url='http://live.humorfm.by:8000/radiorelax', title='Belarus',
                        picture='https://onlineradiomix.com/resource/images/2019/02/relaks-radio.webp')

relax_ukraine = Station(url='https://online.radiorelax.ua/RadioRelax_Int_HD', title='Ukraine',
                        picture='http://top-radio.ru/assets/image/radio/180/Relax_International.png')

stations = [relax_belarus, relax_ukraine]
parsers = {'Belarus': track_belarus,
           'Ukraine': track_ukraine}


@app.route('/')
def index():
    return render_template('index.html', stations=stations)


@app.route('/track')
def get_track():
    station = request.args.get('station')
    track = parsers[station]()
    return jsonify(track=track)


if __name__ == '__main__':
    app.run()
