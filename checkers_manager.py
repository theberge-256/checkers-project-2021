import tkinter as tk
from checkers_logic1 import CheckersPiece
from checkers_logic1 import CheckersLogic
from gui import CheckersApp
#from checkers_logic1 import CheckersApp
class CheckersManager(tk.Frame):
    """
        controller_thing will come from gui_code.py
        and will be the middle man between the gui and
        the functionality
    """
    #def __init__(self,master):
        #super(CheckersManager, self).__init__(master)
        #self.y = y
        #self.
       

    
    #def main(self):
        #self.Cpiece.setup(self)
        #print(self.board)
 
   # def __init__(self, master,):
        #super(CheckersApp, self).__init__(master)
        #self.start_screen()
        
        
    #def start_screen(self):    
        #cell = tk.Button(self,
            #text = "Start?",
            #width=6,
            #command = render(),
            #height = 3).grid(row = 1, column = 1)
#print(Logic.board)
root = tk.Tk()
root.title("Checkers Manager")

logic = CheckersLogic()
app = CheckersApp(root, logic)
root.mainloop()
