"""
   CS 5001
   Final Project, 12/10/2021
   Fall 2021
   Jinyan Li

   Contains class Board and methods to set up the board for Tic-Tac-Toe
"""

import numpy as np


class Board:
    """
    class - Board
    Contains the following methods:
        __init__: to set up a grid as the board
        full_board: check if the board is full
        available_positions: return available positions on the board
        position_open: check if a specific position is open on the board
        make_move: make a move on the board with a given position
        reverse_move: reverse a move (helper function)
        row_check: check rows for wins
        col_check: check column for wins
        left_check: check the diagonal from left to right for wins
        right_check: check the diagonal from right to left for wins
        cross_check: check both diagonals for wins
        player_won: check all scenarios to determine if the player won
        __str__: prints the board.
    """

    def __init__(self, length):
        """
        method: __init__
                Instantiate a Board instance with given parameter, length.
                grid is a nested list with length sublists, each containing
                length elements, each element is a string of a single
                underscore.
        :param length: an int
        """
        self.length = length
        self.grid = [["_"] * self.length for i in range(self.length)]

    def full_board(self):
        """
        method: full_board
                Checks if the board is full
        :return: True if board is full, False otherwise
        """
        for row in self.grid:
            for col in row:
                if col == "_":
                    return False
        return True

    def available_positions(self):
        """
        method: available_positions
                Goes through the board and return available positions
        :return: all open positions (lists) on the board in a nested list
        """
        open_pos = []
        for i in range(3):  # i is the index of row
            for j in range(3):  # j is the index of col
                if self.grid[i][j] == "_":
                    open_pos.append([i, j])
        return open_pos

    def position_open(self, position):
        """
        method: position_open
                Checks if a position of the grid is open
        :param position: a two-element list consists of row (int) and col (int)
        :return: True if the position is open ("_"), False otherwise
        """
        return self.grid[position[0]][position[1]] == "_"

    def make_move(self, position, tag):
        """
        method: make_move
                Makes a move on the board with given tag at the specified
                position if it is open and in bound.
                If the board is full, prints a message on the screen.
                If the position is taken, prints a message on the screen and
                raise ValueError.
        :param position: a two-element list consists of row (int) and col (int)
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: nothing
        """
        if not self.full_board():
            if self.position_open(position):
                self.grid[position[0]][position[1]] = tag
            else:
                print("Position is taken already.")
                raise ValueError
        else:
            print("Board is full.")

    def reverse_move(self, position):
        """
        method: reverse_move
                Reverse a move back to empty state ("_")
        :param position: a two-element list consists of row (int) and col (int)
        :return: nothing
        """
        self.grid[position[0]][position[1]] = "_"

    def row_check(self, tag):
        """
        method: row_check
                Checks if any row of the board contains the same tag that
                constitutes a horizontal win
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: True of any row contains the same tag (a win), False otherwise
        """
        for row in self.grid:
            # goes through each row's elements and compare them to the tag,
            # if a row's all elements match the tag, return True
            if all(row_ele == tag for row_ele in row):
                return True
        return False

    def col_check(self, tag):
        """
        method: col_check
                Checks if any column of the board contains the same tag that
                constitutes a vertical win
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: True of any column contains the same tag (a win), False
                otherwise
        """
        # converts the grid into a transposed version which shows each column's
        # values on rows instead
        transposed_grid = np.transpose(self.grid)
        for row in transposed_grid:
            if all(row_ele == tag for row_ele in row):
                return True
        return False

    def left_check(self, tag):
        """
        method: left_check
                Checks the diagonal from left to right for wins
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: True if all tags matched on left diagonal, False if there is
                an unmatched tag on left diagonal
        """
        length = len(self.grid)
        for i in range(length):
            # i is incrementing row & col index since they're both going
            # from index 0 to length of grid - 1
            if not self.grid[i][i] == tag:
                return False
        return True

    def right_check(self, tag):
        """
        method: right_check
                Checks the diagonal from right to left for wins
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: True if all tags matched on right diagonal, False if there is
                an unmatched tag on right diagonal
        """
        length = len(self.grid)
        for i in range(length):  # i is row index
            j = length - i - 1  # j is col index from right to left
            if not self.grid[i][j] == tag:
                return False
        return True

    def cross_check(self, tag):
        """
        method: cross_check
                Checks both diagonals for wins
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: True if all tags matched on either right or left diagonals,
                 False otherwise (neither diagonal has all matches)
        """
        return self.left_check(tag) or self.right_check(tag)

    def player_won(self, tag):
        """
        method: player_won
                Checks all scenarios to determine if the player won the game
        :param tag: string representing the player's tag, "X" for human
                player & "O" for computer player
        :return: True and prints a message if player won the game,
                False otherwise
        """
        win = False
        if self.row_check(tag) or self.col_check(tag) or self.cross_check(tag):
            win = True
        return win

    def __str__(self):
        """
        method: __str__
                Prints the game board
        :return: nothing
        """
        output = ""
        for row in self.grid:
            output += "| "
            for col in row:
                output += f"{col} "
            output += "|\n"
        return output
