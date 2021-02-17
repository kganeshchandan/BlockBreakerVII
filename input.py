import os
import sys
import time
import getch
import termios
from colorama import init
from colorama import Fore, Back, Style
from objects import Entity
import atexit
from select import select


class KeyboardInput():
    def __init__(self):
        self._fd = sys.stdin.fileno()
        self._new_term = termios.tcgetattr(self._fd)
        self._old_term = termios.tcgetattr(self._fd)

        # New terminal setting unbuffered
        self._new_term[3] = (self._new_term[3] & ~
                             termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self._fd, termios.TCSAFLUSH, self._new_term)

        # Support normal-terminal reset at exit
        atexit.register(self.set_normal_term)

    def set_normal_term(self):
        termios.tcsetattr(self._fd, termios.TCSAFLUSH, self._old_term)

    def getch(self):
        return sys.stdin.read(1)

    def kbhit(self):

        dr, dw, de = select([sys.stdin], [], [], 0)
        # self.flush()
        return dr != []

    def flush(self):
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
