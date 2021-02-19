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
        self.status = "onpaddle"
        self.pv = 1

    def move(self, Board, paddle):
        if self.status == "onpaddle":
            if self.x + self.vx < paddle.x - 1 + paddle.width and self.x + self.vx - 2 > paddle.x:

                self.x = self.x + self.pv
            else:
                self.pv = -self.pv
                self.x = self.x + self.pv

        else:
            self.x = self.x+self.vx
            self.y = self.y + self.vy


class Paddle(Entity):
    def __init__(self, x, y, height, width, color, sprite):
        super().__init__(x, y, height, width, color, sprite)


class Brick(Entity):
    def __init__(self, x, y, height, width, strength, vx=0, vy=0, color=Fore.WHITE, sprite="▒"):
        super().__init__(x, y, height, width, color, sprite)

        self.strength = strength
        self.sprite = sprite
        self.display()
        self.vx = 0
        self.vy = 0

    def display(self):
        if (self.strength == 3):
            self.color = Fore.RED
        if (self.strength == 2):
            self.color = Fore.BLUE
        if (self.strength == 1):
            self.color = Fore.GREEN
        if (self.strength == 0):
            self.color = Fore.WHITE
            self.sprite = ' '

    def move(self, height):
        if self.y < height - 5:
            self.y = self.vy + self.y
        else:
            self.vy = 0
            self.sprite = ' '

    def collide(self, ball):
        new_x = ball.x + ball.vx
        new_y = ball.y + ball.vy

        if ((self.x <= new_x and self.x+self.width >= new_x) and (self.y <= new_y and self.y+self.height >= new_y)):

            if(self.strength != 0):
                # if(self.utility != "unbreakable"):
                self.strength = self.strength - 1
                self.display()
            # ball.vx = -ball.vx
                ball.vy = -ball.vy
                return 1
            else:
                return 0
        else:
            return 0


class SpecialBrick(Brick):
    def __init__(self, x, y, height, width, strength, utility, utility_sprite, vx=0, vy=0, color=Fore.WHITE, sprite="▒"):
        super().__init__(x, y, height, width, strength,
                         vx=0, vy=0, color=Fore.WHITE, sprite="▒")

        self.utility = utility
        self.utility_sprite = utility_sprite
        self.sprite = sprite
        self.ifbreak()

    def ifbreak(self):
        if (self.strength == 0):
            self.color = Fore.WHITE
            self.sprite = self.utility_sprite
            self.vy = 1
            self.width = 1

    def collide(self, ball):
        new_x = ball.x + ball.vx
        new_y = ball.y + ball.vy

        if ((self.x <= new_x and self.x+self.width >= new_x) and (self.y <= new_y and self.y+self.height >= new_y)):

            if(self.strength != 0):
                if(self.utility != "unbreakable"):
                    self.strength = self.strength - 1

                self.display()
                self.ifbreak()

            # ball.vx = -ball.vx
                ball.vy = -ball.vy
                return 1
            else:
                return 0
        else:
            return 0

    def powerup(self):
        self.y = self.y - 1
    # brick = Brick(10, 10, 1, 1, 3, 0, 0, "normal", "u", Fore.GREEN, "▒")
    # print(brick.color + brick.sprite + Fore.RESET)
