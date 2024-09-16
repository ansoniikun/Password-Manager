import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import json
import os

# Function to generate or load the encryption key from a file
def load_or_generate_key():
    if os.path.exists('key.key'):
        # Load the key from a file
        with open('key.key', 'rb') as key_file:
            return key_file.read()
    else:
        # Generate a new key and save it to a file
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        return key

# Function to encrypt a password using the provided key
def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# Function to decrypt an encrypted password using the provided key
def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

# Load passwords from the file if it exists
def load_passwords():
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as file:
            return json.load(file)
    return {}

# Save passwords to the file
def save_passwords():
    with open('passwords.txt', 'w') as file:
        json.dump(passwords, file)

# Load the encryption key
key = load_or_generate_key()

passwords = load_passwords()  # Load existing passwords from file

# Function to add a new password entry for a service
def add_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Ensure all fields are filled before adding the password
    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        save_passwords()  # Save the updated passwords dictionary to the file
        messagebox.showinfo("Success", "Password added successfully!")
    else:
        messagebox.showwarning("Error", "Please fill in all the fields.")

# Function to retrieve and decrypt a password for a given service
def get_password():
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        try:
            decrypted_password = decrypt_password(key, encrypted_password)
            messagebox.showinfo("Password", f"Username: {passwords[service]['username']}\nPassword: {decrypted_password}")
        except Exception as e:
            messagebox.showerror("Error", "Failed to decrypt the password. Invalid key or corrupted data.")
    else:
        messagebox.showwarning("Error", "Password not found.")

# UI Instructions and signature
instructions = '''To add password fill all the fields and press "Add Password"
To view password, enter Account Name and press "Get Password"'''
signature = "Developed by Hlompho Maleke"

# Create main window for the application
window = tk.Tk()
window.title("Password Manager")
window.configure(bg="blue")  # Set background color

window.resizable(False, False)  # Prevent window from being resizable

# Create frame to hold UI elements
center_frame = tk.Frame(window, bg="#d3d3d3")
center_frame.grid(row=0, column=0, padx=10, pady=10)

# Instruction label
instruction_label = tk.Label(center_frame, text=instructions, bg="#d3d3d3")
instruction_label.grid(row=0, column=1, padx=10, pady=5)

# Account (service) input field
service_label = tk.Label(center_frame, text="Account:", bg="#d3d3d3")
service_label.grid(row=1, column=0, padx=10, pady=5)
service_entry = tk.Entry(center_frame)
service_entry.grid(row=1, column=1, padx=10, pady=5)

# Username input field
username_label = tk.Label(center_frame, text="Username:", bg="#d3d3d3")
username_label.grid(row=2, column=0, padx=10, pady=5)
username_entry = tk.Entry(center_frame)
username_entry.grid(row=2, column=1, padx=10, pady=5)

# Password input field
password_label = tk.Label(center_frame, text="Password:", bg="#d3d3d3")
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(center_frame, show="*")  # Mask password input
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Button to add password
add_button = tk.Button(center_frame, text="Add Password", command=add_password, height=1, width=10)
add_button.grid(row=5, column=4, padx=10, pady=5)

# Button to get password
get_button = tk.Button(center_frame, text="Get Password", command=get_password, height=1, width=10)
get_button.grid(row=6, column=4, padx=10, pady=5)

# Signature label
signature_label = tk.Label(center_frame, text=signature, bg="#d3d3d3")
signature_label.grid(row=7, column=1, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()
