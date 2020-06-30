import sqlite3 as sql
from datetime import date
import os
from tkinter.filedialog import askdirectory


#SQLite browser : https//github.com/sqlitebrowser/sqlitebrowser/releases
conn = sql.connect('memories.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS memories(date TEXT , memory TEXT , photo BLOB)")

def enter_memory(date , memory , if_photo):
    if if_photo == 1:
        pass
        photo = convert_pic()
        c.execute("INSERT INTO memories VALUES(?,?,?)",(date , memory, photo) )
    else:
        pass
        c.execute("INSERT INTO memories VALUES(?,?,?)", (date, memory,None))
    print('i remembered')
    conn.commit()
    c.close()
    conn.close()

def input_memory():
    today = str(date.today())
    memory = input('what do you want to remember?')
    print('is there a photo? y/n')
    y = input()
    if y == 'y':
        ask = 1
        enter_memory(today , memory , ask)
    else:
        ask = -1
        enter_memory(today , memory , ask)


def remember_about():
    is_about = input('what to remember about?')
    c.execute("SELECT * FROM memories WHERE memory LIKE (?)", ('%'+is_about+'%',) )
    data = c.fetchall()
    for row in data:
        print(row)

def convert_pic():
    directory = askdirectory()
    os.chdir(directory)
    for f in os.listdir(directory):
        if f.endswith('.jpg'):
            print(f)
    image = input()
    file_name = image
    with open(file_name , 'rb') as file:
        photo = file.read()
    return photo

create_table()
input_memory()