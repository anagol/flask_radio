from flask import Flask, render_template, jsonify, request
import requests, bs4

app = Flask(__name__)


class Station:
    def __init__(self, url, title, picture):
        self.url = url
        self.title = title
        self.picture = picture


def track_belarus():
    s = requests.get('https://onlineradiobox.com/by/radiorelax/')
    b = bs4.BeautifulSoup(s.text, 'html.parser')
    track_tag = b.select('.active td:nth-child(2)')
    track = track_tag[0].getText()
    return track


def track_ukraine():
    s = requests.get('https://play.tavr.media/radiorelax/int/')
    b = bs4.BeautifulSoup(s.text, 'html.parser')
    track_tag = b.select('#song0')
    track = track_tag[0].getText()
    return track


relax_belarus = Station(url='http://live.humorfm.by:8000/radiorelax', title='Belarus',
                        picture='https://onlineradiomix.com/resource/images/2019/02/relaks-radio.webp')

relax_ukraine = Station(url='https://online.radiorelax.ua/RadioRelax_Int_HD', title='Ukraine',
                        picture='http://top-radio.ru/assets/image/radio/180/Relax_International.png')
#
# relax_cafe = Station(url='https://online.radiorelax.ua/RadioRelax_Cafe_HD', title='Radio Relax Cafe',
#                      picture='http://top-radio.ru/assets/image/radio/180/Relax_Cafe.png')

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
