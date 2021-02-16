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

    # def move(self, Board):
    #     if (self.x+self.vx < len(Board[self.y]) and self.x+self.vx >= 0):
    #         if(Board[self.y][self.x + self.vx] == ' '):
    #             self.x = self.x+self.vx
    #         else:
    #             self.vx = -self.vx
    #     else:
    #         self.vx = -self.vx
    #     if (self.x < len(Board) and self.x >= 0):
    #         if(Board[self.y + self.vy][self.x] == ' '):
    #             self.y = self.y+self.vy
    #         else:
    #             self.vy = -self.vy
    #     else:
    #         self.vy = -self.vy


class Paddle(Entity):
    def __init__(self, x, y, height, width, color, sprite):
        super().__init__(x, y, height, width, color, sprite)

        # for i in range(l-1):
        #     self.len = self.len + "="
# a = Entity("|", Fore.GREEN)
# ball1 = Ball(10, 10, 1, 1, 1, 1, Fore.RED, "⬤")
# print(ball1.color+ball1.sprite+Fore.RESET)
# paddle = Paddle(10, 10, 1, 1, Fore.GREEN, "▒")
# print(paddle.color + paddle.sprite + Fore.RESET)
