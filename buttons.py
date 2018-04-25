import tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.prompt = tk.Label(self, text="hello world")
        self.press1 = tk.Button(self, text="hello ", command=self.create_button)
        self.press2 = tk.Button(self, text="bye ", command=self.create_button)
        self.output = tk.Label(self, text="")
        self.prompt.pack(side="top", fill="x")
        self.output.pack(side="top", fill="x", expand=True)
        self.press1.pack(side="left", pady=20, padx=20)  # button1
        self.press2.pack(side="right", pady=20, padx=20)  # button2

    def create_button(self):
        root.destroy()
        root1 = tk.Tk()
        Example(root1).pack(fill="both", expand=True)
        root1.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
