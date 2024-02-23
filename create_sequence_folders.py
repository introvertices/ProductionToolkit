import os
import tkinter as tk
from tkinter import filedialog

def create_folders():
    try:
        num_folders = int(num_folders_entry.get())
        prefix = prefix_entry.get()
        target_directory = filedialog.askdirectory()

        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        for i in range(1, num_folders + 1):
            folder_name = f"{prefix}{i}"
            folder_path = os.path.join(target_directory, folder_name)
            os.makedirs(folder_path)

        result_label.config(text="Folders created successfully!")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a positive integer.")

# Create the main window
root = tk.Tk()
root.title("Folder Creator")

# Input fields
num_folders_label = tk.Label(root, text="Number of Folders:")
num_folders_entry = tk.Entry(root)

prefix_label = tk.Label(root, text="Folder Prefix:")
prefix_entry = tk.Entry(root)

# Button to create folders
create_button = tk.Button(root, text="Create Folders", command=create_folders)

# Result label
result_label = tk.Label(root, text="")

# Grid layout
num_folders_label.grid(row=0, column=0, padx=10, pady=5)
num_folders_entry.grid(row=0, column=1, padx=10, pady=5)
prefix_label.grid(row=1, column=0, padx=10, pady=5)
prefix_entry.grid(row=1, column=1, padx=10, pady=5)
create_button.grid(row=2, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, columnspan=2, padx=10, pady=5)

root.mainloop()