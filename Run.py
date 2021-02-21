import os
import time
import sys
import termios
from window2 import Window
from objects import Ball, Paddle, Brick, SpecialBrick
from colorama import init
from colorama import Fore, Back, Style
import config as config
init()


class Game():
    def __init__(self):
        self.level = 1
        self.lives = config.LIVES
        self.score = 0
        self.brickPattern = []

    def initialize_level(self):
        pass

    def initialize_brickpattern(self, window):
        if self.level == 1:

            brick2 = Brick(10, 10, 20, 10, 3,  0, 0, Fore.GREEN, "▒")

            brick10 = SpecialBrick(80, 20, 1, 10, 3, "multiball",
                                   "⤧", 0, 0, Fore.WHITE, "█")
            brick3 = Brick(50, 15, 3, 12, 3,  0, 0, Fore.GREEN, "▒")
            brick4 = Brick(70, 15, 4, 12, 3, 0, 0, Fore.GREEN, "▒")
            brick5 = Brick(20, 25, 4, 12, 3,  0, 0, Fore.GREEN, "▒")
            brick1 = SpecialBrick(60, 10, 1, 30, 3, "grab",
                                  "⤓", 0, 0, Fore.WHITE, "█")
            window.addBrick(brick2)
            window.addBrick(brick3)
            window.addBrick(brick4)
            # window.addBrick(brick5)
            window.addBrick(brick1)
            window.addBrick(brick10)

        if self.level >= 2:
            brick1 = SpecialBrick(60, 10, 1, 30, 1, "fireball",
                                  "↟", 0, 0, Fore.WHITE, "█")
            brick7 = Brick(10, 5, 3, 12, 3, 0, 0, Fore.GREEN, "▒")
            brick2 = Brick(30, 5, 3, 12, 2,  0, 0, Fore.GREEN, "▒")
            brick3 = Brick(50, 15, 3, 12, 1,  0, 0, Fore.GREEN, "▒")
            brick4 = Brick(70, 15, 1, 12, 1, 0, 0, Fore.GREEN, "▒")
            brick5 = Brick(20, 10, 1, 12, 3,  0, 0, Fore.GREEN, "▒")
            brick6 = Brick(40, 10, 1, 12, 2,  0, 0, Fore.GREEN, "▒")
            brick8 = SpecialBrick(
                80, 10, 1, 12, 1, "shrinkpaddle", "⇄", 0, 0, Fore.GREEN, "█")
            brick9 = SpecialBrick(22, 20, 1, 12, 1, "expandpaddle",
                                  "⟷", 0, 0, Fore.GREEN, "█")
            brick10 = SpecialBrick(40, 20, 1, 12, 2, "multiball",
                                   "⤧", 0, 0, Fore.WHITE, "█")

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
            ball1 = Ball(config.PADDLE_X+int(config.PADDLE_WIDTH / 2), config.PADDLE_Y - 1,
                         1, 1, config.BALL_VX, config.BALL_VY, config.BALL_COLOR, config.BALL_SPRITE)
            paddle = Paddle(config.PADDLE_X, config.PADDLE_Y, 1,
                            config.PADDLE_WIDTH, config.PADDLE_COLOR, config.PADDLE_SPRITE)
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
