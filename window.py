import os
import sys
import time
from colorama import init
from colorama import Fore, Back, Style

init()
FRAME_RATE = 0.07


class Window:
    def __init__(self):
        size = os.get_terminal_size()
        self.height = size.lines - 1
        self.width = size.columns
        self.balls = []
        self.paddle = None

    # create the border for the window
    def makeborder(self):
        self.Board = [[' ' for j in range(self.width)]
                      for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                if j == 0 or j == self.width - 1:
                    self.Board[i][j] = "┃"

                if i == 0:
                    if j == 0:
                        self.Board[i][j] = "┏"
                    elif j == self.width - 1:
                        self.Board[i][j] = "┓"
                    else:
                        self.Board[i][j] = "━"

                if i == self.height - 1:
                    if j == 0:
                        self.Board[i][j] = "┗"
                    elif j == self.width - 1:
                        self.Board[i][j] = "┛"
                    else:
                        self.Board[i][j] = "━"

    # adding objects to the window
    def add(self, element):
        self.balls.append(element)

    def addPaddle(self, element):
        self.paddle = element
    # moving ball within the window

    def move(self, element):
        if(self.Board[element.y + element.vy][element.x] == ' '):
            element.y = element.y + element.vy
        else:
            element.vy = -element.vy
        if(self.Board[element.y][element.x + element.vx] == ' '):
            element.x = element.x + element.vx
        else:
            element.vx = -element.vx

    # render the screen
    def render(self):
        while True:
            begin = time.monotonic()
            os.system("clear")

            self.makeborder()

            for element in self.balls:
                self.Board[element.y][element.x] = element.color
                self.move(element)

            for i in range(self.paddle.len):
                self.Board[self.height-5][self.paddle.x] = self.paddle.pad

            for i in range(self.height):
                for j in range(self.width):
                    pixel = self.Board[i][j]
                    print(pixel, sep="", end="")
                print()

            while time.monotonic() - begin < FRAME_RATE:
                pass
