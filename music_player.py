#music player using python

import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        
        self.music_file_label = tk.Label(self.master, text="No file selected")
        self.music_file_label.pack(pady=10)
        
        self.select_button = tk.Button(self.master, text="Select Music", command=self.select_music)
        self.select_button.pack(pady=5)
        
        self.play_button = tk.Button(self.master, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)
        
        self.resume_button = tk.Button(self.master, text="Resume", command=self.resume_music)
        self.resume_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)
        
        self.music_file = None
        self.playing = False
        
    def select_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("Music Files","*.mp3")])
        if self.music_file:
            self.music_file_label.config(text=self.music_file)
    
    def play_music(self):
        if self.music_file and not self.playing:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play(-1)
            self.playing = True
    
    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
    
    def resume_music(self):
        if not self.playing:
            pygame.mixer.music.unpause()
            self.playing = True
    
    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
    