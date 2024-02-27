import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
import openpyxl

class DragDropApp:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        self.root.title("Drag and Drop Demo")
        self.root.geometry("600x400")

        self.left_frame = tk.Frame(self.root, width=300, height=400, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self.root, width=300, height=400, bg="lightblue")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.left_label = tk.Label(self.left_frame, text="Drop Files Here", bg="lightgray")
        self.left_label.pack(pady=10)

        self.listbox = tk.Listbox(self.left_frame)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.select_base_button = tk.Button(self.left_frame, text="Select Base Folder", command=self.select_base_folder)
        self.select_base_button.pack(pady=10)

        self.base_folder_label = tk.Label(self.left_frame, text="", bg="lightgray")
        self.base_folder_label.pack()

        self.copy_button = tk.Button(self.left_frame, text="Copy Selected", command=self.copy_selected)
        self.copy_button.pack(pady=10)

        self.paste_button = tk.Button(self.left_frame, text="Paste", command=self.paste_items)
        self.paste_button.pack(pady=10)

        # Bind drop event to handle files dropped onto the left frame's listbox
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind('<<Drop>>', self.drop)

        self.copy_items = []  # List to store copied items

        self.copy_button.config(state=tk.DISABLED)  # Initially disable copy button
        self.paste_button.config(state=tk.DISABLED)  # Initially disable paste button

        self.base_folder = ""

    def drop(self, event):
        self.left_label.config(text="Dropped")
        file_paths = event.data.split()  # Get dropped file paths
        for file_path in file_paths:
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                wb = openpyxl.load_workbook(file_path)
                sheet = wb.active
                for row in sheet.iter_rows():
                    for cell in row:
                        self.listbox.insert(tk.END, cell.value)
            else:
                print("Unsupported file format")

    def copy_selected(self):
        self.copy_items = [self.listbox.get(idx) for idx in self.listbox.curselection()]
        self.copy_button.config(state=tk.DISABLED)
        self.paste_button.config(state=tk.NORMAL)

    def paste_items(self):
        for item in self.copy_items:
            self.listbox.insert(tk.END, item)
        self.paste_button.config(state=tk.DISABLED)

    def select_base_folder(self):
        self.base_folder = filedialog.askdirectory()
        self.base_folder_label.config(text="Base Folder: " + self.base_folder)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DragDropApp()
    app.run()