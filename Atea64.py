# библеотеки
import customtkinter as ctk
import yt_dlp
import tkinter as tk

from darkdetect import theme

# настройки видео
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'merge_output_format': 'mp4',
    'outtmpl': 'downloaded_video/%(title)s.%(ext)s',
}

# тема программы
ctk.set_appearance_mode("System")

# функции
def downloading_video():
    url = word.get()
    if url.strip():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def paste_from_clipboard():
    try:
        clipboard_text = root.clipboard_get()
        word.insert(tk.INSERT, clipboard_text)
    except tk.TclError:
        print("Буфер обмена пуст или содержит неподдерживаемые данные")

def change_theme():
    selected_theme = dropdown.get()
    ctk.set_appearance_mode(selected_theme)

# сама программа
options = ["Dark", "Lignt", "Blue"]

root = ctk.CTk()
root.title("Atea64")
root.geometry("640x480")
root.resizable(False, False)
root.clipboard_get()
root.update_idletasks()

name_programm = ctk.CTkLabel(root, text="Atea64", font=("Days Regular", 36))
name_programm.place(x=250, y=50)
slogan_programm = ctk.CTkLabel(root, text="Скачивай видео с YouTube и других видеохостингов", font=("Days Regular", 12))
slogan_programm.place(x=150, y=130)
button = ctk.CTkButton(root, text="скачать видео", command=downloading_video, fg_color="green", hover_color="#014609", font=("Days Regular", 12))
button.pack(side="bottom",pady=50)
paste_button = ctk.CTkButton(root, text="Вставить из буфера", command=paste_from_clipboard, font=("Days Regular", 12))
paste_button.pack(side="bottom")
word = ctk.CTkEntry(root)
word.pack(side="bottom",pady=50)
dropdown = ctk.CTkOptionMenu(root, values=["Light", "Dark", "System"], font=("Days Regular", 12))
dropdown.place(x=20, y=350)
dropdown_button = ctk.CTkButton(root, text="применить изменения", command=change_theme, font=("Days Regular", 12))
dropdown_button.place(x=20, y=400)
dropdown.set("System")

root.mainloop()

