
import tkinter as tk
from tkinter import ttk

def encrypt_text(text, rot):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + rot) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + rot) % 26 + ord('a'))
        else:
            result += char
    return result

def on_encrypt():
    clear_text = clear_text_entry.get()
    selected_rot = int(rot_combobox.get())
    encrypted_text = encrypt_text(clear_text, selected_rot)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, encrypted_text)

# Create the main window
root = tk.Tk()
root.title("ROT Encryption")

# Description label
description = ("Welcome to ROT Encryption Tool!\n\n"
               "ROT (Rotate) encryption is a simple letter substitution "
               "cipher that shifts the letters of the alphabet by a certain "
               "amount. In this tool, you can encrypt your text using ROT1 to ROT25."
               "\n\nHow to use this tool:\n"
               "1. Enter the text in the 'Enter Text' field."
               "\n2. Select the desired ROT type from the drop-down menu."
               "\n3. Click the 'Encrypt' button to generate the encrypted text."
               "\n4. The result will be displayed in the 'Encrypted Text' field.")

description_label = tk.Label(root, text=description, wraplength=400, justify=tk.LEFT)
description_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and place widgets
clear_text_label = tk.Label(root, text="Enter Text:")
clear_text_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

clear_text_entry = tk.Entry(root, width=40)
clear_text_entry.grid(row=1, column=1, padx=10, pady=5)

rot_label = tk.Label(root, text="Select ROT Type:")
rot_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

rot_values = [i for i in range(1, 26)]
rot_combobox = ttk.Combobox(root, values=rot_values, state="readonly")
rot_combobox.current(0)
rot_combobox.grid(row=2, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

result_text_label = tk.Label(root, text="Encrypted Text:")
result_text_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

result_text = tk.Text(root, height=5, width=40)
result_text.grid(row=4, column=1, padx=10, pady=5)

# Start the main event loop
root.mainloop()
