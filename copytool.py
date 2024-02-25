import tkinter as tk
from tkinter import filedialog

class DragDropApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Drag and Drop Demo")
        self.geometry("600x400")

        self.left_frame = tk.Frame(self, width=300, height=400, bg="lightgray")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self, width=300, height=400, bg="lightblue")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.left_label = tk.Label(self.left_frame, text="Drop Files Here", bg="lightgray")
        self.left_label.pack(pady=20)

        self.left_frame.bind("<<Drop>>", self.drop)

        self.select_base_button = tk.Button(self.left_frame, text="Select Base Folder", command=self.select_base_folder)
        self.select_base_button.pack(pady=10)

        self.base_folder_label = tk.Label(self.left_frame, text="", bg="lightgray")
        self.base_folder_label.pack()

        self.copy_button = tk.Button(self.right_frame, text="Copy", command=self.copy_folder_name)
        self.copy_button.pack(pady=20)

        self.select_dest_button = tk.Button(self.right_frame, text="Select Destination Folder", command=self.select_destination_path)
        self.select_dest_button.pack(pady=10)

        self.destination_path_label = tk.Label(self.right_frame, text="", bg="lightblue")
        self.destination_path_label.pack()

        self.base_folder = ""
        self.destination_path = ""

    def drop(self, event):
        self.left_label.config(text="Dropped")
        files = self.tk.splitlist(self.tk.call('::tk::DND::Dnd_Files', 'list', event.data))
        for file in files:
            filename = file.split("/")[-1]  # Extracting filename from the path
            tk.Label(self.left_frame, text=filename).pack()

    def copy_folder_name(self):
        if self.destination_path and self.base_folder:
            print("Copying folder name to destination path:", self.destination_path)
            # Here you can implement the logic to copy folder name to the destination path
        else:
            print("Please select a base folder and destination path.")

    def select_base_folder(self):
        self.base_folder = filedialog.askdirectory()
        self.base_folder_label.config(text="Base Folder: " + self.base_folder)

    def select_destination_path(self):
        self.destination_path = filedialog.askdirectory()
        self.destination_path_label.config(text="Destination Path: " + self.destination_path)

if __name__ == "__main__":
    app = DragDropApp()
    app.mainloop()