import tkinter as tk
from tkinter import Label, Button
import subprocess

def start_translator():
    subprocess.run(["python", "main2.py"])  # Runs the backend

# Create main window
root = tk.Tk()
root.title("Sign Language Translator")
root.geometry("400x300")

# Heading Label
label = Label(root, text="Speech to Sign Language Translator", font=("Arial", 14))
label.pack(pady=20)

# Start Button
start_button = Button(root, text="Start Translation", command=start_translator, font=("Arial", 12))
start_button.pack(pady=20)

# Exit Button
exit_button = Button(root, text="Exit", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=20)

# Run Tkinter loop
root.mainloop()
