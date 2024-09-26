import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("OMR Scanner")
#root.geometry("720x900") 

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, padding="20 20 20 20")
frame.grid(row=0, column=0, sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

labels = ["School", "Class", "Subject", "Code"]
options = {
    "School": ["School A", "School B", "School C", "School D"],
    "Class": ["Class 1", "Class 2", "Class 3", "Class 4"],
    "Subject": ["Math", "Science", "English", "History"],
    "Code": ["Code 101", "Code 102", "Code 103", "Code 104"]
}
comboboxes = []

for i, label in enumerate(labels):
    ttk.Label(frame, text=label).grid(row=i, column=0, sticky=tk.E, padx=10, pady=10)
    combobox = ttk.Combobox(frame, values=options[label], width=30)
    combobox.grid(row=i, column=1, padx=10, pady=10)
    comboboxes.append(combobox)

submit_button = ttk.Button(frame, text="Submit")
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

bottom_frame = ttk.Frame(root, padding="20 20 20 20")
bottom_frame.grid(row=1, column=0)

scan_button = ttk.Button(bottom_frame, text="Scan OMR")
scan_button.grid(row=0, column=0, padx=20, pady=20)

upload_button = ttk.Button(bottom_frame, text="Upload Files")
upload_button.grid(row=0, column=1, padx=20, pady=20)

root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w // 2 - size[0] // 2
y = h // 2 - size[1] // 2
root.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

root.mainloop()
