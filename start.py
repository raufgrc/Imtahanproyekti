import tkinter as tk
from tkinter import ttk
from game import Game
import tkinter.messagebox as messagebox

class App:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x300")
        self.window.title("Kim Milyoner Olmak Ister")
        self.window.configure(bg="skyblue")

        self.player_name = ""

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Verdana", 10), padding=5)

        self.current_page = None
        self.show_page(StartPage)

    def show_page(self, page_class):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = page_class(self)
        self.current_page.pack(fill="both", expand=True)


class StartPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.window, bg="skyblue")
        self.app = app

        tk.Label(self, text="Welcome to Millionaire Game",font=("Verdana", 15), bg="skyblue", fg="white").pack(pady=25)

        ttk.Button(self, text="Start",command=lambda: self.app.show_page(NamePage)).pack(pady=10)
        ttk.Button(self, text="Exit",command=self.app.window.quit).pack(pady=10)


class NamePage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.window, bg="skyblue")
        self.app = app
        tk.Label(self, text="Adınızı daxil edin",font=("Verdana", 15), bg="skyblue", fg="white").pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        ttk.Button(self, text="OK",command=self.save_name).pack(pady=10)

    def save_name(self):
        name = self.entry.get()
        if name == "":
            messagebox.showerror("Səhv!", "Ad daxil etməlisiniz!")
            return

        self.app.player_name = name
        self.app.show_page(MenuPage)


class MenuPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.window, bg="skyblue")
        self.app = app

        tk.Label(self,
                 text=f"Xoş Gəldiniz {self.app.player_name}",
                 bg="skyblue", fg="white",
                 font=("Verdana", 15)).pack(pady=20)

        ttk.Button(self, text="Start Game",command=self.start_game).pack(pady=10)
        ttk.Button(self, text="Exit Game",command=lambda: self.app.show_page(StartPage)).pack(pady=10)

    def start_game(self):
        for widget in self.app.window.winfo_children():
            widget.destroy()

        label = tk.Label(self.app.window)
        label.pack(pady=20)

        self.countdown(label, 3)

    def countdown(self, label, count):
        if count > 0:
            label.config(
                text=f"Oyun başlayır: {count}",
                font=("Verdana", 15),
                fg="white",
                bg="skyblue"
            )
            self.app.window.after(1000, self.countdown, label, count - 1)
        else:
            Game(self.app.window, self.app.player_name)
