# from window import Window
import os
import sys
import time
from colorama import init
from colorama import Fore, Back, Style

init()


class Entity:
    def __init__(self, x, y, height, width, color=Fore.WHITE, sprite=None):
        self.x = x
        self.y = y
        self.color = color
        self.sprite = sprite
        self.height = height
        self.width = width


class Ball(Entity):
    def __init__(self, x, y, height, width, vx=1, vy=1, color=Fore.WHITE, sprite=None):
        super().__init__(x, y, height, width, color, sprite)
        self.vx = vx
        self.vy = vy

    def move(self, Board):
        self.x = self.x+self.vx
        self.y = self.y + self.vy


class Paddle(Entity):
    def __init__(self, x, y, height, width, color, sprite):
        super().__init__(x, y, height, width, color, sprite)

    def move(self, Board):
        pass
