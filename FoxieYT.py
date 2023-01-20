import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from pytube import YouTube
import subprocess

root = tk.Tk()
root.withdraw()
ttk.Style().theme_use('clam')
root.geometry("1200x1200")

youtube_url = simpledialog.askstring(title="DevFoxie YouTube :)",
                                     prompt="Entrez l'URL de la vidéo YouTube à lire:",
                                     parent=root,
                                     initialvalue='',
                                     minvalue=0,
                                     maxvalue=100)

yt = YouTube(youtube_url)
stream = yt.streams.filter(file_extension='mp4').first()
file_path = stream.download()

subprocess.Popen(["vlc", file_path])
