import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_table():
    connection = sqlite3.connect('food_items_donation_database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_items (
            id INTEGER PRIMARY KEY,
            item_no TEXT,
            item_name TEXT,
            veg_or_vegan_or_non_veg TEXT,
            calories INTEGER,
            amount_lb float,
            servings INTEGER
        )
    ''')

    connection.commit()
    connection.close()

def save_to_database():
    item_no = entry_item_no.get()
    item_name = entry_item_name.get()
    veg_or_vegan_or_non_veg = entry_veg.get()
    calories = entry_calories.get()
    amount_lb = entry_amount_lb.get()
    servings = entry_servings.get()

    connection = sqlite3.connect('food_items_donation_database.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO food_items
        (item_no, item_name, veg_or_vegan_or_non_veg, calories, amount_lb, servings)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (item_no, item_name, veg_or_vegan_or_non_veg, calories, amount_lb, servings))

    connection.commit()
    connection.close()

   # clear_entries()

def clear_entries():
    entry_item_no.delete(0, tk.END)
    entry_item_name.delete(0, tk.END)
    entry_veg.delete(0, tk.END)
    entry_calories.delete(0, tk.END)
    entry_amount_lb.delete(0, tk.END)
    entry_servings.delete(0, tk.END)

root = tk.Tk()#creates an window
root.title("Food Donation Form")
root.geometry("800x1000")



# Create Database Table
create_table()



# Background Image
image_path = PhotoImage(file=r"D:\698\project\github files\backgroundimage.png")
bg_image = tk.Label(root, image=image_path)
bg_image.place(relheight=1, relwidth=1)


# Labels
label_item_no = ttk.Label(root, text="Item No:")
label_item_name = ttk.Label(root, text="Item Name:")
label_veg = ttk.Label(root, text="Veg/Vegan/Non-Veg:")
label_calories = ttk.Label(root, text="Calories:")
label_amount_lb = ttk.Label(root, text="Amount (lb):")
label_servings = ttk.Label(root, text="Servings:")

# Entry Widgets
entry_item_no = ttk.Entry(root)
entry_item_name = ttk.Entry(root)
entry_veg = ttk.Entry(root)
entry_calories = ttk.Entry(root)
entry_amount_lb = ttk.Entry(root)
entry_servings = ttk.Entry(root)

# Upload Button
upload_button = ttk.Button(root, text="Upload", command=save_to_database)

# Grid Layout
label_item_no.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_item_no.grid(row=0, column=1, padx=5, pady=5, sticky="w")
label_item_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_item_name.grid(row=1, column=1, padx=5, pady=5, sticky="w")
label_veg.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_veg.grid(row=2, column=1, padx=5, pady=5, sticky="w")
label_calories.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_calories.grid(row=3, column=1, padx=5, pady=5, sticky="w")
label_amount_lb.grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_amount_lb.grid(row=4, column=1, padx=5, pady=5, sticky="w")
label_servings.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entry_servings.grid(row=5, column=1, padx=5, pady=5, sticky="w")
upload_button.grid(row=6, column=0, columnspan=2, pady=10)


# Run the main event loop for the main Tkinter window
root.mainloop()
