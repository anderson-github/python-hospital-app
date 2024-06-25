import tkinter as tk
from tkinter import simpledialog, messagebox
import mysql.connector

class HospitalApp:
    """
    Clase para eliminar registros en la base de datos del hospital
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Application")

        self.label = tk.Label(root, text="Eliminar Registros")
        self.label.pack(pady=10)

        self.delete_button = tk.Button(root, text="Eliminar", command=self.select_delete_option)
        self.delete_button.pack(pady=5)

        self.db_connection = self.connect_db()
        self.cursor = self.db_connection.cursor()

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital_db"
        )

    def select_delete_option(self):
        options = ["departamentos", "administrativos", "trabajadores", "usuarios"]
        option = simpledialog.askstring("Eliminar Registro", f"Seleccione el tipo de registro a eliminar:\n{', '.join(options)}")

        if option is None:
            return  # Salir si se cancela o se cierra la ventana de diálogo
        
        if option not in options:
            messagebox.showerror("Error", "Opción no válida.")
            return

        self.delete_record(option)

    def delete_record(self, table):
        id_column = f"id_{table[:-1]}"
        record_id = simpledialog.askinteger("Eliminar Registro", f"Ingrese el ID del {table[:-1]} a eliminar:")

        if record_id is None:
            return  # Si se cancela o se cierra la ventana, salir sin hacer nada

        select_query = f"SELECT * FROM {table} WHERE {id_column} = %s"
        self.cursor.execute(select_query, (record_id,))
        record = self.cursor.fetchone()

        if not record:
            messagebox.showerror("Error", f"El ID de {table[:-1].capitalize()} no existe.")
            return

        delete_query = f"DELETE FROM {table} WHERE {id_column} = %s"
        self.cursor.execute(delete_query, (record_id,))
        self.db_connection.commit()
        messagebox.showinfo("Éxito", f"ID de {table[:-1].capitalize()} {record_id} eliminado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    root.option_add('*Font', '16')

    app = HospitalApp(root)
    root.mainloop()
