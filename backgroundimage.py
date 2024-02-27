
"""
import tkinter
from tkinter import PhotoImage
root=tkinter.Tk()#creates an window
root.title("Food Donation Form")
root.geometry("800x1000")
image_path=PhotoImage(file=r"D:\698\project\github files\backgroundimage.png")
bg_image=tkinter.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)
root.mainloop()
"""
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

def clear_entries():
    entry_item_no.delete(0, tk.END)
    entry_item_name.delete(0, tk.END)
    entry_veg.delete(0, tk.END)
    entry_calories.delete(0, tk.END)
    entry_amount_lb.delete(0, tk.END)
    entry_servings.delete(0, tk.END)

def send_email(item_no, item_name, veg_or_vegan_or_non_veg, calories, amount_lb, servings):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your_email@gmail.com"
    smtp_password = "your_email_password"

    sender_email = "your_email@gmail.com"
    recipient_email = "chandasandeep1998@gmail.com"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "New Food Donation Information"

    body = f"""
    Item No: {item_no}
    Item Name: {item_name}
    Veg/Vegan/Non-Veg: {veg_or_vegan_or_non_veg}
    Calories: {calories}
    Amount (lb): {amount_lb}
    Servings: {servings}
    """
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

def save_to_database_and_send_email():
    item_no = entry_item_no.get()
    item_name = entry_item_name.get()
    veg_or_vegan_or_non_veg = entry_veg.get()
    calories = entry_calories.get()
    amount_lb = entry_amount_lb.get()
    servings = entry_servings.get()

    save_to_database()
    send_email(item_no, item_name, veg_or_vegan_or_non_veg, calories, amount_lb, servings)
    clear_entries()

root = tk.Tk()
root.title("Food Donation Form")
root.geometry("800x1000")

create_table()

image_path = PhotoImage(file=r"D:\698\project\github files\backgroundimage.png")
bg_image = tk.Label(root, image=image_path)
bg_image.place(relheight=1, relwidth=1)

label_item_no = ttk.Label(root, text="Item No:")
# ... (rest of the labels and entry widgets remain unchanged)

upload_button = ttk.Button(root, text="Upload", command=save_to_database_and_send_email)

# ... (grid layout remains unchanged)

root.mainloop()
