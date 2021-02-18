import os
import sys
import time

from window2 import Window
from objects import Ball, Paddle, Brick, SpecialBrick
from colorama import init
from colorama import Fore, Back, Style

init()
FRAME_RATE = 0.1


if __name__ == "__main__":
    # # hide cursor
    # sys.stdout.write("\033[?25l")
    # sys.stdout.flush()

    # new game window
    window = Window()
    ball1 = Ball(70, 30, 1, 1, 1, 1, Fore.MAGENTA, "⬤")
    # print(ball1.color+ball1.sprite+Fore.RESET)
    paddle = Paddle(40, 40, 1, 24, Fore.WHITE, "▓")

    brick1 = Brick(10, 5, 2, 12, 3, 0, 0, Fore.GREEN, "▒")
    brick2 = Brick(30, 5, 1, 12, 2,  0, 0, Fore.GREEN, "▒")
    brick3 = Brick(50, 15, 1, 12, 1,  0, 0, Fore.GREEN, "▒")
    brick4 = Brick(70, 15, 1, 12, 1, 0, 0, Fore.GREEN, "▒")
    brick5 = Brick(20, 10, 1, 12, 3,  0, 0, Fore.GREEN, "▒")
    brick6 = Brick(40, 10, 1, 12, 2,  0, 0, Fore.GREEN, "▒")
    brick7 = Brick(60, 10, 1, 12, 1,  0, 0, Fore.GREEN, "▒")
    brick8 = Brick(80, 10, 1, 12, 1,  0, 0, Fore.GREEN, "▒")
    brick9 = SpecialBrick(22, 20, 1, 12, 1, "unbreakable",
                          "$", 0, 0, Fore.GREEN, "█")
    brick10 = SpecialBrick(40, 20, 1, 12, 2, "unbreakable",
                           "@", 0, 0, Fore.WHITE, "█")

    # print(paddle.color + paddle.sprite + Fore.RESET)

    window.add(ball1)
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

    window.addPaddle(paddle)
    window.render()
