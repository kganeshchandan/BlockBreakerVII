from window import Window
import os
import sys
import time
from colorama import init
from colorama import Fore, Back, Style

init()


class Ball:
    def __init__(self, x, y, vx=1, vy=1, colour=Fore.WHITE):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = colour + "⬤\u001b[0m"

    def draw(self):
        print("\n" * self.y, " " * self.x, self.color)


class Paddle:
    def __init__(self, x, l=4):
        self.x = x
        self.len = l
        self.pad = "="
        # for i in range(l-1):
        #     self.len = self.len + "="
