from random import randint

def random_coord(size):
    """
    This function helps with providing a random integer
    based on the size of the board.
    It's a helper function for the rest of the game.
    """
    row = randint(0, size - 1)
    col = randint(0, size - 1)
    return col, row

class Board:
    """
    The Board class contains almost everything for the game to run. 
    """

    def __init__(self, size, num_ships, name, player=False):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.player = player
        self.board = [["O" for row in range(size)] for col in range(size)]
        # Stores the co-ordinates for ships
        self.ships = []
        # Stores the guesses (co-ordinates)
        self.guesses = []
        self.rounds = 16
    

    def boards(self):
        """
        Prints the game boards for both player and computer
        """
        print(f"Captain {self.name}, ships are in formation!")
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, row, col):
        self.guesses.append((row, col))
        self.board[row][col] = "X"

        if (row, col) in self.ships:
            self.board[row][col] = "*"
            return "Hit confirmed, Captain {self.name}!"
        else:
            return "Target missed, Captain!"

