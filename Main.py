import os
import sys
import time

from window2 import Window
from objects import Ball, Paddle, Brick
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
    ball1 = Ball(70, 30, 1, 1, 1, 1, Fore.WHITE, "⬤")
    # print(ball1.color+ball1.sprite+Fore.RESET)
    paddle = Paddle(40, 40, 1, 24, Fore.WHITE, "▓")

    brick1 = Brick(10, 10, 2, 12, 3, "normal", "+", 0, 0, Fore.GREEN, "▒")
    brick2 = Brick(30, 10, 1, 12, 2, "normal", "*", 0, 0, Fore.GREEN, "▒")
    brick3 = Brick(50, 10, 1, 12, 1, "normal", "!", 0, 0, Fore.GREEN, "▒")
    brick4 = Brick(70, 10, 1, 12, 1, "normal", "#", 0, 0, Fore.GREEN, "▒")
    brick5 = Brick(20, 20, 1, 12, 3, "normal", "%", 0, 0, Fore.GREEN, "▒")
    brick6 = Brick(40, 20, 1, 12, 2, "normal", "&", 0, 0, Fore.GREEN, "▒")
    brick7 = Brick(60, 25, 1, 12, 1, "normal", "@", 0, 0, Fore.GREEN, "▒")
    brick8 = Brick(80, 25, 1, 12, 1, "normal", "$", 0, 0, Fore.GREEN, "▒")
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

    window.addPaddle(paddle)
    window.render()
