import os
import sys
import time
import getch
import termios
from colorama import init
from colorama import Fore, Back, Style
from objects import Entity
from input import KeyboardInput
from objects import Power_up
init()
FRAME_RATE = 0.07


class Window:
    def __init__(self, level, lives, score):
        size = os.get_terminal_size()
        self.height = size.lines - 1
        self.width = size.columns
        self.entities = []
        self.paddle = None
        self.bricks = []
        self.level = level
        self.brick_no = 0
        self.lives = lives
        self.score = score
        self.powerups = []
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

    def checkBricks(self):
        self.brick_no = 0
        for brick in self.bricks:
            try:
                if(brick.utility != "unbreakable" and brick.strength > 0):
                    self.brick_no += 1
            except:
                if brick.strength > 0:
                    self.brick_no += 1

        return self.brick_no

    def add(self, element):
        self.entities.append(element)

    def addPaddle(self, element):
        self.paddle = element

    def addBrick(self, element):
        self.bricks.append(element)

    def handle_collisions(self, element):
        self.handle_paddlecollision(element)
        self.handle_bordercollision(element)
        self.handle_brickcollision(element)

    def handle_brickcollision(self, element):
        for brick in self.bricks:
            self.score += brick.collide(element)

    def grab(self):
        pad_x = self.paddle.x
        pad_y = self.paddle.y
        wid_x = self.paddle.width
        gap = wid_x/4

        for element in self.entities:
            new_x = element.x + element.vx
            new_y = element.y + element.vy

            if((new_x >= pad_x and new_x <= pad_x + wid_x) and (new_y == pad_y - 1)):
                element.status = "onpaddle"
                element.x = self.paddle.x + int(self.paddle.width / 2)
                element.y = self.paddle.y - 1
                element.color = Fore.RED

    def checkpowerups(self):
        for powerup in self.powerups:
            powerup.deactivate()
            if powerup.utility == "grab" and powerup.status == True:
                self.grab()

    def handle_powercollision(self, element):
        pad_x = self.paddle.x
        pad_y = self.paddle.y
        wid_x = self.paddle.width

        if (element.y == pad_y and element.x >= pad_x and element.x <= pad_x + wid_x):
            element.vy = 0
            element.powerup()
            self.powerups.append(
                Power_up(self.paddle, self.entities, element.utility))

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
        self.Board[self.height -
                   3][8] = Entity(1, 1, 1, 1, Fore.WHITE, str(self.level))

        self.Board[self.height - 2][2] = Entity(1, 1, 1, 1, Fore.WHITE, "L")
        self.Board[self.height - 2][3] = Entity(1, 1, 1, 1, Fore.WHITE, "I")
        self.Board[self.height - 2][4] = Entity(1, 1, 1, 1, Fore.WHITE, "V")
        self.Board[self.height - 2][5] = Entity(1, 1, 1, 1, Fore.WHITE, "E")
        self.Board[self.height - 2][6] = Entity(1, 1, 1, 1, Fore.WHITE, "S")
        self.Board[self.height - 2][7] = Entity(1, 1, 1, 1, Fore.WHITE, ":")
        self.Board[self.height -
                   2][8] = Entity(1, 1, 1, 1, Fore.WHITE, str(self.lives))

        self.Board[self.height - 2][self.width -
                                    10] = Entity(1, 1, 1, 1, Fore.WHITE, "S")
        self.Board[self.height - 2][self.width -
                                    9] = Entity(1, 1, 1, 1, Fore.WHITE, "C")
        self.Board[self.height - 2][self.width -
                                    8] = Entity(1, 1, 1, 1, Fore.WHITE, "O")
        self.Board[self.height - 2][self.width -
                                    7] = Entity(1, 1, 1, 1, Fore.WHITE, "R")
        self.Board[self.height - 2][self.width -
                                    6] = Entity(1, 1, 1, 1, Fore.WHITE, "E")
        self.Board[self.height - 2][self.width -
                                    5] = Entity(1, 1, 1, 1, Fore.WHITE, ":")
        self.Board[self.height -
                   2][self.width-4] = Entity(1, 1, 1, 1, Fore.WHITE, str(int(self.score/100)))
        self.Board[self.height -
                   2][self.width-3] = Entity(1, 1, 1, 1, Fore.WHITE, str(int(self.score/10)))
        self.Board[self.height -
                   2][self.width-2] = Entity(1, 1, 1, 1, Fore.WHITE, str(int(self.score % 10)))

        self.Board[self.height - 3][self.width -
                                    5] = Entity(1, 1, 1, 1, Fore.WHITE, str(len(self.entities)))

    def movepaddle(self, inp):
        if inp:
            if inp == 'w':
                self.entities[0].status = "go"
            if inp == 'a' and self.paddle.x >= 2:
                self.paddle.x = self.paddle.x - 2
                if self.entities[0].status == "onpaddle":
                    self.entities[0].x -= 2
                self.Make_Paddle()
                termios.tcflush(sys.stdin, termios.TCIOFLUSH)

            elif inp == 'd' and self.paddle.x <= self.width - self.paddle.width-2:
                self.paddle.x = self.paddle.x + 2
                if self.entities[0].status == "onpaddle":
                    self.entities[0].x += 2
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

    def renderBricks(self):
        for element in self.bricks:
            for k in range(element.height):
                for i in range(element.width):
                    self.Board[element.y + k][element.x + i] = element
                    element.move(self.height)
                    self.handle_powercollision(element)

    def renderBalls(self):
        for element in self.entities:
            self.handle_collisions(element)
            element.move(self.Board, self.paddle)
            self.Board[element.y][element.x] = element

    def renderBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                if(self.Board[i][j] != None):
                    pixel = self.Board[i][j].color + \
                        self.Board[i][j].sprite + Fore.RESET
                    self.PrintBoard[i][j] = pixel
                else:
                    pixel = ' '
                    self.PrintBoard[i][j] = pixel
        for i in range(self.height):
            print(*self.PrintBoard[i], sep="")

    def render(self):
        Key = KeyboardInput()
        while True:
            begin = time.monotonic()

            os.system("clear")
            # makeborder
            self.makeborder()

            # show level lives and score
            self.showlevel()

            # checkpowerups
            self.checkpowerups()

            # adding bricks
            self.renderBricks()

            # checking keyboard responses
            inp = Key.kbhit()
            self.movepaddle(inp)
            inp = None

            # adding Balls to the board
            self.renderBalls()

            # rendering the board
            self.renderBoard()

            for ball in self.entities:
                if len(self.entities) == 1:
                    if ball.y > self.paddle.y:
                        ball.status = "onpaddle"
                        ball.x = self.paddle.x + int(self.paddle.width / 2)
                        ball.y = self.paddle.y - 1
                        self.lives -= 1
                    if self.lives == 0:
                        return self.level, self.lives, self.score
                else:
                    if ball.y > self.paddle.y:
                        self.entities.remove(ball)

            if self.checkBricks() == 0:
                return self.level + 1, self.lives, self.score

            while time.monotonic() - begin < FRAME_RATE:
                pass
