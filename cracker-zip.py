#https://github.com/amir-kali-linux
import tkinter as tk
from tkinter import filedialog, messagebox
from zipfile import ZipFile
from datetime import datetime

class ZipCracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Zip File Cracker")

        self.zip_file = ""
        self.password_list = ""

        tk.Label(root, text="Zip File:").pack(pady=5)
        self.zip_entry = tk.Entry(root, width=50)
        self.zip_entry.pack(pady=5)

        tk.Button(root, text="Browse", command=self.browse_zip).pack(pady=5)

        tk.Label(root, text="Password List:").pack(pady=5)
        self.pass_entry = tk.Entry(root, width=50)
        self.pass_entry.pack(pady=5)

        tk.Button(root, text="Browse", command=self.browse_passlist).pack(pady=5)

        tk.Button(root, text="Start Cracking", command=self.start_cracking).pack(pady=20)

    def browse_zip(self):
        self.zip_file = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
        self.zip_entry.insert(0, self.zip_file)

    def browse_passlist(self):
        self.password_list = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.pass_entry.insert(0, self.password_list)

    def start_cracking(self):
        if not self.zip_file or not self.password_list:
            messagebox.showerror("Error", "Pleass select both zip file and password list.")
            return

        zf = ZipFile(self.zip_file)
        tests = 0
        start_time = datetime.now()

        with open(self.password_list) as f:
            for password in f:
                password = password.strip()
                tests += 1
                try:
                    zf.extractall(pwd=password.encode())
                    end_time = datetime.now()
                    duration = end_time - start_time
                    messagebox.showinfo("Success", f"password found: {password}\nTests: {tests}\nDuration: {duration.total_seconds()} secode")
                    break
                except:
                    continue

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipCracker(root)
    root.mainloop()