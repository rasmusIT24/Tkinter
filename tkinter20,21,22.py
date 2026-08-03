import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess
from tkinter import messagebox

DB = "ROjala.db"


class App:

    def __init__(self, root):
        self.root = root
        root.title("Spordiklubi kasutajad")

        # OTSING
        top = tk.Frame(root)
        top.pack(pady=5)

        tk.Label(top, text="Otsi (eesnimi või perenimi):").pack(side=tk.LEFT)

        self.search_entry = tk.Entry(top)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Otsi", command=self.search).pack(side=tk.LEFT)

        # TABEL + SCROLLBAR
        frame = tk.Frame(root)
        frame.pack()

        cols = ("first_name", "last_name", "email", "phone", "image")

        self.tree = ttk.Treeview(frame, columns=cols, show="headings", height=12)

        self.tree.heading("first_name", text="Eesnimi")
        self.tree.heading("last_name", text="Perenimi")
        self.tree.heading("email", text="Email")
        self.tree.heading("phone", text="Telefon")
        self.tree.heading("image", text="Pilt")

        for c in cols:
            self.tree.column(c, width=120)

        self.tree.pack(side=tk.LEFT)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # NUPUD
        tk.Button(root, text="Lisa uus kasutaja", command=self.open_form).pack(pady=5)
        tk.Button(root, text="Kustuta valitud kasutaja", command=self.delete_user).pack()
        tk.Button(root, text="Muuda valitud kasutajat", command=self.edit_user).pack()

        self.load_data()
    #Kasutaja muutmine
    def edit_user(self):

        selected = self.tree.focus()

        if not selected:
            messagebox.showwarning("Hoiatus", "Vali kõigepealt rida!")
            return

        values = self.tree.item(selected, "values")

        self.edit_window = tk.Toplevel()
        self.edit_window.title("Muuda kasutajat")

        labels = ["Eesnimi", "Perenimi", "Email", "Telefon", "Pilt"]
        self.entries = []

        for i, label in enumerate(labels):
            tk.Label(self.edit_window, text=label).grid(row=i, column=0)

            entry = tk.Entry(self.edit_window)
            entry.grid(row=i, column=1)
            entry.insert(0, values[i])

            self.entries.append(entry)

        tk.Button(self.edit_window, text="Salvesta muudatused",
                command=lambda: self.update_user(values[2])).grid(row=6, columnspan=2)

    def update_user(self, old_email):

        try:
            conn = self.connect()
            cur = conn.cursor()

            cur.execute("""
                UPDATE users
                SET first_name=?, last_name=?, email=?, phone=?, image=?
                WHERE email=?
            """, (
                self.entries[0].get(),
                self.entries[1].get(),
                self.entries[2].get(),
                self.entries[3].get(),
                self.entries[4].get(),
                old_email
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Edu", "Andmed edukalt muudetud!")

            self.edit_window.destroy()
            self.load_data()

        except:
            messagebox.showerror("Viga", "Andmete muutmine ebaõnnestus!")

        self.load_data()
    #Kasutaja kustutamine
    def delete_user(self):

        selected = self.tree.focus()

        if not selected:
            messagebox.showwarning("Hoiatus", "Vali kõigepealt rida!")
            return

        values = self.tree.item(selected, "values")
        email = values[2]   # kasutame emaili identifikaatorina

        confirm = messagebox.askyesno("Kinnitus", "Kas oled kindel, et soovid kustutada?")

        if not confirm:
            return

        try:
            conn = self.connect()
            cur = conn.cursor()

            cur.execute("DELETE FROM users WHERE email=?", (email,))

            conn.commit()
            conn.close()

            messagebox.showinfo("Edu", "Kasutaja kustutatud!")

            self.load_data()

        except:
            messagebox.showerror("Viga", "Kustutamine ebaõnnestus!")


    def connect(self):
        return sqlite3.connect(DB)

    def load_data(self, search=""):

        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = self.connect()
        cur = conn.cursor()

        if search:
            cur.execute("""
                SELECT first_name, last_name, email, phone, image
                FROM users
                WHERE first_name LIKE ? OR last_name LIKE ?
            """, ('%' + search + '%', '%' + search + '%'))
        else:
            cur.execute("SELECT first_name, last_name, email, phone, image FROM users")

        for row in cur.fetchall():
            self.tree.insert("", tk.END, values=row)

        conn.close()

    def search(self):
        self.load_data(self.search_entry.get())

    def open_form(self):
        subprocess.Popen(["python", "tkinter19.py"])


root = tk.Tk()
root.geometry("850x550")
App(root)
root.mainloop()