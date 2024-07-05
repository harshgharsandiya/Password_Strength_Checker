import tkinter as tk
from tkinter import messagebox
import re
import math
import threading

def calculate_time_to_crack(password, attacker_power, entropy):
    
    # convert entropy to number of possible combinations
    combinations = 2 ** entropy
    
    #Estimate time to crack in seconds
    time_to_crack_seconds = combinations / attacker_power
    
    return time_to_crack_seconds

def calculate_entropy(password):
    #character sets
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    
    character_set = lowercase + uppercase + digits + special
    #total number of possible characters
    C = len(character_set)
    
    #lenght of password
    L = len(password)

    #calculate entropy
    entropy = L * math.log2(C)

    return entropy

def load_common_passwords(file_path):
    with open(file_path, 'r') as f:
        return set(line.strip() for line in f)

def check_password_strength(password):
    # Criteria
    min_length = 12
    
    # Check common password
    if password in common_passwords:
        return "Weak: \nPassword is too common.", 0
    
    if len(password) < min_length:
        return f"Weak: \nPassword must be at least {min_length} characters long.", 0
    
    #Check character types
    strength = []
    
    if re.search(r"[A-Z]", password):
        strength.append("Uppercase")
    
    if re.search(r"[a-z]", password):
        strength.append("Lowercase")

    if re.search(r"\d", password):
        strength.append("Digit")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength.append("Special characters")
        
    #Entropy of password
    entropy = calculate_entropy(password)
    
    #Time to crack in seconds
    time_to_crack_seconds = calculate_time_to_crack(password, 10**4, entropy)
    
    #Time to crack in minutes and seconds
    time_to_crack_minutes = time_to_crack_seconds // 60
            
    #Strenght level
    if len(strength) >= 3 and len(password) >= min_length and entropy >= 60:
        return "Insane", time_to_crack_seconds
    elif len(strength) >= 3 and len(password) >= min_length and entropy >= 40:
        return "Very Strong", time_to_crack_seconds
    elif len(strength) >= 3 and len(password) >= min_length and entropy >= 20:
        return "Strong", time_to_crack_seconds
    elif len(strength) >= 3 and len(password) >= min_length:
        return "Moderate", time_to_crack_seconds
    elif len(strength) >= 2 and len(password) >= min_length:
        return "Weak", time_to_crack_seconds
    else:
        return "Very Weak", time_to_crack_seconds

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def on_check(event=None):
    password = password_entry.get()
    result = check_password_strength(password)
    strength, time_to_crack_seconds = result[0], result[1]
    time_to_crack_hours = time_to_crack_seconds / 3600
    strength_label.config(text=f"Strength: {strength}")
    strength_label.config(text=f"Strength: {strength}\nEstimated Crack Time: {time_to_crack_hours:.2f} hours")

def clear_password_field(event):
    if event.keysym == 'BackSpace' and event.state & 0x4:
        password_entry.delete(0, tk.END)
        
def close_application(event=None):
    root.destroy()
    
def load_passwords_async():
    global common_passwords
    common_passwords = load_common_passwords('commonPasswords.txt')
    messagebox.showinfo("Passwords Strenght Checker", "Common password list loaded succussfully")

def start_load_thread():
    thread = threading.Thread(target=load_passwords_async)
    thread.start()

if __name__ == "__main__":
    show_password = False
    common_passwords = set()

    root = tk.Tk()
    root.title("Real-Time Password Strength Checker")
    
    label = tk.Label(root, text="Enter Password: ")
    label.pack(pady=10)
    
    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=5)
    password_entry.focus_set()
    password_entry.bind('<KeyRelease>', on_check)
    
    show_password_checkbox = tk.Checkbutton(root, text="Show Password", command=toggle_password_visibility)
    show_password_checkbox.pack(pady=5)
    
    strength_label = tk.Label(root, text="Strenght: ")
    strength_label.pack(pady=5)
    
    button = tk.Button(root, text="Check Strength", command=on_check)
    button.pack(pady=20)
    
    root.bind('<Return>', on_check)
    root.bind('<Key>', clear_password_field)
    root.bind('<Escape>', close_application)
    
    #load common passwords asynchronously
    start_load_thread()
    
    root.mainloop()
