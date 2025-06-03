import tkinter as tk
from tkinter import filedialog
import pygame
from pathlib import Path
from functions import *

pygame.mixer.init()
root = tk.Tk()

audio_extensions = [".mp3", ".waw", ".ogg", ".flac"]
folder = Path("./music")
songs = []

#The left frame should contain things that are specific to the user, like his songlist, playlist, favorites etc
#Visualizer button is here temporarily
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10, pady=10)

#Center Frame is reserved for the main window, currently it only has the option to show all songs
center_frame = tk.Frame(root)
center_frame.pack(expand=True, fill="both", padx=10, pady=10)

#The bottom frame is for song options, like volume level, back, next, pause etc.
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="x", pady=10)

listbox = tk.Listbox(center_frame, width=40, height=15)

#Lists all songs inside the music folder, 
#TODO:Add a way to access all the music on PC
for file in folder.iterdir():
    if file.is_file() and file.suffix.lower() in audio_extensions:
        songs.append(file.name)

is_paused = False

#Inserts the songs into the list box
for song in songs:
    listbox.insert(tk.END, song)

def handle_song_select(event):
    on_song_select(event, songs, folder, status_label)

def handle_toggle_pause():
    global is_paused
    is_paused = toggle_pause(is_paused, PauseUnpauseButton)

listbox.bind("<<ListboxSelect>>", handle_song_select)

root.title("Music player")

playlistButton = tk.Button(left_frame, text="Playlists", width=12)
songsButton = tk.Button(left_frame, text="Songs", width=12)
favoritesButton = tk.Button(left_frame, text="Favorites", width=12)
visualizerButton = tk.Button(left_frame, text="Visualizer", width=12)

playlistButton.pack(pady=5)
songsButton.pack(pady=5)
favoritesButton.pack(pady=5)
visualizerButton.pack(pady=5)

scrollbar = tk.Scrollbar(center_frame)
scrollbar.pack(side="right", fill="y")

listbox.pack(side="left", expand=True, fill="both")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

playButton = tk.Button(bottom_frame, text="Play", command=play_music, width=10)
PauseUnpauseButton = tk.Button(bottom_frame, text="Pause", command=handle_toggle_pause, width=10)
StopButton = tk.Button(bottom_frame, text="Stop", command=stop_music, width=10)

playButton.pack(side="left", padx=5, pady=5)
PauseUnpauseButton.pack(side="left", padx=5, pady=5)
StopButton.pack(side="left", padx=5, pady=5)

volume_scale = tk.Scale(bottom_frame, from_=0, to=100, orient="horizontal", label="Volume")
volume_scale.set(50)
volume_scale.pack(side="bottom", fill="x", padx=20)

def update_volume(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)

volume_scale.config(command=update_volume)

status_label = tk.Label(root, text="No file loaded")
status_label.pack(pady=10)

root.mainloop()