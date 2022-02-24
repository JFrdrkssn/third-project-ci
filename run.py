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

    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["O" for row in range(size)] for col in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        # Stores the guesses on this board/game
        self.guesses = []
        # Stores the coordinates for ships
        self.ships = []
    

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

