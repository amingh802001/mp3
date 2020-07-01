from tinytag import TinyTag
import os

class ordering (object):
    def __init__(self):
        self.song_query = {}
        self.liked_songs = {}
        self.ordered_by_spec_var = {}
    def add_song(self,song_path):
        pass
        a = self.make_dic_of_datas(song_path)
        self.song_query[a['title']] = a

    def make_dic_of_datas(self,path):
        tag = TinyTag.get(path)
        str_tag = str(tag);
        t = list(str_tag)
        t.remove(t[0]);
        t.remove(t[-1]);
        lisa = ''.join(t)
        lisa = str.split(lisa, ',')
        lisa_dict = {}
        for t in lisa:
            l = list(t)
            ll = l[:];
            j = 0
            for i in range(len(ll)):
                j += 1
                if ll[i] == '"':
                    j -= 1
                    l.remove(l[j])
            l = ''.join(l);
            l = str.split(l, ':')
            go = list(l[0])
            if go[0] == ' ':
                go.remove(go[0])

            goo = list(l[1])
            if goo[0] == ' ':
                goo.remove(goo[0])
            go = ''.join(go).lower() ; goo = ''.join(goo).lower()
            lisa_dict[go] = goo
        lisa_dict['directory'] = path
        lisa_dict['liked'] = -1
        return lisa_dict

    def like_a_song(self,song_name):
        pass
        there = -1
        for song in self.song_query:
            if song_name in song:
                song_name = song
                self.song_query[song_name]['liked'] = 1
                there = 1
                break
        if there == -1:
            print(song_name + ' not found')


    def order_by (self , order_var):
        pass
        self.ordered_by_spec_var[order_var] = {}
        for song in self.song_query:
            if self.song_query[song][order_var] not in self.ordered_by_spec_var[order_var]:
                self.ordered_by_spec_var[order_var][self.song_query[song][order_var]] = []
                self.ordered_by_spec_var[order_var][self.song_query[song][order_var]].append(song)
            else :
                self.ordered_by_spec_var[order_var][self.song_query[song][order_var]].append(song)

    def show_all(self):
        pass
        for songs in self.song_query:
            for data in self.song_query[songs]:
                print(data ,':', self.song_query[songs][data])

    def show_likedsongs(self):
        pass
        for song in self.song_query:
            if self.song_query[song]['liked'] == 1:
                print(song)

    def show_by_particular_order(self,order):
        pass
        for i in self.ordered_by_spec_var:
            print(self.ordered_by_spec_var[order])
a = ordering()
destdir = os.curdir

files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

song_list  = []
