import os
import pygame
import tkinter as tk
from tkinter import *
from mutagen.id3 import ID3
from tkinter.filedialog import askdirectory

print('valu bilub dub du')
#window
player = tk.Tk()
player.title('Music player')
player.geometry("205x340")

#get song
file = "song"
real_names = []
list_of_songs = []

def chose_directory():
    directory = askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            realdir = os.path.realpath(file)
            try:
                audio = ID3(realdir)
                real_names.append(audio["TIT2"])
                list_of_songs.append(file)
            except:
                pass
chose_directory()
#playlist
playlist = tk.Listbox(player , highlightcolor = "yellow" , selectmode = tk.SINGLE)

real_names.reverse()

for items in list_of_songs:
    playlist.insert(0 , items)

# valume input
valume_level = tk.Scale(player,from_=0.0,to_=1.0 ,
               orient = tk.HORIZONTAL , resolution = 0.01)
# song name

var = tk.StringVar()
song_title = tk.Label(player,textvariable = var)


#pygame init

pygame.init()
pygame.mixer.init()

#action events

def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(valume_level.get())

def exit():
    pygame.mixer.music.stop()

def pause(): 
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


#register buttons

play_butt = tk.Button(player,width=5,height=3 , text ="play", command= play)
stop_butt = tk.Button(player, text = "Stop" , width=5,height=3, command= exit)
pause_butt = tk.Button(player, text = "Pause" , width=5,height=3, command= pause)
unpause_butt = tk.Button(player, text = "UnPause", width=5 , height = 3 , command=unpause)
#song


# activate
song_title.pack()
play_butt.pack(fill="x")
stop_butt.pack(fill="x")
pause_butt.pack(fill="x")
unpause_butt.pack(fill="x")
valume_level.pack(fill="x")
playlist.pack(fill = "both",expand="yes")
player.mainloop()
