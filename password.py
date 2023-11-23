import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator by Hansraj")
        master.geometry("400x300")
        master.configure(bg="#f0f0f0")

        self.title_label = tk.Label(master, text="Password Generator by Hansraj", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=(20, 10))

        self.complexity_label = tk.Label(master, text="Select Complexity:", font=("Helvetica", 12), bg="#f0f0f0")
        self.complexity_label.pack()

        self.choice = tk.IntVar()
        self.options = [("Simple", 1), ("Moderate", 2), ("Complex", 3)]

        for text, value in self.options:
            tk.Radiobutton(master, text=text, variable=self.choice, value=value, font=("Helvetica", 10), bg="#f0f0f0").pack(anchor=tk.W)

        self.create_button = tk.Button(master, text="Create Password", bd=5, height=2, command=self.generate_password, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
        self.create_button.pack(pady=(20, 10))

        self.copy_button = tk.Button(master, text="Copy Password", bd=5, height=2, command=self.copy_to_clipboard, font=("Helvetica", 12, "bold"), bg="#008CBA", fg="white")
        self.copy_button.pack()

        self.password_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.password_label.pack(pady=(20, 10))

    def generate_password(self):
        complexity = self.choice.get()
        password = self.passgen(complexity)
        self.password_label.config(text=password)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password:
            master.clipboard_clear()
            master.clipboard_append(password)
            master.update()
            messagebox.showinfo("Password Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Generate a password first!")

    def passgen(self, complexity):
        simple = string.ascii_letters + string.digits
        moderate = simple + string.punctuation
        complex_chars = moderate + string.ascii_letters

        if complexity == 1:
            return "".join(random.choice(simple) for _ in range(4))
        elif complexity == 2:
            return "".join(random.choice(moderate) for _ in range(6))
        elif complexity == 3:
            return "".join(random.choice(complex_chars) for _ in range(8))

if __name__ == "__main__":
    master = tk.Tk()
    app = PasswordGeneratorApp(master)
    master.mainloop()
