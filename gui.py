import tkinter as tk
# import controller thing from gui_code.py
class CheckersApp(tk.Frame):
    """
        controller_thing will come from gui_code.py
        and will be the middle man between the gui and
        the functionality
    """
    def __init__(self, master, controller_thing):
        super(CheckersApp, self).__init__(master)

        # self.controller_thing = controller_thing
        self.padding = 3

        self.render()
    
    def render(self):
        self.grid() # unusual freeze here
        # self.build_gui()
        self.build_board()

    def build_gui(self):
        """
        This will have checkers counts, and any sort of stats plus labels like Player 1 and 2
        """
        return
    
    def build_board(self):
        """
        (WIP) Preliminary checkers board
        """
        for x in range(8):
            for y in range(8):
                self.build_cell(x, y)
        return

    def build_cell(self, x, y):
        # determine color by x and y
        color = 'black'
        if (x + y) % 2 == 1:
            color = 'white'
        
        cell = tk.Button(self,
            text=color,
            bg=color,
            width=10)

        cell.grid(row=self.padding + y,
                  column=self.padding + x,
                  columnspan=5,
                  sticky=tk.NSEW)




root = tk.Tk()
root.title("Checkers Application")

# app = CheckersApp(root, controller_thing)
app = CheckersApp(root, False)

root.mainloop()