#theVANMAJESS_rgame
#Vanessa T. Biton , Jessa Mae Atutubo , Ma. Camille Ala


import random, sys, pygame, time, copy
from pygame.locals import *

FPS = 10 # frames per second to update the screen
WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
SPACESIZE = 50 # width & height of each space on the board, in pixels
BOARDWIDTH = 8 # how many columns of spaces on the game board
BOARDHEIGHT = 8 # how many rows of spaces on the game board
WHITE_TILE = 'WHITE_TILE' # an arbitrary but unique value
BLACK_TILE = 'BLACK_TILE' # an arbitrary but unique value
EMPTY_SPACE = 'EMPTY_SPACE' # an arbitrary but unique value
HINT_TILE = 'HINT_TILE' # an arbitrary but unique value
ANIMATIONSPEED = 25 # integer from 1 to 100, higher is faster animation

# Amount of space on the left & right side (XMARGIN) or above and below
# (YMARGIN) the game board, in pixels.
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)

#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
GREEN      = (  0, 155,   0)
BRIGHTBLUE = (  0,  50, 255)
BLUE     = (255)

TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE
HINTCOLOR = BLUE



def main():
    global MAINCLOCK, DISPLAYSURF, FONT, BIGFONT, BGIMAGE

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('theVANMAJESS_rgame')
    FONT = pygame.font.Font('freesansbold.ttf', 16)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 32)

    # Set up the background image.
    boardImage = pygame.image.load('bg5.png')
    # Use smoothscale() to stretch the board image to fit the entire board:
    boardImage = pygame.transform.smoothscale(boardImage, (BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE))
    boardImageRect = boardImage.get_rect()
    boardImageRect.topleft = (XMARGIN, YMARGIN)
    BGIMAGE = pygame.image.load('bg2.png')
    # Use smoothscale() to stretch the background image to fit the entire window:
    BGIMAGE = pygame.transform.smoothscale(BGIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
    BGIMAGE.blit(boardImage, boardImageRect)

    # Run the main game.
    while True:
        if runGame() == False:
            break
