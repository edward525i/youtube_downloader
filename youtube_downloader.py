import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import subprocess

def Widgets():
    head_label = Label(root, text="Descarcă videoclip",
                       padx=15, pady=15,
                       font="SegoeUI 14",
                       bg="palegreen1",
                       fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    link_label = Label(root,
                       text="YouTube link :",
                       bg="salmon",
                       pady=5,
                       padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root,
                              text="Destinație :",
                              bg="salmon",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root,
                      text="Caută",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    Download_B = Button(root,
                        text="Descarcă video",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4, column=1, pady=20, padx=20)

def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH",
                                                 title="Save Video")
    download_Path.set(download_Directory)

def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()

    if not Youtube_link.startswith("https://www.youtube.com"):
        messagebox.showerror("Eroare", "Te rog introdu un link YouTube valid!")
        return

    if not download_Folder:
        messagebox.showerror("Eroare", "Te rog selectează o destinație pentru descărcare!")
        return

    try:
        command = [
            "yt-dlp",
            "--output", f"{download_Folder}/%(title)s.%(ext)s",
            Youtube_link
        ]
        subprocess.run(command, check=True)

        messagebox.showinfo("SUCCES!",
                            f"Videoclipul s-a descărcat cu succes în:\n{download_Folder}")
    except Exception as e:

        messagebox.showerror("Eroare", f"Descărcarea a eșuat: {e}")

root = tk.Tk()

root.geometry("520x280")
root.resizable(False, False)
root.title("GUI")
root.config(background="PaleGreen1")

video_Link = StringVar()
download_Path = StringVar()

Widgets()

root.mainloop()
