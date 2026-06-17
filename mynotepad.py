import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Lightweight Notepad")
        self.root.geometry("800x600")

        # 1. Create the Text Area (No formatting, just plain text)
        self.text_area = tk.Text(self.root, undo=True, font=("Consolas", 11))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # 2. Add a Scrollbar
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        # 3. Create a Simple Menu
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.root.config(menu=self.menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
            self.root.title(f"{file_path} - Notepad")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{file_path} - Notepad")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = SimpleNotepad(root)
    root.mainloop()