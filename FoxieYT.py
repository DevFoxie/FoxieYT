import subprocess
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

youtube_url = simpledialog.askstring(title="Lecteur YouTube",
                                     prompt="Entrez l'URL de la vidéo YouTube à lire:")

subprocess.Popen(['C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC', youtube_url])
