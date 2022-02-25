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
        self.board = [["-" for row in range(size)] for col in range(size)]
        # Stores the co-ordinates for ships
        self.ships = []
        # Stores the guesses (co-ordinates)
        self.guesses = []
        self.rounds = 16
        self.ship_placing()

    def board_print(self):
        """
        Prints the game boards for both the player and computer.
        It adds co-ordinate numbers on the and left of the board.
        """
        print(f"\n {self.name.capitalize()}'s board\n")
        print("  0 1 2 3 4 5 6 7")
        row_number = 0
        for row in self.board:
            print(row_number, " ".join(row))
            row_number += 1

    def ship_placing(self):
        """
        Place ships in random positions on the board.
        For player ships, this method marks the board with (S).
        """
        for _ in range(self.num_ships):
            row, col = random_coord(self.size)
            # Loops until an empty space is found
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
        print(f"\n You entered {row} and {col}.")

        # If player hits a ship
        if (row, col) in self.ships:
            self.board[row][col] = "*"
            print("\n Hit confirmed, Captain!")
        else:
            print("\n Target missed, sir!")

    def bot_guess(self, row, col):
        """
        This method helps differentiate between
        player and bot guesses.
        """
        self.guesses.append((row, col))
        self.board[row][col] = "M"

        # If bot hits a ship
        if (row, col) in self.ships:
            self.board[row][col] = "*"
            print("\n Bot is on fire!")
        else:
            print("\n Bot can't aim!")

    def guessed(self, row, col):
        """
        Checks if player has already entered
        a set of co-ordinates.
        """
        if (row, col) in self.guesses:
            return True
        return False

    def player_guess(self):
        """
        Prompts the user for input.
        Converts input to integers.
        """
        while True:
            try:
                print("\n|" + "«" * 15 + "»" * 15 + "|\n")
                print(f" Remaining turns: {self.rounds}\n")
                row = input(" Captain, first co-ordinate: \n")
                row = int(row)
                col = input(" Sir, second co-ordinate: \n")
                col = int(col)
                break
            except ValueError:
                print(" We can only enter numbers for co-ordinates!")

        return int(row), int(col)

    def validate_input(self, row, col):
        """
        Checks if co-ordinates (input numbers) are
        within board size range and handles invalid inputs.
        """
        try:
            # Checks number range for player inputs
            if not 0 <= row < 8:
                raise ValueError
            if not 0 <= col < 8:
                raise ValueError
            if self.bot_board.guessed(row, col):
                print(" We've already tried that Captain!")
                return False
        except ValueError:
            print(" Invalid number! Accepted range: 0-7!\n")
            return False

        return True

    def intro(self):
        """
        Intro screen with information about the game.
        """
        print("|" + "V" * 35 + "|\n")
        print(" The battle is about to begin!")
        print(" Board is 8x8. You have 8 ships.\n")
        print(" Top left corner is row 0, col 0")
        print(" Enter target co-ordinates using numbers")
        print(" Valid co-ordinates are 0-7")
        print(" Only single digits are valid")
        print(" Target hit: * --- Target miss: M\n")
        print("|" + "V" * 35 + "|\n")
        self.play_game()

    def play_game(self):
        """
        The main game loop takes care of guesses and exits the game if it's
        completed or if the player no longer wants to play.
        """
        player_name = input(" I am Captain:\n")
        print("\n|" + "«" * 15 + "»" * 15 + "|\n")
        # Initialize the player board
        player_board = Board(self.size, self.num_ships,
                             player_name, player=True)
        self.player_board = player_board
        # Initialize the bot board
        bot_board = Board(self.size, self.num_ships, "Bot", player=False)
        self.bot_board = bot_board

        while True:
            # Prints the boards repeatedly, no scrolling needed
            Board.board_print(player_board)
            Board.board_print(bot_board)

            # Asks for input from player and validates the entry
            row, col = self.player_guess()
            # Loops until a valid guess has been put in
            while not self.validate_input(row, col):
                row, col = self.player_guess()
            # This marks the bot's board depending on guess
            player_try = self.bot_board.guess(row, col)

            # Bot/computer randomly hits the board
            row, col = random_coord(self.size)
            # Loops until a valid position has been found
            while self.player_board.guessed(row, col):
                row, col = random_coord(self.size)
            # This marks the player's board depending on guess
            bot_try = self.player_board.bot_guess(row, col)

            self.rounds -= 1
            if self.rounds == 0:
                print("\n The battle is over.")
                return False

# Sets the board size and number of ships
# Names are inputed or already set
run_game = Board(size=8, num_ships=8, name="")
run_game.intro()
