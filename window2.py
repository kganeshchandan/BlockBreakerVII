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
        self.bricks = []

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

                elif i == self.height - 4:
                    if j == 0:
                        self.Board[i][j] = a
                    elif j == self.width - 1:
                        self.Board[i][j] = a
                    else:
                        self.Board[i][j] = d
    # adding objects to the window

    def add(self, element):
        self.entities.append(element)

    def addPaddle(self, element):
        self.paddle = element

    def addBrick(self, element):
        self.bricks.append(element)

    # render the screen

    def handle_collisions(self, element):
        self.handle_paddlecollision(element)
        self.handle_bordercollision(element)

        self.handle_brickcollision(element)

    def handle_brickcollision(self, element):
        for brick in self.bricks:
            brick.collide(element)

    def handle_powercollision(self, element):
        pad_x = self.paddle.x
        pad_y = self.paddle.y
        wid_x = self.paddle.width

        if (element.y == pad_y and element.x >= pad_x and element.x <= pad_x + wid_x):
            element.vy = 0
            element.powerup()

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
                element.vy = -element.vy
            elif pad_x + 2*gap >= new_x:
                element.vx = -1
                element.vy = -element.vy
            elif pad_x + 3*gap >= new_x:
                element.vx = 1
                element.vy = -element.vy
            elif pad_x + 4*gap >= new_x:
                element.vx = 2
                element.vy = -element.vy

    def handle_bordercollision(self, element):
        if(element.y+element.vy >= self.height or element.y + element.vy <= 0):
            element.vy = -element.vy
        if(element.x + element.vx >= self.width or element.x + element.vx <= 0):
            element.vx = -element.vx

    def Make_Paddle(self):
        for i in range(self.paddle.width):
            self.Board[self.paddle.y][self.paddle.x+i] = self.paddle

    def showlevel(self):
        self.Board[self.height - 3][2] = Entity(1, 1, 1, 1, Fore.WHITE, "L")
        self.Board[self.height - 3][3] = Entity(1, 1, 1, 1, Fore.WHITE, "E")
        self.Board[self.height - 3][4] = Entity(1, 1, 1, 1, Fore.WHITE, "V")
        self.Board[self.height - 3][5] = Entity(1, 1, 1, 1, Fore.WHITE, "E")
        self.Board[self.height - 3][6] = Entity(1, 1, 1, 1, Fore.WHITE, "L")
        self.Board[self.height - 3][7] = Entity(1, 1, 1, 1, Fore.WHITE, ":")
        self.Board[self.height - 2][2] = Entity(1, 1, 1, 1, Fore.WHITE, "L")
        self.Board[self.height - 2][3] = Entity(1, 1, 1, 1, Fore.WHITE, "I")
        self.Board[self.height - 2][4] = Entity(1, 1, 1, 1, Fore.WHITE, "V")
        self.Board[self.height - 2][5] = Entity(1, 1, 1, 1, Fore.WHITE, "E")
        self.Board[self.height - 2][6] = Entity(1, 1, 1, 1, Fore.WHITE, "S")
        self.Board[self.height - 2][7] = Entity(1, 1, 1, 1, Fore.WHITE, ":")

    def render(self):
        frame = 0
        Key = KeyboardInput()
        while True:
            begin = time.monotonic()

            os.system("clear")

            self.makeborder()
            self.showlevel()

            # adding bricks
            for element in self.bricks:
                for k in range(element.height):
                    for i in range(element.width):
                        self.Board[element.y + k][element.x + i] = element
                        element.move(self.height)
                        self.handle_powercollision(element)

            # checking keyboard responses
            inp = Key.kbhit()
            if inp:
                # inp = Key.getch()
                # time.sleep(0.001)
                if inp == 'a' and self.paddle.x >= 2:
                    self.paddle.x = self.paddle.x - 2
                    self.Make_Paddle()
                    termios.tcflush(sys.stdin, termios.TCIOFLUSH)

                elif inp == 'd' and self.paddle.x <= self.width - self.paddle.width-2:
                    self.paddle.x = self.paddle.x + 2
                    self.Make_Paddle()
                    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
                else:
                    self.Make_Paddle()
                    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
                # inp = None
            else:
                self.Make_Paddle()
                termios.tcflush(sys.stdin, termios.TCIOFLUSH)
                inp = None

            # adding elements to the board
            for element in self.entities:
                self.handle_collisions(element)
                element.move(self.Board)

                self.Board[element.y][element.x] = element

            for i in range(self.height):
                for j in range(self.width):
                    if(self.Board[i][j] != None):
                        pixel = self.Board[i][j].color + \
                            self.Board[i][j].sprite + Fore.RESET
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
