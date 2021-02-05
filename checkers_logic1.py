class CheckersPiece:
    """
        Piece data, includes how pieces are allowed to move
    """
    def __init__(self, x, y, board, team):
        self.board = board
        self.team = team # "white" or "black"
        self.x = x
        self.y = y
        self.is_king = False

    def allowed_moves(self):
        """
            Gets the moves that are permitted from the piece
            TODO -> if there is a player where it can move, but not a player after,
            allow "jumping" over players.
            TODO -> allow backwards movement by kings

            X = self player
            Y = other players
            Z = allowed moves
               |   |   |   |
            -------------------
             cant go backwards
            -------------------
               |   | X |   |
            -------------------
               | Z |   | Y |   
            -------------------
               |   |   |   | Z 

        """

        possible_moves = [] # stored as an array of [x, y]s
        x = self.x
        y = self.y
        # If its white, it moves from y = 0, to y = 8
        # If its black, it moves from y = 8 to y = 0
        direction = -1
        if self.team == 'white':
            direction = 1

        # if there is no player on right, its direction
        if self.board[x + 1][y + direction] == 0:
            possible_moves.append([x + 1, y + direction])
        # if there is no player on left, its direction
        if self.board[x - 1][y + direction] == 0:
            possible_moves.append([x - 1, y + direction])
        if self.is_king:
            # if there is no player on right, opposite its direction, and is a king
            if self.board[x + 1][y - direction] == 0:
                possible_moves.append([x + 1, y - direction])

            # if there is no player on left,  opposite its direction, and is a kings
            if self.board[x - 1][y - direction] == 0:
                possible_moves.append([x - 1, y - direction])
        
        return possible_moves

    
class CheckersLogic:
    """
        Class with much of the logic, which will be used to store pieces
         and know the rule of the game
        
        This will some how be passed to the gui class in the future
    """
    def __init__(self):
        #   when 0, there is no piece
        self.board = []
        for x in range(8):
            arr = []
            for y in range(8):
                arr.append(0)

            self.board.append(arr)