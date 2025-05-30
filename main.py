import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

def load_file():
    filepath = filedialog.askopenfilename(filetypes = [("MP3 Files", "*.mp3")])
    if filepath:
        pygame.mixer.music.load(filepath)
        status_label.config(text=f"Loaded: {filepath.split('/')[-1]}")

def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

root= tk.Tk()
root.title("Music player")

tk.Button(root, text="Load", command=load_file, width=10).pack(pady=5)
tk.Button(root, text="Play", command=play_music, width=10).pack(pady=5)
tk.Button(root, text="Pause", command=pause_music, width=10).pack(pady=5)
tk.Button(root, text="Unpause", command=unpause_music, width=10).pack(pady=5)
tk.Button(root, text="Stop", command=stop_music, width=10).pack(pady=5)


status_label = tk.Label(root, text="No file loaded")
status_label.pack(pady=10)

root.mainloop()