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
        self.counter = 0
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
        self.button_list = []
        for x in range(8):
            column = []
            for y in range(8):
                bcell = self.build_cell(x, y)
                column.append(bcell)
            self.button_list.append(column)
        self.update_board()

        return

    def build_cell(self, x, y):
        color = 'black'
        if (x + y) % 2 +1 == 1:
            color = 'red'
        self.piecelist = []
        self.piecelist.append("x")
        self.piecelist.append('y')
        self.locationlist = []
        self.locationlist.append("x")
        self.locationlist.append("y")




        cell = tk.Button(self,
            highlightbackground=color,
            bg=color,
            width=6,
            command = lambda x=x, y=y :self.grid_clicked(x, y),
            height=3)


        if x % 2 == ((y)%2):
            if y < 3: 
                cell = tk.Button(self,
                    width=50, 
                    image = self.img, 
                    command = lambda x=x, y=y :self.button_clicked(x, y),
                    height=50)
            
            elif y > 4:
                cell = tk.Button(self,
                    width=50, 
                    image = self.img2, 
                    command = lambda x=x, y=y :self.button_clicked(x, y),
                    height=50)
        
        cell.grid(row=self.padding + y,
                  column=self.padding + x)
        self.board=[]
        
        return cell
   
    def update_board(self):
        pass
    def move_piece(self, x, y):
        pass

    def grid_clicked(self, x, y):
        print('Clicked piece %d, %d' % (x, y))
        del(self.locationlist[0])
        del(self.locationlist[0])
        self.locationlist.append(x)
        self.locationlist.append(y)
        print(self.locationlist)
        if self.counter > 0:
            self.counter +=1
        
            if self.counter == 2:
                x1 = self.piecelist[0]
                y1 = self.piecelist[1]
                x2 = self.locationlist[0]
                y2 = self.locationlist[1]
                piece = self.button_list[x1][y1]
                location = self.button_list[x2][y2]
                piece.grid(row=self.padding + y2,
                column = self.padding + x2)
                location.grid(row=self.padding + y1,
                column=self.padding + x1)
                self.button_list[x1][y1] = location
                self.button_list[x2][y2] = piece
                piece['command'] = lambda x2 = x2, y2 = y2 :self.button_clicked(x2, y2)
                location['command'] = lambda x1 = x1, y1 = y1 :self.grid_clicked(x1, y1)
                self.counter = 0
    
    def button_clicked(self, x, y):
        print('Clicked piece %d, %d' % (x, y))
        if self.counter == 0:
            self.counter +=1
            print(self.counter)
        del(self.piecelist[0])
        del(self.piecelist[0])
        self.piecelist.append(x)
        self.piecelist.append(y)
        print(self.piecelist)

root = tk.Tk()
root.title("Checkers Application")

# app = CheckersApp(root, controller_thing)
app = CheckersApp(root, False)

root.mainloop()