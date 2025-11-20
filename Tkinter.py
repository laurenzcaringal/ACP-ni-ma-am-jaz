#-----------LOGIN --------------

import tkinter as tk
from tkinter import messagebox

users = {}

def open_register():
    login_window.destroy()
    register_window()

def open_login():
    reg_window.destroy()
    login_page()

def login_page():
    global login_window
    login_window = tk.Tk()
    login_window.title("Login Form")
    login_window.geometry("350x250")
    login_window.config(bg="lightblue")

    tk.Label(login_window, text="User Login", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)
    tk.Label(login_window, text="Username:", bg="lightblue", font=("Arial", 12)).pack()
    username_entry = tk.Entry(login_window, width=30)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:", bg="lightblue", font=("Arial", 12)).pack()
    password_entry = tk.Entry(login_window, show="*", width=30)
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        if username in users and users[username] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        elif username == "" or password == "":
            messagebox.showwarning("Input Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    tk.Button(login_window, text="Login", command=login, bg="green", fg="white", width=10).pack(pady=10)
    tk.Button(login_window, text="Register", command=open_register, bg="blue", fg="white", width=10).pack()
    tk.Button(login_window, text="Exit", command=login_window.destroy, bg="red", fg="white", width=10).pack(pady=5)

    login_window.mainloop()


def register_window():
    global reg_window
    reg_window = tk.Tk()
    reg_window.title("Register Account")
    reg_window.geometry("350x250")
    reg_window.config(bg="lightyellow")

    tk.Label(reg_window, text="Register New User", font=("Arial", 18, "bold"), bg="lightyellow").pack(pady=10)
    tk.Label(reg_window, text="New Username:", bg="lightyellow", font=("Arial", 12)).pack()
    new_user_entry = tk.Entry(reg_window, width=30)
    new_user_entry.pack(pady=5)

    tk.Label(reg_window, text="New Password:", bg="lightyellow", font=("Arial", 12)).pack()
    new_pass_entry = tk.Entry(reg_window, show="*", width=30)
    new_pass_entry.pack(pady=5)

    def register():
        new_user = new_user_entry.get()
        new_pass = new_pass_entry.get()
        
        if new_user == "" or new_pass == "":
            messagebox.showwarning("Input Error", "Please fill in all fields.")
        elif new_user in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            users[new_user] = new_pass
            messagebox.showinfo("Success", "Account created successfully!")
            reg_window.destroy()
            login_page()

    tk.Button(reg_window, text="Register", command=register, bg="green", fg="white", width=10).pack(pady=10)
    tk.Button(reg_window, text="Back to Login", command=open_login, bg="blue", fg="white", width=12).pack()
    tk.Button(reg_window, text="Exit", command=reg_window.destroy, bg="red", fg="white", width=10).pack(pady=5)

    reg_window.mainloop()

login_page()
tk.tk



#-----------PERSONAL INFORMATION--------------


import tkinter as tk
from tkinter import messagebox, ttk

# Create main window
window = tk.Tk()
window.title("Personal Information Form")
window.geometry("400x500")
window.config(bg="lightblue")

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    country = country_cb.get()
    comment = text_comment.get("1.0", "end-1c")
    
    hobbies = []
    if hobby_reading.get():
        hobbies.append("Reading")
    if hobby_sports.get():
        hobbies.append("Sports")
    if hobby_music.get():
        hobbies.append("Music")
    
    if name == "" or age == "" or gender == "" or country == "":
        messagebox.showwarning("Incomplete Data", "Please fill out all required fields!")
    else:
        info = (
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Gender: {gender}\n"
            f"Hobbies: {', '.join(hobbies)}\n"
            f"Country: {country}\n"
            f"Comment: {comment}"
        )
        messagebox.showinfo("Form Submitted", info)

tk.Label(window, text="Personal Information Form", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

frame = tk.Frame(window, bg="lightblue")
frame.pack(pady=5)

tk.Label(frame, text="Full Name:", bg="lightblue", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=3)

tk.Label(frame, text="Age:", bg="lightblue", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
entry_age = tk.Entry(frame, width=30)
entry_age.grid(row=1, column=1, pady=3)

tk.Label(frame, text="Gender:", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
ge
