"""
   CS 5001
   Final Project, 12/10/2021
   Fall 2021
   Jinyan Li

   Contains class Computer and methods to generate a move on the board for the
   computer player
"""

import random


class Computer:
    """
    class - Computer
    Contains the following methods:
        __init__: to create a computer player
        win_in_one: goes through the remaining positions on the board and
                    returns a position (two-element list) that would enable
                    the player to win in one additional move, if any
        get_position: get a row & col position from computer
    """

    def __init__(self, length, board, name="Computer"):
        """
        method: __init__
                Instantiate a Computer instance with given parameters, length,
                board, and an optional parameter, name.
        :param length: an integer, length of the board grid
        :param board: a Board instance
        :param name: a string, the player's name
        """
        self.length = length
        self.name = name
        self.board = board

    def win_in_one(self, tag):
        """
        method: win_in_one
                Goes through the remaining positions on the board and returns
                a position (two-element list) that would enable the player to
                win in one additional move, if any. Otherwise, return None.
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: a position (two-element list) that would enable the player to
                win in one additional move, if there is one. Otherwise,
                return None.
        """
        for position in self.board.available_positions():
            # make moves on the available positions of the board
            self.board.make_move(position, tag)
            # save the boolean value of whether one move would win to win_check
            win_check = self.board.player_won(tag)
            # reverse the move back to empty position ("_")
            self.board.reverse_move(position)
            if win_check:
                return position
        return None

    def get_position(self):
        """
        method: get_position
                - First, checks if the computer player would win in one move,
                  if so, returns that position to win the game.
                - Then, checks if the computer player would lose in one move,
                  if so, returns that position to prevent losing the game.
                - If win or lose in one move scenario does not apply, returns
                  either center or a corner position if it is still available.
                - If none of the above applies, returns a random position that
                  is available.
        :return: a position (two-element list)
        """
        # checks if computer could win in one move
        win_position = self.win_in_one("O")
        if win_position is not None:
            return win_position
        # checks if computer could lose in one move
        loss_position = self.win_in_one("X")
        if loss_position is not None:
            return loss_position
        # goes through center and corner positions
        positions = [[1, 1], [0, 0], [0, 2], [2, 0], [2, 2]]
        for position in positions:
            if self.board.position_open(position):
                return position
        while True:
            row = random.randint(0, self.length - 1)
            col = random.randint(0, self.length - 1)
            position = [row, col]
            if self.board.position_open(position):
                return position

    def __str__(self):
        """
        method: __str__
                Prints the computer player's name
        :return: nothing
        """
        return self.name
