import os
import sys
import time

from window2 import Window
from objects import Ball, Paddle
from colorama import init
from colorama import Fore, Back, Style

init()
FRAME_RATE = 0.07


if __name__ == "__main__":
    # # hide cursor
    # sys.stdout.write("\033[?25l")
    # sys.stdout.flush()

    # new game window
    window = Window()
    ball1 = Ball(10, 10, 1, 1, 1, 1, Fore.RED, "⬤")
    # print(ball1.color+ball1.sprite+Fore.RESET)
    paddle = Paddle(10, 40, 1, 15, Fore.GREEN, "▒")
    # print(paddle.color + paddle.sprite + Fore.RESET)

    window.add(ball1)

    window.addPaddle(paddle)
    window.render()
