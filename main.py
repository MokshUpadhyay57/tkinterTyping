import tkinter as tk
from tkinter import messagebox
from tkinter import END
import time
import random


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Assessment")
        self.text = tk.Text(self.root, width=50, height=10, font=('Arial', 12))
        self.text.pack()
        self.text.insert('1.0', "The quick brown fox jumps over the lazy dog.")
        self.text.config(state='disabled')
        self.entry = tk.Text(self.root, width=50,
                             height=10, font=('Arial', 12))
        self.entry.pack()
        self.entry.config(state='normal')
        self.entry.focus_set()
        self.entry.bind("<Return>", self.check_speed)
        self.label = tk.Label(
            self.root, text="Type the text above and press Enter.")
        self.label.pack()
        self.label2 = tk.Label(self.root, text="")
        self.label2.pack()
        self.start_time = time.time()

    def check_speed(self, event):
        self.entry.config(state='disabled')
        self.text.config(state='normal')
        self.text.config(state='disabled')
        self.entry.delete('1.0', tk.END)
        self.text.config(state='normal')
        self.label.config(text="Your typing speed is: ")
        self.label2.config(text="")
        self.root.update_idletasks()
        time.sleep(1)
        self.label2.config(text="seconds.")
        self.root.update_idletasks()
        end_time = time.time()
        time_taken = end_time - self.start_time
        entered_text = self.entry.get("1.0", END)
        words_typed = len(entered_text.split())
        # Calculate words per minute
        typing_speed = words_typed / (time_taken / 60)
        self.label2.config(text=f"Your typing speed is {
                           typing_speed:.2f} words per minute.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
