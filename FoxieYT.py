import tkinter as tk
from tkinter import simpledialog
from pytube import YouTube
import subprocess

root = tk.Tk()
root.withdraw()

youtube_url = simpledialog.askstring(title="Lecteur YouTube",
                                     prompt="Entrez l'URL de la vidéo YouTube à lire:")

yt = YouTube(youtube_url)
stream = yt.streams.filter(file_extension='mp4').first()
file_path = stream.download()

subprocess.Popen(["vlc", file_path])
