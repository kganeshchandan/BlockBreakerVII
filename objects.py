# from window import Window
import os
import sys
import time
from colorama import init
from colorama import Fore, Back, Style
from time import monotonic as clock, sleep
import config as config
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
    def __init__(self, x, y, height, width, vx=1, vy=1, color=Fore.WHITE, sprite="⬤", status="onpaddle"):
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
                self.x = self.x - self.pv

        else:
            self.x = self.x+self.vx
            self.y = self.y + self.vy


class Paddle(Entity):
    def __init__(self, x, y, height, width, color, sprite):
        super().__init__(x, y, height, width, color, sprite)


class Brick(Entity):
    def __init__(self, x, y, height, width, strength, vx=0, vy=0, color=Fore.WHITE, sprite=config.BRICK_SPRITE):
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
            self.height = 1
            self.width = 1

    def move(self, height):
        if self.y + self.height < height - 4:
            self.y = self.vy + self.y
        else:
            self.vy = 0
            # self.sprite = ' '

    # def collide(self, ball):
    #     new_x = ball.x + ball.vx
    #     new_y = ball.y + ball.vy

    #     if ((self.x <= new_x and self.x+self.width >= new_x) and (self.y <= new_y and self.y+self.height >= new_y)):

    #         if(self.strength != 0):
    #             # if(self.utility != "unbreakable"):
    #             if ball.strength == 1:
    #                 self.strength = self.strength - 1
    #             else:
    #                 self.strength = 0
    #                 ball.vy = -ball.vy

    #             self.display()
    #         # ball.vx = -ball.vx
    #             ball.vy = -ball.vy
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         return 0
    def willtouch(self, ball):
        new_x = ball.x + ball.vx
        new_y = ball.y + ball.vy
        dist = int((new_y - ball.y)/ball.vy)

        if new_x >= self.x and new_x <= self.x + self.width - 1 and new_y >= self.y and new_y <= self.y + self.height - 1:
            return True
        else:
            return False

    def collide(self, ball):
        new_x = ball.x + ball.vx
        new_y = ball.y + ball.vy

        if self.willtouch(ball):

            if(self.strength != 0):

                # if(self.utility != "unbreakable"):
                if ball.strength == 1:
                    self.strength = self.strength - 1
                    if ball.x < self.x or ball.x > self.x + self.width - 1:
                        ball.vx = -ball.vx
                    else:
                        ball.vy = -ball.vy
                else:
                    self.strength = 0

                self.display()
                return 1
            else:
                return 0
        else:
            return 0


class SpecialBrick(Brick):
    def __init__(self, x, y, height, width, strength, utility, utility_sprite, vx=0, vy=0, color=Fore.WHITE, sprite="▒"):
        super().__init__(x, y, height, width, strength,
                         vx=0, vy=0, color=Fore.WHITE, sprite="█")

        self.utility = utility
        self.utility_sprite = utility_sprite
        self.sprite = sprite
        self.ifbreak()

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

    def ifbreak(self):
        if (self.strength == 0 and self.utility != "explode"):
            self.color = Fore.WHITE
            self.sprite = self.utility_sprite
            self.vy = config.POWERUP_FALL
            self.x = int(self.x + self.width / 2)

            self.height = config.POWERUP_WIDTH
            self.width = config.POWERUP_WIDTH

    def willtouch(self, ball):
        new_x = ball.x + ball.vx
        new_y = ball.y + ball.vy
        dist = int((new_y - ball.y)/ball.vy)

        if new_x >= self.x and new_x <= self.x + self.width - 1 and new_y >= self.y and new_y <= self.y + self.height - 1:
            return True
        else:
            return False

    def collide(self, ball):
        new_x = ball.x + ball.vx
        new_y = ball.y + ball.vy

        if self.willtouch(ball):

            if(self.strength != 0):

                # if(self.utility != "unbreakable"):
                if ball.strength == 1:
                    if(self.utility != "unbreakable"):
                        self.strength = self.strength - 1
                    if ball.x < self.x or ball.x > self.x + self.width - 1:
                        ball.vx = -ball.vx
                    else:
                        ball.vy = -ball.vy
                else:
                    self.strength = 0
                # self.width = 1
                self.display()
                self.ifbreak()

                return 1
            else:
                return 0
        else:
            return 0
    # def powerup(self):
    #     self.y = self.y - 1
    # brick = Brick(10, 10, 1, 1, 3, 0, 0, "normal", "u", Fore.GREEN, "▒")
    # print(brick.color + brick.sprite + Fore.RESET)


class Power_up():
    def __init__(self, paddle, balls, utility, utility_sprite):
        self.utility = utility
        self.utility_sprite = utility_sprite
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
            self.paddle.width += config.POWERUP_EXPAND_PADDLE
            self.paddle.x -= int(config.POWERUP_EXPAND_PADDLE / 2)

        elif self.utility == "shrinkpaddle":
            self.paddle.width -= config.POWERUP_SHRINK_PADDLE
            self.paddle.x += int(config.POWERUP_SHRINK_PADDLE / 2)

        elif self.utility == "fireball":
            for ball in self.balls:
                ball.strength = -1
                ball.color = Fore.WHITE

        elif self.utility == "multiball":
            temp = []
            for ball in self.balls:
                vx = ball.vx
                vy = ball.vy
                newball = Ball(ball.x - ball.vx, ball.y + ball.vy + 1, 1, 1, -
                               ball.vx, 1, ball.color, "⬤", status="go")
                newball.strength = ball.strength

                temp.append(newball)
            for ball in temp:
                self.balls.append(ball)

        elif self.utility == "grab":
            for ball in self.balls:
                ball.color = Fore.RED

    def deactivate(self):
        if self.status:
            if not self.validate():
                if self.utility == "expandpaddle":
                    self.paddle.width -= config.POWERUP_EXPAND_PADDLE
                    for ball in self.balls:
                        if ball.status == "onpaddle":
                            ball.x = int(self.paddle.x + self.paddle.width / 2)
                    self.status = False

                elif self.utility == "shrinkpaddle":
                    self.paddle.width += config.POWERUP_SHRINK_PADDLE
                    self.paddle.x -= int(config.POWERUP_SHRINK_PADDLE / 2)
                    for ball in self.balls:
                        if ball.status == "onpaddle":
                            ball.x = int(self.paddle.x + self.paddle.width / 2)
                    self.status = False

                elif self.utility == "fireball":
                    for ball in self.balls:
                        ball.strength = 1
                        ball.color = Fore.MAGENTA
                    self.status = False
                elif self.utility == "multiball":
                    self.status = False

                elif self.utility == "grab":
                    for ball in self.balls:
                        ball.status = "go"
                        ball.color = Fore.MAGENTA

                    self.status = False

    def validate(self):
        if self.activation_time + config.POWER_UP_TIME < clock():
            return False
        else:
            return True
