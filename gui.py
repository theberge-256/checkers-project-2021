import tkinter as tk
import checkers_logic1
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
        self.img = tk.PhotoImage(file = "Red Checker.png")
        self.img2 = tk.PhotoImage(file = "Black Checker.png")
        #self.img2 = self.img2.zoom(3)
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
        color = 'black'
        if (x + y) % 2 +1 == 1:
            color = 'red'


        cell = tk.Button(self,
            highlightbackground=color,
            bg=color,
            width=6,
            command = lambda :self.button_clicked(x, y),
            height=3)
        #Too make it so that the checkers image doesn't show a white background always,
        #you need to crop it to be a circle. However, VS code doesn't seem to support pure
        #circle shapes.
        #counter = 0
        #if counter = 0:
        self.piecelist = {}
        self.locationlist = {}

        if x % 2 == ((y)%2):
            if y < 3: 
                cell = tk.Button(self,
                    width=50, 
                    image = self.img, 
                    command = lambda :self.button_clicked(x, y),
                    height=50)

            elif y > 4:
                cell = tk.Button(self,
                    width=50, 
                    image = self.img2, 
                    command = lambda :self.button_clicked(x, y),
                    height=50)
        
        cell.grid(row=self.padding + y,
                  column=self.padding + x)
                  

   
    def update_board(self):
        pass


    def button_clicked(self, x, y):
        print('Clicked piece %d, %d' % (x, y))
        self.piecelist[x] = y
        print(self.piecelist)


root = tk.Tk()
root.title("Checkers Application")

# app = CheckersApp(root, controller_thing)
app = CheckersApp(root, False)

root.mainloop()