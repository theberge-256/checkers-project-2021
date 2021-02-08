class CheckersPiece:
    """
        Piece data, includes how pieces are allowed to move
    """
    def __init__(self, x, y, board, team):
        self.board = board
        self.team = team # "red" or "black"
        self.x = x
        self.y = y
        
        if board[x][y] == 0:
            board[x][y] = self

        self.is_king = False
        self.is_dead = False
    
    def destroy(self):
        self.board[self.x][self.y] = 0
        self.is_dead = False

    def move_to(self, x, y):
        self.board[self.x][self.y] = 0

        self.x = x
        self.y = y
        self.board[self.x][self.y] = self


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
        # stored as an array of {x, y, destroyedPieces:[{x, y}]}s
        possible_moves = []
     
        x = self.x
        y = self.y
        # If its black, it moves from y = 0, to y = 8
        # If its black, it moves from y = 8 to y = 0
        direction = -1
        if self.team == 'black':
            direction = 1

        # if there is no player on right, its direction
        if self.board[x + 1][y + direction] == 0:
            possible_moves.append({
                "x": x + 1,
                "y": y + direction,
                "destroyedPieces": [],
            })
        # if there is no player on left, its direction
        if self.board[x - 1][y + direction] == 0:
            possible_moves.append({
                "x": x - 1,
                "y": y + direction,
                "destroyedPieces": [],
            })
        if self.is_king:
            # if there is no player on right, opposite its direction, and is a king
            if self.board[x + 1][y - direction] == 0:
                possible_moves.append({
                    "x": x + 1,
                    "y": y - direction,
                    "destroyedPieces": [],
                })

            # if there is no player on left,  opposite its direction, and is a kings
            if self.board[x - 1][y - direction] == 0:
                possible_moves.append({
                    "x": x - 1,
                    "y": y - direction,
                    "destroyedPieces": [],
                })
        
        return possible_moves

    
class CheckersGame:
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
                arr.append(0)

            self.board.append(arr)

        self.setup()

    def setup(self):
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 1:
                    if y < 3:
                        self.board[x][y] = CheckersPiece(x, y, self.board, 'black')
                        continue
                    if y > 4:
                        self.board[x][y] = CheckersPiece(x, y, self.board, 'black')
                        continue

                self.board[x][y] = 0
