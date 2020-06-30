import json
from urllib import request
import requests

class lyrics(object):
    def __init__(self):
        self.artists = {}
        self.keywords = {}
        self.lyrics = {}

    def search_for_lyrics(self , artist , song):
        url = 'https://api.lyrics.ovh./v1/' + artist + '/' + song
        response = requests.get(url)
        json_data = json.loads(response.content)
        a = json_data["lyrics"]
        l = []
        l = list(a) ; j = ''.join(l)
        if artist in self.lyrics:
            self.lyrics[artist][song] = j
        else:
            self.lyrics[artist] = {}
            self.lyrics[artist][song] = j

    def get_info(self , artist , song):
        self.artists[artist] = []
        self.artists[artist] . append(song)
        self.search_for_lyrics(artist , song)


a = lyrics()
si = input('singer:')
so = input('song:')
a.get_info(si , so)

k = 0
def search_number(lyrics , word):
    global k
    a = str.split(lyrics, ' ')
    l = list(a)
    for i in l:
        if word in i:
            print(i)
            k+=1
    return

for i in a.lyrics:
    for j in a.lyrics[i]:
        t = j + '.txt'
        tiki = a.lyrics[i][j]
        tik = ''.join(tiki)
        f = open(t, 'w')
        f.write(str.upper(i))
        f.write('\n'*2)
        f.write(str.upper(j))
        f.write('\n'*2)
        for word in tiki:
            f.write(word)


