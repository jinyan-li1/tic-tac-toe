"""
   CS 5001
   Final Project, 12/10/2021
   Fall 2021
   Jinyan Li

   Contains class Game and methods to enable gameplay between two players
"""

from board import Board
from player import Player
from computer import Computer


class Game:
    """
    class - Game
    Contains the following methods:
            __init__: to initiate a game
            play: calls different methods from Board, Player and Computer
                instances to enable gameplay and replay
            toggle: switches between players and their tags to take turn
                playing the game
    """

    def __init__(self):
        """
        method: __init__
            Instantiate Game instances that consist of Board, Player and
            Computer instances passing in appropriate parameters to each one.
        """
        # instantiates a Game instance that consists of a Board instance
        length = 3  # sets a 3 * 3 grid
        self.board = Board(length)
        # validates input for player's name
        running = True
        while running:
            user_input = input("Please enter your name (Letters only): ")
            if user_input.isalpha():
                name_1 = user_input
                running = False
            else:
                continue
        # instantiates a Game instance that consists of a Player instance
        self.player_1 = Player(length, name_1)
        # instantiates a Game instance that consists of a Computer instance
        self.player_2 = Computer(length, self.board)
        # sets current player and current tag at the beginning of the game
        self.current_player = self.player_1
        self.current_tag = "X"

    def play(self):
        """
        method: play
                Calls different methods from Board, Player and Computer
                classes to enable gameplay
                - Prints the board before the game starts and each time a
                  player makes a move on the board
                - If the board is full, prints a message stating it is a
                  draw and terminates the game
                - If the board is not full, prompts current player to make
                  a move on the board
                - If the position player wants to take is already taken,
                  re-prompts player to enter another position
                - Each time a player makes a move, checks if the player has
                  won. If so, prints a victory message and terminates the
                  game. Else, toggles between players for the opponent to play.
                - After a match, prompts player to choose whether they want
                  to play again
        :return: nothing
        """
        while True:
            print("Welcome to the game of Tic-Tac-Toe")
            print(self.board)
            while not self.board.full_board():
                # gets position input from current player
                position = self.current_player.get_position()
                # current player tries to make a move on the board with current
                # tag
                try:
                    self.board.make_move(position, self.current_tag)
                # if value error raise, go back to the beginning of the loop
                # and re-prompts player to enter another position
                except ValueError:
                    continue
                print(f"{self.current_player} made a move:")
                print(self.board)
                if self.board.player_won(self.current_tag):
                    print(f"{self.current_player.name} won!")
                    break
                else:
                    self.toggle()
            if self.board.full_board():
                print("It's a draw.")  # if board is full

            user_input = ""
            while user_input.upper() not in ["YES", "Y", "NO", "N"]:
                user_input = input("Would you like to play Tic-Tac-Toe again? "
                                   "(Yes/No)\n")
            if user_input.upper() in ["YES", "Y"]:
                positions = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                             [2, 0], [2, 1], [2, 2]]
                for position in positions:
                    self.board.reverse_move(position)
                self.toggle()
                continue
            elif user_input.upper() in ["NO", "N"]:
                print("Thanks for playing!")
                return

    def toggle(self):
        """
        method: toggle
                Sets the current player to opponent and sets the current tag
                to opponent's tag
        :return: nothing
        """
        if self.current_player == self.player_1:
            self.current_player = self.player_2
            self.current_tag = "O"
        else:
            self.current_player = self.player_1
            self.current_tag = "X"


game = Game()
game.play()
