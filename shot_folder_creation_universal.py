import os
import csv
import tkinter as tk
from tkinter import filedialog, simpledialog

def create_folders_from_csv(csv_file_path, output_folder_path, start_row):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for i, row in enumerate(reader, start=1):
            if i >= start_row:
                folder_name = row[0]
                folder_path = os.path.join(output_folder_path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

def select_csv_file():
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return csv_file_path

def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    return output_folder_path

def get_start_row():
    start_row = simpledialog.askinteger("Start Row", "Enter the row number to start creating folders from:", minvalue=1)
    return start_row

def create_folders():
    csv_file_path = select_csv_file()
    if not csv_file_path:
        return

    output_folder_path = select_output_folder()
    if not output_folder_path:
        return

    start_row = get_start_row()
    if not start_row:
        return

    create_folders_from_csv(csv_file_path, output_folder_path, start_row)
    print("Folders created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    create_folders()