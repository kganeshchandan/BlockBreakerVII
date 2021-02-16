import os
import sys
import time

from window import Window
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
    Ball_1 = Ball(5, 5, 1, 1, Fore.RED)
    Ball_2 = Ball(10, 25, -1, 1)
    paddle_1 = Paddle(1, 5)
    window.add(Ball_1)
    window.add(Ball_2)
    window.addPaddle(paddle_1)
    window.render()
