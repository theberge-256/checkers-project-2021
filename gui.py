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
        self.grid()
        self.build_gui()
        self.build_board()

    def build_gui(self):
        """
        This will have checkers counts, and any sort of stats plus labels like Player 1 and 2
        """
        pass
    
    def build_board(self):
        """
        (WIP) Preliminary checkers board
        """
        for x in range(8):
            for y in range(8):
                self.build_cell(x, y)
        
        self.update_board()

        return

    def build_cell(self, x, y):
        # determine color by x and y
        color = 'black'
        if (x + y) % 2 == 1:
            color = 'white'
        
        cell = tk.Button(self,
            highlightbackground=color,
            bg=color,
            # text='%d,%d' % (x, y),
            width=6,
            command = lambda :self.button_clicked(x, y),
            height=3)

        cell.grid(row=self.padding + y,
                  column=self.padding + x)
   
    def update_board(self):
        """
        Goes through game board data and updates the gui respectively
        """
        pass



    def button_clicked(self, x, y):
        print('Clicked piece %d, %d' % (x, y))



root = tk.Tk()
root.title("Checkers Application")

# app = CheckersApp(root, controller_thing)
app = CheckersApp(root, False)

root.mainloop()