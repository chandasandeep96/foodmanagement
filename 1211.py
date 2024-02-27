import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        # Variables to store input values
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.user_type_var = tk.StringVar(value="User")

        # Create widgets
        tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.username_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.password_var, show="*").grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="User Type:").grid(row=2, column=0, padx=10, pady=10)
        tk.OptionMenu(root, self.user_type_var, "Admin", "Manager", "User").grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Sign In", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Sign Up", command=self.sign_up).grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Forgot Email", command=self.forgot_email).grid(row=5, column=0, columnspan=2, pady=10)

    def login(self):
        # Dummy authentication, replace this with your authentication logic
        username = self.username_var.get()
        password = self.password_var.get()
        user_type = self.user_type_var.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "Username and password are required!")
        else:
            # Replace this block with actual authentication logic
            if user_type == "Admin":
                if username == "admin" and password == "adminpass":
                    messagebox.showinfo("Success", f"Welcome, {user_type}!")
                else:
                    messagebox.showerror("Error", "Invalid credentials!")
            elif user_type == "Manager":
                # Add manager authentication logic here
                pass
            elif user_type == "User":
                # Add user authentication logic here
                pass

    def sign_up(self):
        messagebox.showinfo("Sign Up", "Sign up feature coming soon!")

    def forgot_email(self):
        messagebox.showinfo("Forgot Email", "Forgot email feature coming soon!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
    