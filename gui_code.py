import tkinter
# import gui

class CheckersGui(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_grid()
    def set_coords(self):
        #The coordinates need to assign a particular button, like button1 to the corresponding number. 
        #Maybe like button[i] = [i] in list
        #However, there also needs to be a way to replace each checkers circle button
        #with the normal grid button. The button moving could work without having to use
        #Math like (move up subtract 8 from i)
        pass
    def choose_peice(self):
        coordinateloc = self.piece1.get()
        #piece1 and piece2 are also placeholders.
    def choose_location(self):
        coordinatemove = self.location1.get()
        #location1 and location2 are placeholders for the actual widgets.
    
    def calculate_movement(self):
        #There needs to be a way to track directional movements with the buttons. The only way I can think of is having a button have like [i] 
        # and every time i is increased by 1, it moves right.
        #Then we could implement the grid or something.
        pass

        
    def create_grid(self):
        grid = []
        #FOR SOME REASON, THE GRID ENDS AT 07 AND STARTS THE NEXT ROW AT 10. IT SKIPS ALL 8 and 9s.
        for row in range(8):

            grid.append([])

            for column in range(8):
                grid_button = tkinter.Button(self, text= str(row) + str(column), command = lambda r=row, c=column :self.button_clicked(r, c))
                grid_button.grid(row=row, column=column)
                grid[row].append(grid_button)
        self.button_grid = grid
        
    def replace_piece(self):
        #while calculate_movement changes the coordinates of a peice, this needs to actively move the
        #checkers peice from one coordinate to another. The way I need to do this is probably by having the coords
        #actually move the circle from one place to another. It would duplicate the circle to another slot,
        #then delete the circle from its original location. 
        pass

    def button_clicked(self, row, column):
        print(str(row) + str(column))
        button = self.button_grid[row][column]
        button['fg'] = 'red'
        pass
root = tkinter.Tk()
root.title("Checkers Application")

# app = CheckersApp(root, controller_thing)
app = CheckersGui(root)

root.mainloop()