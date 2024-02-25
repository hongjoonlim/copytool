import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

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

        self.text_widget = tk.Text(self.left_frame, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Bind drop event to handle files dropped onto the application
        self.text_widget.drop_target_register(DND_FILES)
        self.text_widget.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
    # Get the dropped file paths
        file_paths = event.data.split()
        # Display all dropped file paths in the text widget
        if file_paths:
            self.text_widget.delete(1.0, tk.END)
            for file_path in file_paths:
                self.text_widget.insert(tk.END, file_path + '\n')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DragDropApp()
    app.run()