import tkinter as tk
from checkers_logic1 import CheckersLogic
from gui import CheckersApp

root = tk.Tk()
root.title("Checkers Application")


logic = CheckersLogic()
app = CheckersApp(root, logic)

root.mainloop()