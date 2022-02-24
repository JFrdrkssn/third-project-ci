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

    def board_print(self):
        """
        Prints the game boards for both the player and computer.
        It adds co-ordinate numbers on the and left of the board.
        """
        print(f"\n{self.name.capitalize()}'s board\n")
        print("  0 1 2 3 4 5 6 7")
        row_number = 0
        for row in self.board:
            print(" ".join(row))
            row_number += 1

    def ship_placing(self):
        """
        Place ships in random positions on the board.
        For player ships, this method marks the board with (S).
        """
        for _ in range(self.num_ships):
            row, col = random_coord(self.size)
            while (row, col) in self.ships:
                row, col = random_coord(self.size)
            self.ships.append((row, col))
            if self.player:
                self.board[row][col] = "S"
    
    def guess(self, row, col):
        """
        Marks misses (M) and hits (*) on the board.
        Prints info to the player.
        Stores already guessed co-ordinates
        in the "guesses" list.
        """
        self.guesses.append((row, col))
        self.board[row][col] = "M"
        print(f"\nYou entered {row} and {col}.")

        if (row, col) in self.ships:
            self.board[row][col] = "*"
            print(f"\nHit confirmed, Captain {self.name.capitalize()}!"
        else:
            print("\nTarget missed, sir!")

    def bot_guess(self, row, col):
        """
        This method helps differentiate between
        player and bot guesses.
        """
        self.guesses.append((row, col))
        self.board[row][col] = "M"

        if (row, col) in self.ships:
            self.board[row][col] = "*"
            print("\nBot is on fire!")
        else:
            print("\nBot can't aim!")

    def guessed(self, row, col):
        """
        Checks if player has already entered
        a set of co-ordinates.
        """
        if (row, col) in self.guesses:
            return True
        return False

