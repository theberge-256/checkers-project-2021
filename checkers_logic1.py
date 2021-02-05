
class CheckersLogic:
    """
        Class with all the logic, which will be used to store pieces
        find out where pieces are allowed to go, and know the rule of the game
        
        This will some how be passed to the gui class in the future
    """
    def __init__(self):
        self.board = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]