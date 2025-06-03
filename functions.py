import pygame

def toggle_pause(is_paused, button):
    if is_paused:
        pygame.mixer.music.unpause()
        button.config(text="Pause")
        return False
    else:
        pygame.mixer.music.pause()
        button.config(text="Unpause")
        return True

def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def on_song_select(event, songs, folder, status_label):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        song_name = songs[index]
        song_path = folder / song_name
        pygame.mixer.music.load(str(song_path))
        pygame.mixer.music.play()
        status_label.config(text=f"Playing: {song_name}")

