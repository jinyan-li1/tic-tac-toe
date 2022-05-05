"""
   CS 5001
   Final Project, 12/10/2021
   Fall 2021
   Jinyan Li

   Contains class Player and methods to take input from a player and generate
   a move on the board
"""


class Player:
    """
    class - Player
    Contains the following methods:
        __init__: to create a player
        validate_input: validate player's input to ensure it is valid
        get_position: get a row & col position (two-element list) from player
    """

    def __init__(self, length, name="Player"):
        """
        method: __init__
                Instantiate a Player instance with given parameter, length,
                and an optional parameter, name.
        :param length: an integer, length of the board grid
        :param name: a string, the player's name
        """
        self.length = length
        self.name = name

    def validate_input(self, text):
        """
        method: validate_input
                Checks if the parameter, text, can be converted to an integer.
                If so, checks if the integer is within the grid.
        :param text: a string, representing the index on the row or the column
        :return: True if text can be converted into an integer and it is in
                bound of the grid, False otherwise
        """
        if text.isnumeric():
            if int(text) in range(self.length):
                return True
        return False

    def get_position(self):
        """
        method: get_position
                Prompts player to enter integers for the indices of row and
                column they want to place their tag at on the board while
                calling validate_input to validate their input to ensure
                it is in bound, and re-prompts player to enter again if
                the input is invalid.
        :return: a two-element list consists of row (int) and col (int)
        """
        row = ""
        while not self.validate_input(row):
            row = input(f"{self.name}, please enter an integer from 0 "
                        f"to {self.length - 1} for the row: ")
        col = ""
        while not self.validate_input(col):
            col = input(f"{self.name}, please enter an integer from 0 "
                        f"to {self.length - 1} for the column: ")
        return [int(row), int(col)]  # position

    def __str__(self):
        """
        method: __str__
                Prints the player's name
        :return: nothing
        """
        return self.name
