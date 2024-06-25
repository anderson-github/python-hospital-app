import tkinter as tk
from tkinter import messagebox
import mysql.connector

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Application")

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital_db"
        )
        self.cursor = self.db_connection.cursor()

        self.label = tk.Label(root, text="Hospital Application")
        self.label.pack(pady=10)

        self.list_buttons = {}

        tables = ['administrativos', 'departamentos', 'trabajadores', 'usuarios']
        for table in tables:
            self.list_buttons[table] = tk.Button(root, text=f"List {table.capitalize()}", command=lambda t=table: self.list_data(t))
            self.list_buttons[table].pack(pady=5)

    def list_data(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        records = self.cursor.fetchall()
        if not records:
            messagebox.showinfo("Data", f"No data in {table}.")
        else:
            records_list = "\n".join([str(record) for record in records])
            messagebox.showinfo("Data", f"{table.capitalize()} data:\n{records_list}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hospital Application")
    root.geometry("400x600")
    root.option_add('*Font', '14')

    app = HospitalApp(root)
    root.mainloop()
