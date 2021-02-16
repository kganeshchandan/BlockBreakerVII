import os
import sys
import time
from colorama import init
from colorama import Fore, Back, Style
from objects import Entity
init()
FRAME_RATE = 0.07


class Window:
    def __init__(self):
        size = os.get_terminal_size()
        self.height = size.lines - 1
        self.width = size.columns
        self.entities = []
        self.paddle = None

    # create the border for the window
    def makeborder(self):
        self.Board = [[None for j in range(self.width)]
                      for i in range(self.height)]

        a = Entity(1, 1, 1, 1, Fore.WHITE, '┃')
        b = Entity(1, 1, 1, 1, Fore.WHITE, '┏')
        c = Entity(1, 1, 1, 1, Fore.WHITE, '┓')
        d = Entity(1, 1, 1, 1, Fore.WHITE, '━')
        e = Entity(1, 1, 1, 1, Fore.WHITE, '┗')
        f = Entity(1, 1, 1, 1, Fore.WHITE, '┛')

        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width - 1:
                    self.Board[i][j] = a

                if i == 0:
                    if j == 0:
                        self.Board[i][j] = b
                    elif j == self.width - 1:
                        self.Board[i][j] = c
                    else:
                        self.Board[i][j] = d

                if i == self.height - 1:
                    if j == 0:
                        self.Board[i][j] = e
                    elif j == self.width - 1:
                        self.Board[i][j] = f
                    else:
                        self.Board[i][j] = d

    # adding objects to the window
    def add(self, element):
        self.entities.append(element)

    def addPaddle(self, element):
        # self.entities.append(element)

        self.paddle = element
    # moving ball within the window

    # def move(self, element, paddle):
    #     if(self.Board[element.y + element.vy][element.x] == ' '):
    #         element.y = element.y + element.vy
    #     else:
    #         element.vy = -element.vy
    #     if(self.Board[element.y][element.x + element.vx] == ' '):
    #         element.x = element.x + element.vx
    #     else:

    #         element.vx = -element.vx

    # render the screen
    def handle_collisions(self, element):
        self.handle_bordercollision(element)
        self.handle_paddlecollision(element)

    def handle_paddlecollision(self, element):
        pad_x = self.paddle.x
        pad_y = self.paddle.y
        wid_x = self.paddle.width
        gap = wid_x/4

        new_x = element.x + element.vx
        new_y = element.y + element.vy

        if((new_x >= pad_x and new_x <= pad_x + wid_x) and (new_y == pad_y)):
            if pad_x + gap >= new_x:
                element.vx = -2
                element.vy = -1
            elif pad_x + 2*gap >= new_x:
                element.vx = -1
                element.vy = -1
            elif pad_x + 3*gap >= new_x:
                element.vx = 1
                element.vy = -1
            elif pad_x + 4*gap >= new_x:
                element.vx = 2
                element.vy = -1
            # if pad_x + gap >= new_x:
            #     element.vx = -2*abs(element.vx)
            #     element.vy = -(element.vy)
            # elif pad_x + 2*gap >= new_x:
            #     element.vx = -abs(element.vx)
            #     element.vy = -(element.vy)
            # elif pad_x + 3*gap >= new_x:
            #     element.vx = abs(element.vx)
            #     element.vy = -(element.vy)
            # elif pad_x + 4*gap >= new_x:
            #     element.vx = 2*abs(element.vx)
            #     element.vy = -(element.vy)

    def handle_bordercollision(self, element):
        if(element.y+element.vy >= self.height or element.y + element.vy <= 0):
            element.vy = -element.vy
        if(element.x + element.vx >= self.width or element.x + element.vx <= 0):
            element.vx = -element.vx

    def render(self):
        while True:
            begin = time.monotonic()
            os.system("clear")

            self.makeborder()

            for i in range(self.paddle.width):
                self.Board[self.paddle.y][self.paddle.x+i] = self.paddle

            # adding elements to the board
            for element in self.entities:
                self.Board[element.y][element.x] = element
                element.move(self.Board)
                self.handle_collisions(element)

            for i in range(self.height):
                for j in range(self.width):

                    if(self.Board[i][j] != None):
                        pixel = self.Board[i][j].sprite

                        print(pixel, sep="", end="")

                    else:
                        pixel = ' '
                        print(pixel, sep="", end="")

                print()

            while time.monotonic() - begin < FRAME_RATE:
                pass
