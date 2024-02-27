import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Themed Tkinter Example")

label = ttk.Label(root, text="Hello, Themed Tkinter!")
label.pack()

button = ttk.Button(root, text="Click Me")
button.pack()

entry = ttk.Entry(root)
entry.pack()

root.mainloop()