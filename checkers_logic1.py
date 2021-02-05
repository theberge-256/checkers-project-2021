
class CheckersLogic:
    """
        Class with all the logic, which will be used to store pieces
        find out where pieces are allowed to go, and know the rule of the game
        
        This will some how be passed to the gui class in the future
    """
    def __init__(self):
        # Maybe something like:
        #   -1 = no piece
        #   0  = black piece
        #   1  = white piece
        self.board = []
        for x in range(8):
            arr = []
            for y in range(8):
                arr.append(-1)

            self.board.append(arr)
