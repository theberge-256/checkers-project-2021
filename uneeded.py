from tkinter import *
import gui
import checkers_logic1

class CheckersGui(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.img = PhotoImage(file = "checkers.gif")
        self.create_piece()

    def create_piece(self):
        #if (x + y) % 2 == 1:   
        self.img = PhotoImage(file = "checkers.gif")
        Button(self, text = 'Click Me !', image = self.img).grid()

root = Tk()
root.title("Checkers Gui")

# app = CheckersApp(root, controller_thing)
app = CheckersGui(root)

root.mainloop()
