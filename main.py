import tkinter as tk
from tkinter import messagebox
import re

def load_common_passwords(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f)

def check_password_strength(password):
    # Criteria
    min_length = 12
    
    # Check common password
    common_passwords = load_common_passwords('commonPasswords.txt')
    if password in common_passwords:
        return "Weak: Password is too common."
    
    if len(password) < min_length:
        return f"Weak: Password must be at least {min_length} characters long."
    
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not re.search(r"[a-z]", password):
        return "Weak: Password must include at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Weak: Password must include at least one number."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must include at least one special character."
    
    return "Strong: Password meets all the criteria."

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def on_check(event=None):
    password = password_entry.get()
    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", strength)
    
    # Clear the entry field after checking strength
    password_entry.delete(0, tk.END)

def clear_password_field(event):
    if event.keysym == 'BackSpace' and event.state & 0x4:
        password_entry.delete(0, tk.END)
        
def close_application(event=None):
    root.destroy()

if __name__ == "__main__":
    show_password = False

    root = tk.Tk()
    root.title("Password Strength Checker")
    
    label = tk.Label(root, text="Enter Password: ")
    label.pack(pady=10)
    
    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=5)
    password_entry.focus_set()
    
    show_password_checkbox = tk.Checkbutton(root, text="Show Password", command=toggle_password_visibility)
    show_password_checkbox.pack(pady=5)
    
    button = tk.Button(root, text="Check Strength", command=on_check)
    button.pack(pady=20)
    
    root.bind('<Return>', on_check)
    root.bind('<Key>', clear_password_field)
    root.bind('<Escape>', close_application)
    
    root.mainloop()
