import os
import time
import sys
import termios


class Game():
    def __init__(self):
        self.level = 1
        self.brickPattern = []

    def initialize_game():
        pass


if __name__ == "__main__":

    print("Press Enter to  key to start the game")
    var = sys.stdin.read(1)

    if var:
        print("Game started")
        Game = Game()
