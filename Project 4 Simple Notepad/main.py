import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button

class SimpleNotepad():
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Dan\'s Notepad")
        self.file_path: str = ""
        # Text Widget
        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        # Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Save Button
        self.save_button: Button = Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT)
        
        # Save To Existing File Button
        self.save_existing_button: Button = Button(self.button_frame, text="Save to Existing File", command=self.save_if_available)
        self.save_existing_button.pack(side=tk.LEFT)

        # Load Button
        self.load_button: Button = Button(self.button_frame, text="Load", command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)

    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(file_path, "w") as file:
            file.write(self.text_area.get(1.0, tk.END))
        print(f"File saved to {file_path}")

    def save_if_available(self) -> None:
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f"File saved to {self.file_path}")

    def load_file(self) -> None:
        self.file_path: str = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(self.file_path, "r") as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)
        print(f"File loaded from {self.file_path}")

    def run(self) -> None:
        self.root.mainloop()

def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root)
    app.run()

if __name__ == "__main__":
    main()