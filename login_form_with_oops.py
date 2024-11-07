import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("300x200")

        tk.Label(root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

root = tk.Tk()
app = LoginForm(root)
root.mainloop()
