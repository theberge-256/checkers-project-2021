import tkinter as tk

class CheckersApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


root = tk.Tk()
root.title("Checkers Application")

app = CheckersApp(root)

root.mainloop()