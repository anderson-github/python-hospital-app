import tkinter as tk
from tkinter import messagebox, simpledialog


class HospitalApp:
    """
    Class to create, delete and update used in the database
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Application")
        self.root.config(bg="gray")

        self.users = {}  # Dictionary to store users

        self.label = tk.Label(root, text="Hospital Application")
        self.label.pack(pady=10)

        self.register_button = tk.Button(root, text="Register User", command=self.register_user)
        self.register_button.pack(pady=5)
        self.register_button.config(bg="CadetBlue", foreground="white", cursor="hand2", relief="flat", width=100)

        self.modify_button = tk.Button(root, text="Modify User", command=self.modify_user)
        self.modify_button.pack(pady=5)
        self.modify_button.config(cursor="hand2", relief="flat", width=100)

        self.delete_button = tk.Button(root, text="Delete User", command=self.delete_user)
        self.delete_button.pack(pady=5)
        self.delete_button.config(cursor="hand2", relief="flat", width=100)

        self.list_button = tk.Button(root, text="List Users", command=self.list_users)
        self.list_button.pack(pady=5)
        self.list_button.config(cursor="hand2", relief="flat", width=100)

    def register_user(self):
        username = simpledialog.askstring("Input", " username:")
        if not username:
            return
        if username in self.users:
            messagebox.showerror("Error", "User already exists.")
            return
        
        password = simpledialog.askstring("Input", "Enter password:", show='*')
        if not password:
            return
        
        name = simpledialog.askstring("Input", "Enter full name:")
        if not name:
            return
        
        age = simpledialog.askstring("Input", "Enter age:")
        if not age:
            return
        
        address = simpledialog.askstring("Input", "Enter address:")
        if not address:
            return
        
        phone = simpledialog.askstring("Input", "Enter phone number:")
        if not phone:
            return
        
        self.users[username] = {
            'password': password,
            'name': name,
            'age': age,
            'address': address,
            'phone': phone
        }
        messagebox.showinfo("Success", f"User {username} registered successfully.")

    def modify_user(self):
        username = simpledialog.askstring("Input", "Enter username to modify:")
        if not username:
            return
        if username not in self.users:
            messagebox.showerror("Error", "User does not exist.")
            return

        password = simpledialog.askstring("Input", "Enter new password:", show='*')
        if not password:
            return
        name = simpledialog.askstring("Input", "Enter new full name:")
        if not name:
            return
        age = simpledialog.askstring("Input", "Enter new age:")
        if not age:
            return
        address = simpledialog.askstring("Input", "Enter new address:")
        if not address:
            return
        phone = simpledialog.askstring("Input", "Enter new phone number:")
        if not phone:
            return

        self.users[username] = {
            'password': password,
            'name': name,
            'age': age,
            'address': address,
            'phone': phone
        }
        messagebox.showinfo("Success", f"User {username} modified successfully.")

    def delete_user(self):
        username = simpledialog.askstring("Input", "Enter username to delete:")
        if not username:
            return
        if username not in self.users:
            messagebox.showerror("Error", "User does not exist.")
            return
        del self.users[username]
        messagebox.showinfo("Success", f"User {username} deleted successfully.")

    def list_users(self):
        if not self.users:
            messagebox.showinfo("Users", "No users registered.")
        else:
            users_list = "\n".join([f"{username}: {info['name']}" for username, info in self.users.items()])
            messagebox.showinfo("Users", f"Registered users:\n{users_list}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.option_add('*Font', '16')

    app = HospitalApp(root)
    root.mainloop()
