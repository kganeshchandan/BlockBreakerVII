import os
import sys
import time
import getch
import termios
from colorama import init
from colorama import Fore, Back, Style
from objects import Entity
from input import KeyboardInput
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
        self.PrintBoard = [[None for j in range(self.width)]
                           for i in range(self.height)]
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

    def handle_bordercollision(self, element):
        if(element.y+element.vy >= self.height or element.y + element.vy <= 0):
            element.vy = -element.vy
        if(element.x + element.vx >= self.width or element.x + element.vx <= 0):
            element.vx = -element.vx

    def Make_Paddle(self):
        for i in range(self.paddle.width):
            self.Board[self.paddle.y][self.paddle.x+i] = self.paddle

    def render(self):
        frame = 0
        Key = KeyboardInput()
        while True:
            begin = time.monotonic()
            # frame += 1

            # if frame > 2500000:
            #     frame = 0
            # temp = input("proceed :")

            os.system("clear")

            self.makeborder()

            # checking keyboard responses

            if Key.kbhit():
                inp = Key.getch()
                termios.tcflush(sys.stdin, termios.TCIOFLUSH)
                if inp == 'a' and self.paddle.x >= 1:
                    self.paddle.x = self.paddle.x - 1

                elif inp == 'd' and self.paddle.x <= self.width - self.paddle.width-1:
                    self.paddle.x = self.paddle.x + 1
                Key.flush()
            # making paddle
            self.Make_Paddle()

            # adding elements to the board
            for element in self.entities:
                self.Board[element.y][element.x] = element
                element.move(self.Board)
                self.handle_collisions(element)

            for i in range(self.height):
                for j in range(self.width):
                    if(self.Board[i][j] != None):
                        pixel = self.Board[i][j].sprite
                        self.PrintBoard[i][j] = pixel
                        # print(pixel, sep="", end="")
                    else:
                        pixel = ' '
                        self.PrintBoard[i][j] = pixel
                        # print(pixel, sep="", end="")

            # Printing on screen
            for i in range(self.height):
                print(*self.PrintBoard[i], sep="")

            while time.monotonic() - begin < FRAME_RATE:
                pass
