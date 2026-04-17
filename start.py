import tkinter.ttk as ttk
from game import *

window = tk.Tk()
window.geometry("400x300")
window.title("Kim Milyoner Olmak Ister")

player_name = ""

def clear():
    for widget in window.winfo_children():
        widget.destroy()

style = ttk.Style()
style.configure("TButton", font=("Verdana", 10), padding=5)


def start_page():
    clear()
    window.configure(bg="skyblue")

    tk.Label(window, text="Welcome to Millionaire Game", font=("Verdana", 15),bg="skyblue",fg="white").pack(pady=25)

    ttk.Button(window, text="Start", command=name_page).pack(pady=10)
    ttk.Button(window, text="Exit", command=window.quit).pack(pady=10)


def name_page():
    clear()
    window.configure(bg="skyblue")

    tk.Label(window, text="Adınızı daxil edin",font=("Verdana", 15),bg="skyblue",fg="white").pack(pady=10)

    entry = tk.Entry(window)
    entry.pack(pady=10)

    def save_name():
        global player_name
        name = entry.get()

        if name.strip() == "":
            messagebox.showerror("Xəta", "Ad daxil edin")
            return

        player_name = name
        menu_page()

    ttk.Button(window, text="OK", command=save_name).pack(pady=10)

def menu_page():
    clear()
    window.configure(bg="skyblue")

    tk.Label(window, text=f"Xos Gəldiniz {player_name}",bg="skyblue",fg="white",font=("Verdana", 15)).pack(pady=20)

    ttk.Button(window, text="Start Game", command=game_page).pack(pady=10)
    ttk.Button(window, text="Exit Game", command=start_page).pack(pady=10)

def game_page():
    clear()

    label = tk.Label(window, text="")
    label.pack(pady=20)

    def countdown(count):
        if count > 0:
            label.config(text=f"Oyun başlayır: {count}",font=("Verdana", 15),fg="white",bg="skyblue")
            window.after(1000, countdown, count - 1)
        else:
            Game(window, player_name)

    countdown(3)


start_page()
window.mainloop()
