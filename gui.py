import tkinter as tk
#from checkers_logic1 import CheckersPiece
#from checkers_logic1 import CheckersLogic
# import controller thing from gui_code.py
class CheckersApp(tk.Frame):
    """
        controller_thing will come from gui_code.py
        and will be the middle man between the gui and
        the functionality
    """
    def __init__(self, master, logic):
        super(CheckersApp, self).__init__(master)

        self.logic = logic
        self.padding = 3
        #Lines 16 and 17 import an image which is eventually used on a button
        self.img = tk.PhotoImage(file = "Red Checker.png")
        self.img2 = tk.PhotoImage(file = "Black Checker.png")
        #These three parameters keep track of which color piece can be moved, where each piece can move too, and also if pieces can move.
        self.round = 1
        self.loop = 0
        self.red = 1
        self.black = 0
        self.render()
        self.logic.setup()
        #self.check_piece()
        

    def render(self):
        self.grid()
        self.build_board()
        self.build_gui()
    def build_gui(self):
        #This label keeps track of which color's turn it is.
        self.label1 = tk.Label(self.master, text="", width = 63, height = 2).grid(row = 1)
        if self.round ==2:
            self.text = tk.StringVar()
            self.text.set("Black's turn")
            self.label1 = tk.Label(self.master, textvariable=self.text, bg = 'red', width = 40, height = 2, font = 'Arial').grid(row = 1)
        if self.round == 1:
            self.text = tk.StringVar()
            self.text.set("Red's turn")
            self.label1 = tk.Label(self.master, textvariable=self.text, bg = 'red', width = 40, height = 2, font = 'Arial').grid(row = 1)


    
    def build_board(self):
        """
        (WIP) Preliminary checkers board
        """
        self.button_list = []
        for x in range(8):
            column = []
            for y in range(8):
                bcell = self.build_cell1(x, y)
                column.append(bcell)
            self.button_list.append(column)
        self.update_board(x, y)

        return

    def build_cell1(self, x, y):
        color = 'black'
        cell1 = tk.Button(self,
                    highlightbackground=color,
                    bg=color,
                    #command = lambda x=x, y=y :self.check_grid(x,y),
                    width=6,
                    height=3)
        if (x + y) % 2 == 1:
            color = 'red'
            cell1 = tk.Button(self,
                    highlightbackground=color,
                    bg=color,
                    width=6,
                    command = lambda x=x, y=y :self.check_grid(x, y),
                    height=3)
        #Lines 77-82 create two lists to store the locations of the clicked piece and clicked space to move
        self.piecelist = []
        self.piecelist.append("x")
        self.piecelist.append('y')
        self.locationlist = []
        self.locationlist.append("x")
        self.locationlist.append("y")


        if (x + y) % 2 == 1:
            if y < 3: 
                cell1 = tk.Button(self,
                    width=50, 
                    image = self.img2, 
                    command = lambda x=x, y=y :self.check_piece(x,y),
                    height=50)

            elif y > 4:
                cell1 = tk.Button(self,
                    width=50, 
                    image = self.img, 
                    command = lambda x=x, y=y :self.check_piece(x,y),
                    height=50)
    
        cell1.grid(row=self.padding + y,
                  column=self.padding + x)
        #self.board = []
        return cell1
    def grid_clicked(self, x, y):
        #All of this code determines whether a certain piece can move and where each color piece can actually move.
        del(self.locationlist[0])
        del(self.locationlist[0])
        self.locationlist.append(x)
        self.locationlist.append(y)
        print("grid_clicked")
        if self.red > self.black:
            if self.round == 1: 
                x1 = self.piecelist[0]
                y1 = self.piecelist[1]
                x2 = self.locationlist[0]
                y2 = self.locationlist[1]
                if (y2 ==y1-1 and x2==x1-1) or (y2 ==y1-1 and x2==x1+1):  
                    while self.loop == 0:
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
                        self.loop =1       
                        self.round =2
                        #print(self.game)
                        #print(CheckersPiece.team)

        if self.red < self.black:
            if self.round == 2:
                x1 = self.piecelist[0]
                y1 = self.piecelist[1]
                x2 = self.locationlist[0]
                y2 = self.locationlist[1]
                if (y2 == y1+1 and x2==x1+1) or (y2==y1+1 and x2==x1-1):  
                    while self.loop == 1:
                        piece = self.button_list[x1][y1]
                        location = self.button_list[x2][y2]
                        piece.grid(row=self.padding + y2,
                        column = self.padding + x2)
                        location.grid(row=self.padding + y1,
                        column=self.padding + x1)
                        self.button_list[x1][y1] = location
                        self.button_list[x2][y2] = piece
                        piece['command'] = lambda x2 = x2, y2 = y2 :self.black_clicked(x2, y2)
                        location['command'] = lambda x1 = x1, y1 = y1 :self.grid_clicked(x1, y1)
                        self.loop =0
                        self.round =1
            
        self.build_gui()
    def button_clicked(self, x, y):
        #This determines certain variables when it's red's turn
        if self.round == 1:
            self.red = 1
            self.black = 0
        if self.round == 2:
            self.red = 1
            self.black = 0

        del(self.piecelist[0])
        del(self.piecelist[0])
        self.piecelist.append(x)
        self.piecelist.append(y)

    def black_clicked(self, x, y):
        #This determines certain variables when it's black's turn
        if self.round == 1:
            self.black = 1 
            self.red = 0
        if self.round ==2:
            self.black = 1
            self.red = 0
        del(self.piecelist[0])
        del(self.piecelist[0])
        self.piecelist.append(x)
        self.piecelist.append(y)
    
    def update_board(self,x,y):
        self.logic.setup()
    
    def check_piece(self, x, y):
        print(x,y)
        if self.logic.color_check(x,y) == 'black':
            print("black")
            if self.round == 1:
                self.black = 1 
                self.red = 0
            if self.round ==2:
               self.black = 1
               self.red = 0
        if self.logic.color_check(x,y) == 'red':
            print("red")
            if self.round == 1:
                self.red = 1
                self.black = 0
            if self.round == 2:
                self.red = 1
                self.black = 0 
        del(self.piecelist[0])
        del(self.piecelist[0])
        self.piecelist.append(x)
        self.piecelist.append(y)
        cell = self.logic.first_get_cell(x,y)
        moves = cell.allowed_moves()
        print(moves)
        #How to use apply_moves
        #moves[x][y].apply_move()
        #print(moves.apply_move())
        self.update_board
        #self.button_clicked(x,y)

    def check_grid(self,x,y):
        print(x,y)
        #print(self.logic.get_cell(x, y, False))
       
        self.update_board
        self.grid_clicked(x,y)
        
#root = tk.Tk()
#root.title("Checkers Application")
#app = CheckersApp(root, False)

#root.mainloop()

#CHANGES MADE:
#PIECES CAN NO LONGER MOVE TO BLACK SQUARES
#PIECES CAN ONLY MOVE DIAGONAL NOW TO ONE SPACE AWAY, NOT TO ANYWHERE ON THE BOARD
#PLAYERS CAN CHOOSE TO MOVE THEIR PIECE BACK FOR ONE TURN IF THEY MISCLICKED, BUT AFTER THAT TURN ENDS THE PIECE CAN NO LONGER MOVE BACK
#TURNS ARE IMPLEMENTED, MEANING RED PIECES CAN MOVE FIRST, THEN BLACK PIECES MOVE.
#THE TURNS RESTRICT WHICH PIECES CAN MOVE DEPENDING ON WHICH TURN IT IS
#IF A SPACE THAT THE PIECE CANNOT BE MOVED TOO IS CLICKED, THE PLAYER CAN SELECT ANOTHER SPOT TO MOVE THAT PIECE TOO



#COMBINE BOTH FILES