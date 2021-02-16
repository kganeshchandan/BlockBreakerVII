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
        self.Board = [[' ' for j in range(self.width)]
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
                    self.Board[i][j] = '┃'

                if i == 0:
                    if j == 0:
                        self.Board[i][j] = '┏'
                    elif j == self.width - 1:
                        self.Board[i][j] = '┓'
                    else:
                        self.Board[i][j] = '━'

                if i == self.height - 1:
                    if j == 0:
                        self.Board[i][j] = '┗'
                    elif j == self.width - 1:
                        self.Board[i][j] = '┛'
                    else:
                        self.Board[i][j] = '━'

    # adding objects to the window
    def add(self, element):
        self.entities.append(element)

    def addPaddle(self, element):
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

    def render(self):
        while True:
            begin = time.monotonic()
            os.system("clear")

            self.makeborder()

            for i in range(self.paddle.width):
                self.Board[self.paddle.y][self.paddle.x+i] = self.paddle.sprite

            # adding elements to the board
            for element in self.entities:
                self.Board[element.y][element.x] = element.sprite
                # element.move(self.Board)

            for i in range(self.height):
                for j in range(self.width):
                    if(self.Board[i][j] != None):
                        # if (self.Board[i][j].width == 1):
                        pixel = self.Board[i][j]
                        print(pixel, sep="", end="")

                        # j = j+self.Board[i][j].width + 1

                    else:
                        pixel = ' '
                        print(pixel, sep="", end="")
                print()

            while time.monotonic() - begin < FRAME_RATE:
                pass
