import tkinter as tk
import fnmatch
import os
from pygame import mixer 
from tkinter.filedialog import askdirectory


VER = "1.2.4"   # default-version-value 
Font = ("Gaborila", 14)
canvas = tk.Tk()
canvas.title(f"Rock-Music: {VER}")
canvas.geometry('550x450')     # default-Dimension: 550x600
canvas.resizable(0, 0)  # not resizable  # type: ignore
canvas.config(bg="black")

rootpath = askdirectory()  #  Select the Folder
pattern = "*.mp3" 

mixer.init()


prev_img= tk.PhotoImage(file='icn/prev_img.png')
stop_img= tk.PhotoImage(file='icn/stop_img.png')
play_img= tk.PhotoImage(file='icn/play_img.png')
pause_img= tk.PhotoImage(file='icn/pause_img.png')
next_img= tk.PhotoImage(file='icn/next_img.png')


def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def pause_song():
    if PauseButton['text'] == "Pause":
        mixer.music.pause()
        PauseButton['text'] = "Play"
    else:
        mixer.music.unpause()
        PauseButton['text'] = "Pause"


label = tk.Label(canvas, text="", bg="black", fg="yellow", font=Font)
label.pack(pady=15)


listBox = tk.Listbox(canvas, fg="red", bg="black", width=100, font=Font)
listBox.pack(padx=15, pady=15)


top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')


prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg="black", borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_ = top, side='left')


StopButton = tk.Button(canvas, text="Stop", image=stop_img, bg="black", borderwidth=0, command=stop)
StopButton.pack(pady=15, in_ = top, side='left') 


PlayButton = tk.Button(canvas, text="Play", image=play_img, bg="black", borderwidth=0, command=select)
PlayButton.pack(pady=15, in_ = top, side='left') 


PauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg="black", borderwidth=0, command=pause_song)
PauseButton.pack(pady=15, in_ = top, side='left') 


NextButton = tk.Button(canvas, text="Next", image=next_img, bg="black", borderwidth=0, command=play_next)
NextButton.pack(pady=15, in_ = top, side='left') 


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
            listBox.insert('end', filename)

canvas.mainloop() 
