import os
import time
import sys
import termios
from window2 import Window
from objects import Ball, Paddle, Brick, SpecialBrick
from colorama import init
from colorama import Fore, Back, Style
from time import monotonic as clock, sleep

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
        if self.level == 1 or self.level > 2:

            brick2 = SpecialBrick(
                10, 10, 20, 10, 4, "rainbow", " ", 0, 0, Fore.GREEN, "█")
            brick7 = SpecialBrick(
                75, 10, 20, 10, 4, "rainbow", " ", 0, 0, Fore.WHITE, "█")

            brick3 = Brick(10, 5, 3, 12, 2,  0, 0, Fore.GREEN, "▒")
            bricka = Brick(25, 5, 3, 12, 2,  0, 0, Fore.GREEN, "▒")
            brickb = Brick(40, 5, 3, 15, 2,  0, 0, Fore.GREEN, "▒")
            brick4 = Brick(58, 5, 3, 12, 2, 0, 0, Fore.GREEN, "▒")
            brick5 = Brick(73, 5, 3, 12, 2,  0, 0, Fore.GREEN, "▒")

            brick10 = SpecialBrick(22, 10, 4, 10, 1, "multiball",
                                   "⤧", 0, 0, Fore.WHITE, "█")
            brick1 = SpecialBrick(34, 10, 4, 10, 2, "grab",
                                  "⤓", 0, 0, Fore.WHITE, "█")
            brick11 = SpecialBrick(51, 10, 4, 10, 2, "unbreakable",
                                   " ", 0, 0, Fore.WHITE, "░")
            brick12 = SpecialBrick(63, 10, 4, 10, 1, "multiball",
                                   "⤧", 0, 0, Fore.WHITE, "█")
            brick13 = Brick(22, 16, 4, 10, 3,  0, 0, Fore.GREEN, "▒")
            brick14 = Brick(34, 16, 4, 10, 1,  0, 0, Fore.GREEN, "▒")
            brick15 = Brick(51, 16, 4, 10, 1,  0, 0, Fore.GREEN, "▒")
            brick16 = Brick(63, 16, 4, 10, 3, 0, 0, Fore.GREEN, "▒")

            brickc = SpecialBrick(
                46, 10, 10, 3, 4, "expandpaddle", "⟷", 0, 0, Fore.WHITE, "█")

            brickz = SpecialBrick(
                22, 21, 4, 51, 2, "shooting", "!", 0, 0, Fore.WHITE, "█")

            brickx1 = SpecialBrick(
                22, 30, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")

            brickx2 = SpecialBrick(
                32, 27, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            brickx3 = SpecialBrick(
                42, 30, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            brickx4 = SpecialBrick(
                52, 27, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            brickx5 = SpecialBrick(
                62, 30, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            # brickx6 = SpecialBrick(
            #     65, 27, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")

            brickex = Brick(22, 27, 3, 10, 3)
            brickex1 = Brick(32, 30, 3, 10, 3)
            brickex2 = Brick(42, 27, 3, 10, 3)
            brickex3 = Brick(52, 30, 3, 10, 3)
            brickex4 = Brick(62, 27, 3, 10, 3)

            # window.addBrick(brickex)
            # window.addBrick(brickex1)
            # window.addBrick(brickex2)
            # window.addBrick(brickex3)
            # window.addBrick(brickex4)

            window.addBrick(brick2)
            window.addBrick(brick7)
            window.addBrick(brick3)
            window.addBrick(brick4)
            window.addBrick(brick5)
            window.addBrick(bricka)
            window.addBrick(brickb)

            window.addBrick(brick1)
            window.addBrick(brick10)
            window.addBrick(brick11)
            window.addBrick(brick12)
            window.addBrick(brick14)
            window.addBrick(brick15)

            window.addBrick(brick13)
            window.addBrick(brick16)

            window.addBrick(brickc)
            window.addBrick(brickz)
            # window.addBrick(brickx1)
            # window.addBrick(brickx2)
            # window.addBrick(brickx3)

            # window.addBrick(brickx4)
            # window.addBrick(brickx5)
            # window.addBrick(brickx6)

        if self.level == 2:
            brick2 = SpecialBrick(
                10, 10, 20, 10, 4, "multiball", "⤧", 0, 0, Fore.GREEN, "█")
            brick7 = SpecialBrick(
                75, 10, 20, 10, 4, "multiball", "⤧", 0, 0, Fore.WHITE, "█")
            brickx1 = SpecialBrick(
                22, 30, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")

            brickx2 = SpecialBrick(
                32, 27, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            brickx3 = SpecialBrick(
                42, 30, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            brickx4 = SpecialBrick(
                52, 27, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")
            brickx5 = SpecialBrick(
                62, 30, 3, 10, 1, "explode", "", 0, 0, Fore.WHITE, "⣿")

            brickex = Brick(22, 27, 3, 10, 3)
            brickex1 = Brick(32, 30, 3, 10, 3)
            brickex2 = Brick(42, 27, 3, 10, 3)
            brickex3 = Brick(52, 30, 3, 10, 3)
            brickex4 = Brick(62, 27, 3, 10, 3)
            window.addBrick(brick2)
            window.addBrick(brick7)

            window.addBrick(brickex)
            window.addBrick(brickex1)
            window.addBrick(brickex2)
            window.addBrick(brickex3)
            window.addBrick(brickex4)

            window.addBrick(brickx1)
            window.addBrick(brickx2)
            window.addBrick(brickx3)
            window.addBrick(brickx4)
            window.addBrick(brickx5)

    def initialize_game(self):
        begin = clock()

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
                print("time taken :", clock() - begin)
                break


if __name__ == "__main__":

    print("Press Enter to  key to start the game")
    var = sys.stdin.read(1)

    if var:
        print("Game started")
        Game = Game()
        Game.initialize_game()
