import tkinter as tk
from tkinter import ttk
import sqlite3

def create_user_table():
    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
    ''')

    connection.commit()
    connection.close()

def save_user():
    username = entry_username.get()
    email = entry_email.get()

    connection = sqlite3.connect('user_database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))

    connection.commit()
    connection.close()

    clear_entries()

def clear_entries():
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("User Page")
root.geometry("400x200")

# Create User Table
create_user_table()

# Labels
label_username = ttk.Label(root, text="Username:")
label_email = ttk.Label(root, text="Email:")

# Entry Widgets
entry_username = ttk.Entry(root)
entry_email = ttk.Entry(root)

# Save Button
save_button = ttk.Button(root, text="Save User", command=save_user)

# Grid Layout
label_username.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_username.grid(row=0, column=1, padx=5, pady=5, sticky="w")
label_email.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_email.grid(row=1, column=1, padx=5, pady=5, sticky="w")
save_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main event loop for the main Tkinter window
root.mainloop()
