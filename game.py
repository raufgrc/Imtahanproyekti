import tkinter as tk
from tkinter import messagebox
from questions import *

class Game:
    def __init__(self, window, player_name):
        self.window = window
        self.player_name = player_name

        self.moneys = [1000, 2000, 5000, 10000, 20000,
                       40000, 80000, 150000, 300000, 1000000]

        self.questions = questions()

        self.index = 0
        self.money = 0
        self.correct = 0
        self.wrong = 0

        self.jokers = {
            "50": True,
            "call": True,
            "audience": True
        }

        self.buttons = {}

        self.setup()
        self.next_question()

    def setup(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.window, bg="#0b0f2f")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label = tk.Label(
            frame,
            text="",
            fg="white",
            bg="#1a1f4f",
            font=("Verdana", 15, "bold"),
            wraplength=300,
            width=35,
            pady=15,
            padx=10,
        )
        self.label.pack(pady=(20, 25))

        for key in ["A", "B", "C", "D"]:
            btn = tk.Button(
                frame,
                text="",
                width=35,
                height=2,
                font=("Verdana", 11, "bold"),
                bg="#2a2f6f",
                fg="white",
                relief="flat",
                activebackground="#4b4fff",
                command = lambda k=key: self.check(k)
            )
            btn.pack(pady=5)
            self.buttons[key] = btn

        joker_frame = tk.Frame(frame, bg="#0b0f2f")
        joker_frame.pack(pady=15)

        tk.Button(joker_frame, text="50/50",bg="blue", command=self.joker_50,fg="white").pack(side="left", padx=8)
        tk.Button(joker_frame, text="Dostdan Kömək",bg="blue", command=self.joker_friend,fg="white").pack(side="left", padx=8)
        tk.Button(joker_frame, text="Tamaşaçılardan Kömək",bg="blue", command=self.joker_audience,fg="white").pack(side="left", padx=8)

    def next_question(self):
        if self.index >= len(self.questions):
            self.end_game()
            return

        q = self.questions[self.index]
        self.label.config(text=f"{q[0]}")

        for i, key in enumerate(["A", "B", "C", "D"]):
            self.buttons[key].config(
                text=f"{key}: {q[1][i]}",
                state="normal",
                bg="#2a2f6f"
            )

    def check(self, ans):
        q = self.questions[self.index]

        if ans == q[2]:
            self.money = self.moneys[self.index]
            self.correct += 1

            self.buttons[ans].config(bg="green")

            messagebox.showinfo("Doğru!", f"Təbriklər, siz artıq {self.money} qazandınız")

            self.index += 1
            self.next_question()
        else:
            self.wrong += 1

            self.buttons[ans].config(bg="red")
            self.buttons[q[2]].config(bg="green")

            messagebox.showerror("Səhv!", f"Düzgün cavab: {q[2]}-dir!")

            self.end_game()

        if self.index == 7:
            if messagebox.askyesno("Info","Siz artıq 7-ci sualdansınız,davam etmık istəyirsiniz?"):
                return
            else:
                self.end_game()

        if self.index == 10:
            messagebox.showinfo("Təbriklər!","Siz böyük mükafatın sahibisiniz!")


    def joker_50(self):
        if not self.jokers["50"]:
            return

        q = self.questions[self.index]
        wrong = ["A", "B", "C", "D"]
        wrong.remove(q[2])

        removed = random.sample(wrong, 2)

        for r in removed:
            self.buttons[r].config(state="disabled")

        messagebox.showinfo("50/50", f"{removed} silindi")
        self.jokers["50"] = False

    def joker_friend(self):
        if not self.jokers["call"]:
            return
        q = self.questions[self.index]
        messagebox.showinfo("Dostdan Kömək", f"Məncə cavab {q[2]}-dir! ")
        self.jokers["call"] = False

    def joker_audience(self):
        if not self.jokers["audience"]:
            return

        q = self.questions[self.index]

        messagebox.showinfo("Tamaşaçı", f"Çoxluq {q[2]} cavabı doğrudur deyir!")
        self.jokers["audience"] = False

    def end_game(self):
        messagebox.showinfo(
            "Nəticə",
            f"Adınız: {self.player_name}\nQazandığınız Pul: {self.money}\nDoğru Cavab Sayı: {self.correct}"
        )
        self.window.quit()