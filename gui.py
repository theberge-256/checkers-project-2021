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
        #img is the red checker image
        #img2 is the black checker image
        #img3 is the image for when a piece is destroyed
        self.img = tk.PhotoImage(file = "Red Checker.png")
        self.img2 = tk.PhotoImage(file = "Black Checker.png")
        self.img3 = tk.PhotoImage(file = "red.png")
        self.img4 = tk.PhotoImage(file = "Red Checker King.png")
        self.img5 = tk.PhotoImage(file = "Black Checker King.png")
        #These three parameters keep track of which color piece can be moved, where each piece can move too, and also if pieces can move.
        #Self.round keeps track of the turn systenm round 1 is red's turn, round 2 is black's turn
        #self.loop ensures the movement will loop until it finishes.
        #self.red is just another verification combined with the self.round
        #same with self.black
        #self.move is in charge of jumping + double jumping
        #self.red_counter and black_counter are the win conditions. They are tracked whenever a piece jumps and kills the opposing piece.
        #Self.double_counter is a way to track infinite jumping
        #self.loop_counter it a way to track how many jumps are applied.
        self.round = 1
        self.loop = 0
        self.red = 1
        self.black = 0
        self.move = 0
        self.red_counter = 12
        self.black_counter = 12
        self.double_counter = 0
        self.loop_counter = 0
        self.loop_counter2 = 0
        self.render()
        self.logic.setup()

        #self.check_piece()
        

    def render(self):
        self.grid()
        self.build_board()
        self.build_gui()
    def build_gui(self):
        #This label keeps track of which color's turn it is.
        self.round_label = tk.Label(self.master, text="", width = 63, height = 2).grid(row = 1)
        if self.round ==2:
            self.text = tk.StringVar()
            self.text.set("Black's turn")
            self.round_label = tk.Label(self.master, textvariable=self.text, bg = 'red', width = 40, height = 2, font = 'Arial').grid(row = 1)
        if self.round == 1:
            self.text = tk.StringVar()
            self.text.set("Red's turn")
            self.round_label = tk.Label(self.master, textvariable=self.text, bg = 'red', width = 40, height = 2, font = 'Arial').grid(row = 1)
        if self.red_counter == 0:
            self.text = tk.StringVar()
            self.text.set("BLACK WINS!!!!")
            self.round_label = tk.Label(self.master, textvariable=self.text, bg = 'blue', width = 40, height = 2, font = 'Arial').grid(row = 1)
            print("black wins!!")
        if self.black_counter == 0:
            self.text = tk.StringVar()
            self.text.set("RED WINS!!!!")
            self.round_label = tk.Label(self.master, textvariable=self.text, bg = 'blue', width = 40, height = 2, font = 'Arial').grid(row = 1)
            print("red wins!!!")
    
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
        #self.update_board(x, y)

        return

    def build_cell1(self, x, y):
        #color = 'black'
        cell1 = tk.Button(self,
                    highlightbackground='black',
                    bg='black',
                    #command = lambda x=x, y=y :self.check_grid(x,y),
                    width=6,
                    height=3)
        if (x + y) % 2 == 1:
            #color = 'red'
            cell1 = tk.Button(self,
                    highlightbackground='red',
                    bg='red',
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
                    bg = 'gray1', 
                    image = self.img2, 
                    command = lambda x=x, y=y :self.check_piece(x,y),
                    height=50)

            elif y > 4:
                cell1 = tk.Button(self,
                    width=50, 
                    bg = 'red2',
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
        x1 = self.piecelist[0]
        y1 = self.piecelist[1]
        x2 = self.locationlist[0]
        y2 = self.locationlist[1]
        current_location = self.button_list[x1][y1]
        a = x1-1
        b = y1-1
        c = x1+1
        e = y1+1
        a2 = x2-1
        b2 = y2-1
        c2 = x2+1
        e2 = y2+1
        a3 = x2-2
        b3 = y2-2
        c3 = x2+2
        e3 = y2+2
        if x2 > 1 and y2 > 1:
            pieceone = self.button_list[a2][b2]
            second_pieceone = self.button_list[a3][b3]
        if x2 < 6 and y2 > 1:
            piecetwo = self.button_list[c2][b2]
            second_piecetwo = self.button_list[c3][b3]
        if x2 > 1 and y2 < 6:
            piecethree = self.button_list[a2][e2]
            second_piecethree = self.button_list[a3][e3]
        if x2 < 6 and y2 < 6:
            piecefour = self.button_list[c2][e2]
            second_piecefour = self.button_list[c3][e3]
        
        
     


        if self.red > self.black:
            self.loop = 0
            #self.double_counter = 0
            if self.round == 1: 
                #add these variables for when you click a piece, it displays all possible moves.
                if self.loop_counter == 1:
                    self.loop_counter = 0
                    self.double_counter = 1
                if x1 != 0:
                    piece1 = self.button_list[a][b] #in charge of left-way movement 
                    if piece1.cget('bg') == 'gray1' or piece1.cget('bg') == 'yellow1':
                        if (y2 ==y1-2 and x2==x1-2):
                            self.move = 2
                    if piece1.cget('bg') == 'red' or 'black':
                        if (y2 ==y1-1 and x2==x1-1):
                            self.move = 1
                if x1 !=7:
                    piece2 = self.button_list[c][b] #in charge of right-way movement
                    if piece2.cget('bg') == 'gray1'or piece2.cget('bg') == 'yellow1':
                        if (y2 ==y1-2 and x2==x1+2):
                            self.move = 2
                    if piece2.cget('bg') == 'red' or 'black':
                        if (y2 ==y1-1 and x2==x1+1):
                            self.move = 1
                
                if current_location['bg'] == 'yellow':
                    
                    if x1 < 6 and y1 <6:
                        piece1 = self.button_list[a][e] 
                        if piece1.cget('bg') == 'gray1' or piece1.cget('bg') == 'yellow1':
                            if (y2 == y1+2 and x2==x1+2):
                                self.move = 2
                    if x1 != 7 and y1 != 7:
                        piece1 = self.button_list[a][e]     
                        if piece1.cget('bg') == 'red' or 'black':
                            if (y2 == y1+1 and x2==x1+1):
                                self.move = 1
                    if x1 > 1 and y1 <6:
                        piece2 = self.button_list[c][e]
                        if piece2.cget('bg') == 'gray1' or piece2.cget('bg') == 'yellow1':
                            if (y2==y1+2 and x2==x1-2):
                                self.move = 2
                    if x1 != 0 and y1 != 7:
                        piece2 = self.button_list[c][e]
                        if piece2.cget('bg') == 'red' or 'black':
                                if (y2==y1+1 and x2==x1-1):
                                    self.move = 1
                        

                if self.double_counter == 1 or current_location['bg'] == 'yellow':
                    if x1 != 0:
                        piece = self.button_list[a][b]
                        if piece.cget('bg') == 'gray1' or piece.cget('bg') == 'yellow1':
                            if (y2 ==y1-2 and x2==x1-2):
                                self.move = 2
                    if x1 !=7:
                        piece = self.button_list[c][b]
                        if piece.cget('bg') == 'gray1'or piece.cget('bg') == 'yellow1':
                            if (y2 ==y1-2 and x2==x1+2):
                                self.move = 2
                    if x1 <6 and y1 < 6:
                        piece = self.button_list[c][e]
                        if piece.cget('bg') == 'gray1' or piece.cget('bg') == 'yellow1':
                            if (y2 ==y1+2 and x2==x1+2):
                                self.move =2
                    if x1 != 0:
                        piece = self.button_list[a][e]
                        if piece.cget('bg') == 'gray1' or piece.cget('bg') == 'yellow1':
                            if (y2==y1+2 and x2==x1-2):
                                self.move = 2
                if self.move == 1:
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
                        self.move = 0
                        self.double_counter = 0
                        #print(self.game)
                        #print(CheckersPiece.team)
                if self.move == 2:
                    while self.loop == 0:
                        if x1 != 0: #might encounter problems when jumping further away
                            if (y2 ==y1-2 and x2==x1-2):
                                #self.button_list[a][b] =0
                                piece1 = self.button_list[a][b]
                                piece1['bg'] = 'red'
                                piece1['command'] = lambda a=a,b=b:self.grid_clicked(a,b)
                                piece1['image'] = self.img3#('image')#(self.img2)
                                self.button_list[a][b] = piece1
                        if x1 != 7:
                            if (y2 ==y1-2 and x2==x1+2):
                                piece2 = self.button_list[c][b]
                                piece2['bg'] = 'red'
                                piece2['command'] = lambda c=c,b=b:self.grid_clicked(c,b)
                                piece2['image'] = self.img3#('image')#(self.img2)
                                self.button_list[c][b] = piece2
                        if x1 != 0:
                            if (y2==y1+2 and x2==x1-2):
                                piece3 = self.button_list[a][e]
                                piece3['bg'] = 'red'
                                piece3['command'] = lambda a=a,e=e:self.grid_clicked(a,e)
                                piece3['image'] = self.img3
                                self.button_list[a][e] = piece3

                        if x1 != 7:
                            if (y2==y1+2 and x2 ==x1+2):
                                piece4 = self.button_list[c][e]
                                piece4['bg'] = 'red'
                                piece4['command'] = lambda c=c,e=e:self.grid_clicked(c,e)
                                piece4['image'] = self.img3
                                self.button_list[c][e] = piece4
                        if x2 > 1 and y2 > 1:
                            if pieceone.cget('bg') == 'gray1' or pieceone.cget('bg') == 'yellow1':
                                if second_pieceone.cget('bg') == 'red':
                                    #print("ab works")
                                    self.loop_counter = 1
                        if x2 < 6 and y2 > 1:
                            if piecetwo.cget('bg') == 'gray1' or piecetwo.cget('bg') == 'yellow1':  
                                if second_piecetwo.cget('bg') == 'red':
                                    #print("cb works")
                                    self.loop_counter = 1
                        if x2 > 1 and y2 < 6:
                            if piecethree.cget('bg') == 'gray1'or piecethree.cget('bg') == 'yellow1': 
                                if second_piecethree.cget('bg') == 'red':
                                    #print("ae works")
                                    self.loop_counter = 1
                        if x2 < 6 and y2 < 6:
                            if piecefour.cget('bg') == 'gray1'or piecefour.cget('bg') == 'yellow1': 
                                if second_piecefour.cget('bg') == 'red':
                                    #print("ce works")
                                    self.loop_counter = 1
                        
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
                        self.move = 0
                        self.black_counter -=1
                        self.double_counter = 0
                        if self.loop_counter == 1:
                            self.round = 1
                    self.loop = 0        
                if y2 == 0:
                    print("RED KING RUNS")
                    piece['image'] = self.img4    
                    piece['bg'] = 'yellow'       
        
        if self.red < self.black:
            #self.double_counter = 0
            self.loop = 1
            if self.round == 2:
                if self.loop_counter2 == 1:
                    self.loop_counter2 = 0
                    self.double_counter = 1
                self.loop_counter = 0

                if x1 != 7 and y1 != 7:
                    piece1 = self.button_list[c][e] #in charge of right-way movement
                    if piece1.cget('bg') == 'red2' or piece1.cget('bg') == 'yellow':
                        if (y2 == y1+2 and x2==x1+2):
                            self.move = 2
                    if piece1.cget('bg') == 'red' or 'black':
                        if (y2 == y1+1 and x2==x1+1):
                            self.move = 1
                if x1 != 0 and y1 != 7:
                    piece2 = self.button_list[a][e] #in charge of left-way movement
                    if piece2.cget('bg') == 'red2' or piece2.cget('bg') == 'yellow':
                        if (y2==y1+2 and x2==x1-2):
                            self.move = 2
                    if piece2.cget('bg') == 'red' or 'black':
                        if (y2==y1+1 and x2==x1-1):
                            self.move = 1
                
                if current_location['bg'] == 'yellow1':
                    if x1 != 0:
                        piece = self.button_list[a][b]
                        if piece.cget('bg') == 'red2' or piece.cget('bg') == 'yellow':
                            if (y2 ==y1-2 and x2==x1-2):
                                self.move = 2
                        if piece.cget('bg') == 'red' or 'black':
                            if (y2 ==y1-1 and x2==x1-1):
                                self.move = 1
                    if x1 !=7:
                        piece = self.button_list[c][b]
                        if piece.cget('bg') == 'red2' or piece.cget('bg') == 'yellow':
                            if (y2 ==y1-2 and x2==x1+2):
                                self.move = 2
                        if piece.cget('bg') == 'red' or 'black':
                            if (y2 ==y1-1 and x2==x1+1):
                                self.move = 1

                if self.double_counter == 1 or current_location['bg'] == 'yellow1': 
                    if x1 != 0:
                        piece = self.button_list[a][b]
                        if piece.cget('bg') == 'red2' or piece.cget('bg') == 'yellow':
                            if (y2 ==y1-2 and x2==x1-2):
                                self.move = 2
                    if x1 !=7:
                        piece = self.button_list[c][b]
                        if piece.cget('bg') == 'red2' or piece.cget('bg') == 'yellow':
                            if (y2 ==y1-2 and x2==x1+2):
                                self.move = 2
                    if x1 != 7 and y1 != 7:
                        piece = self.button_list[c][e]
                        if piece.cget('bg') == 'red2' or piece.cget('bg') == 'yellow':
                            if (y2 ==y1+2 and x2==x1+2):
                                self.move =2
                    if x1 != 0 and y1 != 7:
                        piece = self.button_list[a][e]
                        if piece.cget('bg') == 'red2'  or piece.cget('bg') == 'yellow':
                            if (y2==y1+2 and x2==x1-2):
                                self.move = 2
                
               
                
                if self.move == 1:
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
                        self.move = 0
                        self.double_counter = 0
                
                
                if self.move == 2:
                    while self.loop == 1:
                        if x1 != 0: 
                            if (y2 ==y1-2 and x2==x1-2):
                                #self.button_list[a][b] =0
                                piece1 = self.button_list[a][b]
                                piece1['bg'] = 'red'
                                piece1['command'] = lambda a=a,b=b:self.grid_clicked(a,b)
                                piece1['image'] = self.img3#('image')#(self.img2)
                                self.button_list[a][b] = piece1
                        if x1 != 7:
                            if (y2 ==y1-2 and x2==x1+2):
                                piece2 = self.button_list[c][b]
                                piece2['bg'] = 'red'
                                piece2['command'] = lambda c=c,b=b:self.grid_clicked(c,b)
                                piece2['image'] = self.img3#('image')#(self.img2)
                                self.button_list[c][b] = piece2
                        if x1 != 0:
                            if (y2==y1+2 and x2==x1-2):
                                piece3 = self.button_list[a][e]
                                piece3['bg'] = 'red'
                                piece3['command'] = lambda a=a,e=e:self.grid_clicked(a,e)
                                piece3['image'] = self.img3
                                self.button_list[a][e] = piece3

                        if x1 != 7:
                            if (y2==y1+2 and x2 ==x1+2):
                                piece4 = self.button_list[c][e]
                                piece4['bg'] = 'red'
                                piece4['command'] = lambda c=c,e=e:self.grid_clicked(c,e)
                                piece4['image'] = self.img3
                                self.button_list[c][e] = piece4

                        if x2 > 1 and y2 > 1:
                            if pieceone.cget('bg') == 'red2' or pieceone.cget('bg') == 'yellow':
                                if second_pieceone.cget('bg') == 'red':
                                    #print("ab works")
                                    self.loop_counter2 = 1
                        if x2 < 6 and y2 > 1:
                            if piecetwo.cget('bg') == 'red2'  or piecetwo.cget('bg') == 'yellow':  
                                if second_piecetwo.cget('bg') == 'red':
                                    #print("cb works")
                                    self.loop_counter2 = 1
                        if x2 > 1 and y2 < 6:
                            if piecethree.cget('bg') == 'red2' or piecethree.cget('bg') == 'yellow':
                                if second_piecethree.cget('bg') == 'red':
                                    #print("ae works")
                                    self.loop_counter2 = 1
                        if x2 < 6 and y2 < 6:
                            if piecefour.cget('bg') == 'red2' or piecefour.cget('bg') == 'yellow':
                                if second_piecefour.cget('bg') == 'red':
                                    #print("ce works")
                                    self.loop_counter2 = 1
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
                        self.move = 0
                        self.red_counter -=1
                        self.double_counter = 0
                        if self.loop_counter2 == 1:
                            self.round = 2
                    self.loop = 1
                        #self.double_jump_counter = 2
                        
                if y2 == 7:
                    piece['image'] = self.img5
                    piece['bg'] = 'yellow1'
                    
        self.update_board()
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
    
    def update_board(self):
        pass
    
    def check_piece(self, x, y):
        if self.logic.color_check(x,y) == 'black':
            if self.round == 1:
                self.black = 1 
                self.red = 0
            if self.round ==2:
               self.black = 1
               self.red = 0
        if self.logic.color_check(x,y) == 'red':
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
    def check_grid(self,x,y):
        self.grid_clicked(x,y)
    #def destroy(self,x,y):
        pass
        
        
        
        #tk.Button.destroy(x,y)
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
