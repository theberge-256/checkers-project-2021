class CheckersPiece:
    """
        Piece data, includes how pieces are allowed to move
    """
    def __init__(self, x, y, game, team):
        self.game = game
        self.team = team # "red" or "black"
        self.x = x
        self.y = y
        
        if game.board[x][y] == 0:
            game.board[x][y] = self

        self.is_king = False
        self.is_dead = False
    
    def destroy(self):
        self.game.board[self.x][self.y] = 0
        self.is_dead = False

    def move_to(self, x, y):
        self.game.board[self.x][self.y] = 0

        self.x = x
        self.y = y
        self.game.board[self.x][self.y] = self

    def apply_move(self, move):
        """
            Apply a move outputted from allowed_moves
        """
        self.move_to(move.x, move.y)
        if move.destroyedPiece != -1:
            self.game.get_cell(move.x, move.y).destroy()

        for extra_move in move.extras:
            self.apply_move(extra_move)

        return True

    def allowed_moves(self):
        """
            Gets the moves that are permitted from the piece
            TODO -> if there is a player where it can move, but not a player after,
            allow "jumping" over players.
            X = self player
            Y = other players
            Z = allowed moves
               |   |   |   |
            -------------------
             cant go backwards
            -------------------
               |   | X |   |
            -------------------
               | Z |   | Y |   < jump thing is TODO
            -------------------
               |   |   |   | Z 
        """
        # stored as an array of {x, y, destroyedPiece:{x, y}, extras: None|[more of these]}s
        possible_moves = []
        x = self.x
        y = self.y
        # If its black, it moves from y = 0, to y = 8
        # If its black, it moves from y = 8 to y = 0
        direction = -1
        if self.team == 'black':
            direction = 1
        # if there is no player on right, its direction
        #if self.counter == 2:
                #del(possible_moves[0])
                #del(possible_moves[0])
                #self.counter = 0
        cell = self.game.get_cell(x + 1, y + direction, True)
        if cell == 0:
            possible_moves.append({
                "x": x + 1,
                "y": y + direction,
                "destroyedPiece": -1,
                "extras1": [] # this will be used for extra jumps
            })
        elif cell != -1 and cell != self.team and self.game.get_cell(x + 2, y + direction * 2, True) == 0: # if not 0, then it must be an object
            possible_moves.append({
                "x": x + 2,
                "y": y + direction * 2,
                "destroyedPiece": {
                    "x": x + 1,
                    "y": y + direction
                },
                "extras2": [] # this will be used for extra jumps
            })



        # if there is no player on left, its direction
        cell = self.game.get_cell(x - 1, y + direction, True)
        if cell == 0:
            possible_moves.append({
                "x": x - 1,
                "y": y + direction,
                "destroyedPiece": -1,
                "extras3": []
            })
        elif cell != -1 and cell != self.team and self.game.get_cell(x - 2, y + direction * 2, True) == 0: # if not 0, then it must be an object
            possible_moves.append({
                "x": x - 2,
                "y": y + direction * 2,
                "destroyedPiece": {
                    "x": x - 1,
                    "y": y + direction
                },
                "extras4": [] # this will be used for extra jumps
            })

        if self.is_king:
            # if there is no player on right, opposite its direction, and is a king
            cell = self.game.get_cell(x + 1, y - direction, True)
            if cell == 0:
                possible_moves.append({
                    "x": x + 1,
                    "y": y - direction,
                    "destroyedPiece": -1,
                    "extras5": []
                })
            elif cell != -1 and cell != self.team and self.game.get_cell(x + 2, y - direction * 2, True) == 0: # if not 0, then it must be an object
                possible_moves.append({
                    "x": x + 2,
                    "y": y - direction * 2,
                    "destroyedPiece": {
                        "x": x + 1,
                        "y": y - direction
                    },
                    "extras6": [] # this will be used for extra jumps
                })

            # if there is no player on left,  opposite its direction, and is a kings
            cell = self.game.get_cell(x - 1, y - direction, True)
            if cell == 0:
                possible_moves.append({
                    "x": x - 1,
                    "y": y - direction,
                    "destroyedPieces": [],
                })
            elif cell != -1 and cell != self.team and self.game.get_cell(x - 2, y - direction * 2, True) == 0: # if not 0, then it must be an object
                possible_moves.append({
                    "x": x - 2,
                    "y": y - direction * 2,
                    "destroyedPiece": {
                        "x": x - 1,
                        "y": y - direction
                    },
                    "extras": [] # this will be used for extra jumps
                })


        return possible_moves

    
class CheckersLogic:
    """
        Class with much of the logic, which will be used to store pieces
         and know the rule of the game
        
        This will some how be passed to the gui class in the future
    """
    def __init__(self):
        # when 0, there is no piece
        self.board = []
        for x in range(8):
            arr = []
            for y in range(8): 
                ccell = (x,y)
                arr.append(ccell)
            self.board.append(arr)
        self.setup()

    def setup(self):
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 1:
                    if y < 3:
                        self.board[x][y] = CheckersPiece(x, y, self, 'black')
                        continue
                    if y > 4:
                        self.board[x][y] = CheckersPiece(x, y, self, 'red')
                        continue
       
                self.board[x][y] = 0
                #del(self.board[x])
                #del(self.board[y]) 
    def get_cell(self, x, y, by_team=False):
        """
            Get a cell (x, y) on self board
        """
        if x < 8 and y < 8:
            if not by_team:
                return self.board[x][y]
            cell = self.board[x][y]
            if cell == 0:
                return cell
            return cell.team
        return -1
    def color_check(self,x,y):
        if x < 8 and y < 8:         
            self.x = x
            self.y = y
            cell = self.board[x][y]
            return cell.team
    def first_get_cell(self,x,y):
        if x < 8 and y < 8:            
            self.x = x
            self.y = y
            cell = 0
            cell = self.board[x][y]
            return cell
    