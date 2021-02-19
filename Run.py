import os
import time
import sys
import termios
from window2 import Window
from objects import Ball, Paddle, Brick, SpecialBrick
from colorama import init
from colorama import Fore, Back, Style
init()


class Game():
    def __init__(self):
        self.level = 1
        self.lives = 5
        self.score = 0
        self.brickPattern = []

    def initialize_level(self):
        pass

    def initialize_brickpattern(self, window):
        if self.level == 1:
            brick1 = Brick(10, 5, 3, 50, 3, 0, 0, Fore.GREEN, "▒")
            brick9 = SpecialBrick(22, 20, 1, 12, 1, "unbreakable",
                                  "$", 0, 0, Fore.GREEN, "█")
            brick10 = SpecialBrick(40, 20, 1, 30, 2, "lmao",
                                   "@", 0, 0, Fore.WHITE, "█")
            window.addBrick(brick1)
            window.addBrick(brick10)

        if self.level == 2:
            brick1 = Brick(10, 5, 3, 12, 3, 0, 0, Fore.GREEN, "▒")
            brick2 = Brick(30, 5, 3, 12, 2,  0, 0, Fore.GREEN, "▒")
            brick3 = Brick(50, 15, 3, 12, 1,  0, 0, Fore.GREEN, "▒")
            brick4 = Brick(70, 15, 1, 12, 1, 0, 0, Fore.GREEN, "▒")
            brick5 = Brick(20, 10, 1, 12, 3,  0, 0, Fore.GREEN, "▒")
            brick6 = Brick(40, 10, 1, 12, 2,  0, 0, Fore.GREEN, "▒")
            brick7 = Brick(60, 10, 1, 12, 1,  0, 0, Fore.GREEN, "▒")
            brick8 = Brick(80, 10, 1, 12, 1,  0, 0, Fore.GREEN, "▒")
            brick9 = SpecialBrick(22, 20, 1, 12, 1, "unbreakable",
                                  "$", 0, 0, Fore.GREEN, "█")
            brick10 = SpecialBrick(40, 20, 1, 12, 2, "lmao",
                                   "@", 0, 0, Fore.WHITE, "█")

            window.addBrick(brick1)
            window.addBrick(brick2)
            window.addBrick(brick3)
            window.addBrick(brick4)
            window.addBrick(brick5)
            window.addBrick(brick6)
            window.addBrick(brick7)
            window.addBrick(brick8)
            window.addBrick(brick9)
            window.addBrick(brick10)

    def initialize_game(self):
        while True:
            window = Window(self.level, self.lives, self.score)
            self.initialize_brickpattern(window)
            ball1 = Ball(52, 39, 1, 1, 1, 1, Fore.MAGENTA, "⬤")
            paddle = Paddle(40, 40, 1, 24, Fore.WHITE, "▓")
            window.add(ball1)
            window.addPaddle(paddle)
            self.level, self.lives, self.score = window.render()
            if self.lives == 0:
                print("Game over youe score is :", self.score)
                break


if __name__ == "__main__":

    print("Press Enter to  key to start the game")
    var = sys.stdin.read(1)

    if var:
        print("Game started")
        Game = Game()
        Game.initialize_game()
