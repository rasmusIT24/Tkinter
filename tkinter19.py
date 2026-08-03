#Kasutaja lisamine
#Harjutus 19
#Rasmus Ojala
import tkinter as tk
from tkinter import messagebox
import sqlite3

#Funktsioonid
def validate_data():
    enimi = entries["Eesnimi"].get()
    pnimi = entries["Perenimi"].get()
    email = entries["Email"].get()
    tel = entries["Telefon"].get()
    pilt = entries["Pilt"].get()

    if not enimi:
        tk.messagebox.showerror("Viga", "Eesnimi on kohustuslik!")
        return False
    if not pnimi:
        tk.messagebox.showerror("Viga", "Perenimi on kohustuslik!")
        return False
    if not email:
        tk.messagebox.showerror("Viga", "email on kohustuslik!")
        return False
    if not tel:
        tk.messagebox.showerror("Viga", "Tel on kohustuslik!")
        return False
    if not pilt:
        tk.messagebox.showerror("Viga", "Pilt on kohustuslik!")
        return False
    
    #tk.messagebox.showinfo("Edu", "Andmed on kehtivad")
    return True

#Valideerib andmed ja lisab need andmebaasi
def insert_data():
    if validate_data():
        connection = sqlite3.connect("KPoldmaa.db")
        cursor = connection.cursor()
 
        cursor.execute("""
            INSERT INTO users(first_name, last_name, email, phone, image)
            VALUES (?, ?, ?, ?, ?)
        """, (
            entries["Eesnimi"].get(),
            entries["Perenimi"].get(),
            entries["Email"].get(),
            entries["Telefon"].get(),
            entries["Pilt"].get()
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Kasutaja edukalt loodud!")

# Loo Tkinteri aken
root = tk.Tk()
root.title("Kasutaja Lisamine")

# Loo sildid ja sisestusväljad
labels = ["Eesnimi", "Perenimi", "Email", "Telefon", "Pilt"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

# Loo nupp andmete sisestamiseks
submit_button = tk.Button(root, text="Sisesta kasutaja", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

# Näita Tkinteri akent
root.mainloop()