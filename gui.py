import tkinter as tk
# import controller thing from gui_code.py
class CheckersApp(tk.Frame):
    def __init__(self, master, controller_thing):
        super().__init__(master)

        self.controller_thing = controller_thing

        self.draw_gui()
    
    def draw_gui(self):
        self.grid()
        return



root = tk.Tk()
root.title("Checkers Application")

# app = CheckersApp(root, controller_thing)
app = CheckersApp(root, False)

root.mainloop()