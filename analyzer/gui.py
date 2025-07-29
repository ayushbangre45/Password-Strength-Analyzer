import tkinter as tk
from tkinter import messagebox
from analyzer.password_analyzer import analyze_password
from analyzer.wordlist_generator import generate_wordlist

def run_gui():
    def analyze():
        pwd = pwd_entry.get()
        if pwd:
            result = analyze_password(pwd)
            feedback = result['feedback']['suggestions']
            messagebox.showinfo("Password Score", f"Score: {result['score']}/4\nSuggestions: {', '.join(feedback) if feedback else 'Good Password!'}")

    def generate():
        name = name_entry.get()
        pet = pet_entry.get()
        year = year_entry.get()
        if name and pet and year:
            path = generate_wordlist(name, pet, year)
            messagebox.showinfo("Wordlist Generated", f"Saved to: {path}")

    root = tk.Tk()
    root.title("Password Analyzer & Wordlist Generator")
    root.geometry("400x300")

    tk.Label(root, text="Password:").pack()
    pwd_entry = tk.Entry(root, show="*")
    pwd_entry.pack()
    tk.Button(root, text="Analyze Password", command=analyze).pack(pady=5)

    tk.Label(root, text="--- Wordlist Generator ---").pack(pady=10)
    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Pet Name:").pack()
    pet_entry = tk.Entry(root)
    pet_entry.pack()

    tk.Label(root, text="Year:").pack()
    year_entry = tk.Entry(root)
    year_entry.pack()

    tk.Button(root, text="Generate Wordlist", command=generate).pack(pady=10)
    root.mainloop()
