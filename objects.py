# from window import Window
import os
import sys
import time
from colorama import init
from colorama import Fore, Back, Style
from time import monotonic as clock, sleep
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
    def __init__(self, x, y, height, width, vx=1, vy=1, color=Fore.WHITE, sprite=None, status="onpaddle"):
        super().__init__(x, y, height, width, color, sprite)
        self.vx = vx
        self.vy = vy
        self.status = status
        self.strength = 1
        self.pv = 1

    def move(self, Board, paddle):
        if self.status == "onpaddle":
            if self.x + self.pv < paddle.x - 1 + paddle.width and self.x + self.pv - 1 > paddle.x:

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
                if ball.strength == 1:
                    self.strength = self.strength - 1
                else:
                    self.strength = 0
                    ball.vy = -ball.vy

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
                if ball.strength == 1:
                    if(self.utility != "unbreakable"):
                        self.strength = self.strength - 1
                else:
                    self.strength = 0
                    ball.vy = -ball.vy

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


class Power_up():
    def __init__(self, paddle, balls, utility):
        self.utility = utility
        self.paddle = paddle
        self.balls = balls
        self.status = False
        self.activate()
        # self.deactivate()

    def activate(self):
        self.status = True
        self.activation_time = clock()
        # need to make sure new paddle is not out of border
        if self.utility == "expandpaddle":
            self.paddle.width += 8
            self.paddle.x -= 4
        elif self.utility == "shrinkpaddle":
            self.paddle.width -= 4
            self.paddle.x += 2
        elif self.utility == "fireball":
            for ball in self.balls:
                ball.strength = -1
                ball.color = Fore.WHITE
        elif self.utility == "multiball":
            temp = []
            for ball in self.balls:
                vx = ball.vx
                vy = ball.vy
                temp.append(Ball(ball.x - ball.vx, ball.y - ball.vy + 1, 1, 1, -
                                 ball.vx, 1, Fore.RED, "⬤", status="go"))
            for ball in temp:
                self.balls.append(ball)

    def deactivate(self):
        if self.status:
            if not self.validate():
                if self.utility == "expandpaddle":
                    self.paddle.width -= 8
                    for ball in self.balls:
                        if ball.status == "onpaddle":
                            ball.x = int(self.paddle.x + self.paddle.width / 2)
                    self.status = False

                elif self.utility == "shrinkpaddle":
                    self.paddle.width += 4
                    self.paddle.x -= 2
                    for ball in self.balls:
                        if ball.status == "onpaddle":
                            ball.x = int(self.paddle.x + self.paddle.width / 2)
                    self.status = False

                elif self.utility == "fireball":
                    for ball in self.balls:
                        ball.strength = 1
                        ball.color = Fore.MAGENTA
                    self.status = False

    def validate(self):
        if self.activation_time + 10 < clock():
            return False
        else:
            return True
