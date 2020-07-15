import os
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog
mixer.init()
class song(object):
    def __init__(self):
        pass
    def add_song(self):
        pass
class list_of_song(object):
    def __init__(self):
        self.list = []
class data(object):
    pass
class save(object):
    pass
class status(object):
    def __int__(self,a,b):
        self.which = a
        self.is_mute =b
l= list_of_song()
what = status()
what.which = 0 ; what.is_mute = 0
#main things of the window
root = Tk()

root.title('Melody')
root.iconbitmap(r'icon.ico')
root.configure(bg = 'coral')
left_frame = Frame(root)
left_frame.pack(side = LEFT)
right_frame = Frame(root)
right_frame.pack(side= RIGHT)
#menubar
menubar = Menu(root)
root.config(menu =menubar)




def select_directory():
    global file_name
    file_name = filedialog.askopenfile()
    print(file_name.name)

#SHOW LYRICS , SHOW DITAILS(BY PARTITION OR ALL) , SHOW THE PICTURE(OS TO MAKE  NAMES THE SAME)
#SAVE SHOW THE SAVED ONES

sub_menu = Menu(menubar,tearoff =0)
menubar.add_cascade(label ='rick',menu=sub_menu)

sub_menu.add_command(label= 'select-file',command = select_directory)

#list box
lb = Listbox(right_frame)
lb.pack()
add = Button(right_frame,text = "Add")
delet = Button(right_frame,text = "Remove")
add.pack(side =LEFT) ; delet.pack(side =LEFT)
#images
play = Image.open('play.png')
pause = Image.open('pause.png')
rewind = Image.open('rewind.png')
mute = Image.open('mute.png')
valume = Image.open('valume.png')
rewind_mage = ImageTk.PhotoImage(rewind)
play_mage = ImageTk.PhotoImage(play)
pause_mage = ImageTk.PhotoImage(pause)
mute_mage = ImageTk.PhotoImage(mute)
valume_mage = ImageTk.PhotoImage(valume)
#commands
def add_single_toplaylist():
    pass
    file = file.askopenfile()
    l.list.append()
def add_folder_toplaylist():
    pass
def play():
    try:
     mixer.music.load(file_name)
     mixer.music.play()
     status['text'] = 'is playing '.upper()+os.path.basename(file_name.name)
    except:
        tkinter.messagebox.showerror('havent chosen a file ','chose a file if wanna hear')


def pause():
    pass
    if what.which ==0:
        mixer.music.pause()
        status['text'] = os.path.basename(file_name.name)+ ' is paused'.upper()
        what.which = 1
    else:
        mixer.music.unpause()
        status['text'] = 'is playing '.upper()+os.path.basename(file_name.name)
        what.which = 0

def set_val(val):
    pass
    volume = int(val)/100
    mixer.music.set_volume(volume)
def rewind():
    mixer.music.rewind()
    status['text'] = 'is playing '.upper() + os.path.basename(file_name.name)
def is_mute():
    global a
    if what.is_mute == 0:
        btn_valume.configure(image = mute_mage)
        a = mixer.music.get_volume() * 100
        set_val(0)
        what.is_mute = 1
    else:
        btn_valume.configure(image = valume_mage)
        what.is_mute = 0
        set_val(a)
#buttons
middle_frame = Frame(left_frame) #used to partition
middle_frame.pack(side = LEFT)#padx,y #grid row,column

btn_play = Button(middle_frame ,image = play_mage ,command = play)
btn_play.pack(side =LEFT)

btn_pause = Button(middle_frame ,image = pause_mage, command = pause)
btn_pause.pack(side =LEFT)

btn_rewind = Button(middle_frame,image = rewind_mage,command =rewind)
btn_rewind.pack(side =LEFT)

btn_valume = Button(middle_frame,image = valume_mage,command =is_mute)
btn_valume.pack(side =LEFT)
#valume widgete
scale = Scale(left_frame, from_ = 0 , to= 100, orient = HORIZONTAL, command = set_val)
scale.set(69)
mixer.music.set_volume(0.69)
scale.pack()

status =Label(left_frame,text = 'hi there',relief = SUNKEN)
status.pack(side = BOTTOM)
root.mainloop()
