'''
this file contains all relevant game constants
'''

# probabilities heavily depend on frame rate

from colorama import Fore, Back, Style

LIVES = 6

# window constants
FRAME_RATE = 0.1

# ball constants
BALL_VX = 1
BALL_VY = 1
BALL_SPRITE = "⬤"
BALL_COLOR = Fore.MAGENTA

# paddle constants
PADDLE_X = 40
PADDLE_Y = 40
PADDLE_V = 2
PADDLE_WIDTH = 24
PADDLE_SPRITE = "▒"
PADDLE_COLOR = Fore.WHITE

# objects constants

# power up
POWER_UP_TIME = 10
POWERUP_FALL = 1
POWERUP_WIDTH = 1
POWERUP_EXPAND_PADDLE = 8
POWERUP_SHRINK_PADDLE = 4

BRICK_SPRITE = "▒"
BRICK_WIDTH = 10
BRICK_HEIGHT = 1
BRICK_FALL_TIME = 10
