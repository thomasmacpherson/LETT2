# Ink Spill (a Flood It clone)
# http://inventwithpython.com/pygame
# By Al Sweigart al@inventwithpython.com
# Released under a "Simplified BSD" license

import random, sys, webbrowser, copy, pygame
from pygame.locals import *

# There are different box sizes, number of boxes, and
# life depending on the "board size" setting selected.
SMALLBOXSIZE  = 60 # size is in pixels
MEDIUMBOXSIZE = 20
LARGEBOXSIZE  = 11

SMALLBOARDSIZE  = 6 # size is in boxes
MEDIUMBOARDSIZE = 17
LARGEBOARDSIZE  = 30

SMALLMAXLIFE  = 10 # number of turns
MEDIUMMAXLIFE = 30
LARGEMAXLIFE  = 64



EASY = 0   # arbitrary but unique value
MEDIUM = 1 # arbitrary but unique value
HARD = 2   # arbitrary but unique value

difficulty = MEDIUM # game starts in "medium" mode
maxLife = MEDIUMMAXLIFE
boardWidth = MEDIUMBOARDSIZE
boardHeight = MEDIUMBOARDSIZE


#            R    G    B
WHITE    = (255, 255, 255)
DARKGRAY = ( 70,  70,  70)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)

# The first color in each scheme is the background color, the next six are the palette colors.
COLORSCHEMES = (((150, 200, 255), RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE),
                ((0, 155, 104),  (97, 215, 164),  (228, 0, 69),  (0, 125, 50),   (204, 246, 0),   (148, 0, 45),    (241, 109, 149)),
                ((195, 179, 0),  (255, 239, 115), (255, 226, 0), (147, 3, 167),  (24, 38, 176),   (166, 147, 0),   (197, 97, 211)),
                ((85, 0, 0),     (155, 39, 102),  (0, 201, 13),  (255, 118, 0),  (206, 0, 113),   (0, 130, 9),     (255, 180, 115)),
                ((191, 159, 64), (183, 182, 208), (4, 31, 183),  (167, 184, 45), (122, 128, 212), (37, 204, 7),    (88, 155, 213)),
                ((200, 33, 205), (116, 252, 185), (68, 56, 56),  (52, 238, 83),  (23, 149, 195),  (222, 157, 227), (212, 86, 185)))
for i in range(len(COLORSCHEMES)):
    assert len(COLORSCHEMES[i]) == 7, 'Color scheme %s does not have exactly 7 colors.' % (i)
bgColor = COLORSCHEMES[0][0]
paletteColors =  COLORSCHEMES[0][1:]

def main():

    mainBoard = generateRandomBoard(boardWidth, boardHeight, difficulty)
    life = maxLife
    lastPaletteClicked = None

    while True: # main game loop


        if paletteClicked != None and paletteClicked != lastPaletteClicked:
            # a palette button was clicked that is different from the
            # last palette button clicked (this check prevents the player
            # from accidentally clicking the same palette twice)
            lastPaletteClicked = paletteClicked
            floodAnimation(mainBoard, paletteClicked)
            life -= 1

            resetGame = False
            if hasWon(mainBoard):
		   		printLCD(2, 1, "You Win", 0)
                resetGame = True
                pygame.time.wait(2000) # pause so the player can bask in victory
                
            elif life == 0:
		   		printLCD(2, 1, "You lose", 0)
                pygame.time.wait(400)

                resetGame = True
                pygame.time.wait(2000) # pause so the player can suffer in their defeat

        if resetGame:
            # start a new game
            mainBoard = generateRandomBoard(boardWidth, boardHeight, difficulty)
            life = maxLife
            lastPaletteClicked = None



def hasWon(board):
    # if the entire board is the same color, player has won
    for x in range(boardWidth):
        for y in range(boardHeight):
            if board[x][y] != board[0][0]:
                return False # found a different color, player has not won
    return True



def drawColorSchemeBoxes(x, y, schemeNum):
    # Draws the color scheme boxes that appear on the "Settings" screen.
    for boxy in range(2):
        for boxx in range(3):
            pygame.draw.rect(DISPLAYSURF, COLORSCHEMES[schemeNum][3 * boxy + boxx + 1], (x + MEDIUMBOXSIZE * boxx, y + MEDIUMBOXSIZE * boxy, MEDIUMBOXSIZE, MEDIUMBOXSIZE))
            if paletteColors == COLORSCHEMES[schemeNum][1:]:
                # put the ink spot next to the selected color scheme
                DISPLAYSURF.blit(SPOTIMAGE, (x - 50, y))


def flashBorderAnimation(color, board, animationSpeed=30):
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    for start, end, step in ((0, 256, 1), (255, 0, -1)):
        # the first iteration on the outer loop will set the inner loop
        # to have transparency go from 0 to 255, the second iteration will
        # have it go from 255 to 0. This is the "flash".
        for transparency in range(start, end, animationSpeed * step):
            DISPLAYSURF.blit(origSurf, (0, 0))
            r, g, b = color
            flashSurf.fill((r, g, b, transparency))
            DISPLAYSURF.blit(flashSurf, (0, 0))
            drawBoard(board) # draw board ON TOP OF the transparency layer
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0)) # redraw the original surface




def floodAnimation(board, paletteClicked, animationSpeed=25):
    origBoard = copy.deepcopy(board)
    floodFill(board, board[0][0], paletteClicked, 0, 0)

    for transparency in range(0, 255, animationSpeed):
        # The "new" board slowly become opaque over the original board.
        drawBoard(origBoard)
        drawBoard(board, transparency)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateRandomBoard(width, height, difficulty=MEDIUM):
    # Creates a board data structure with random colors for each box.
    board = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(random.randint(0, len(paletteColors) - 1))
        board.append(column)

    # Make board easier by setting some boxes to same color as a neighbor.

    # Determine how many boxes to change.
    if difficulty == EASY:
        if boxSize == SMALLBOXSIZE:
            boxesToChange = 100
        else:
            boxesToChange = 1500
    elif difficulty == MEDIUM:
        if boxSize == SMALLBOXSIZE:
            boxesToChange = 5
        else:
            boxesToChange = 200
    else:
        boxesToChange = 0

    # Change neighbor's colors:
    for i in range(boxesToChange):
        # Randomly choose a box whose color to copy
        x = random.randint(1, width-2)
        y = random.randint(1, height-2)

        # Randomly choose neighbors to change.
        direction = random.randint(0, 3)
        if direction == 0: # change left and up neighbor
            board[x-1][y] == board[x][y]
            board[x][y-1] == board[x][y]
        elif direction == 1: # change right and down neighbor
            board[x+1][y] == board[x][y]
            board[x][y+1] == board[x][y]
        elif direction == 2: # change right and up neighbor
            board[x][y-1] == board[x][y]
            board[x+1][y] == board[x][y]
        else: # change left and down neighbor
            board[x][y+1] == board[x][y]
            board[x-1][y] == board[x][y]
    return board






def getColorOfPaletteAt(x, y):
    # Returns the index of the color in paletteColors that the x and y parameters
    # are over. Returns None if x and y are not over any palette.
    numColors = len(paletteColors)
    xmargin = int((WINDOWWIDTH - ((PALETTESIZE * numColors) + (PALETTEGAPSIZE * (numColors - 1)))) / 2)
    top = WINDOWHEIGHT - PALETTESIZE - 10
    for i in range(numColors):
        # Find out if the mouse click is inside any of the palettes.
        left = xmargin + (i * PALETTESIZE) + (i * PALETTEGAPSIZE)
        r = pygame.Rect(left, top, PALETTESIZE, PALETTESIZE)
        if r.collidepoint(x, y):
            return i
    return None # no palette exists at these x, y coordinates



def floodFill(board, oldColor, newColor, x, y):
    # This is the flood fill algorithm.
    if oldColor == newColor or board[x][y] != oldColor:
        return

    board[x][y] = newColor # change the color of the current box

    # Make the recursive call for any neighboring boxes:
    if x > 0:
        floodFill(board, oldColor, newColor, x - 1, y) # on box to the left
    if x < boardWidth - 1:
        floodFill(board, oldColor, newColor, x + 1, y) # on box to the right
    if y > 0:
        floodFill(board, oldColor, newColor, x, y - 1) # on box to up
    if y < boardHeight - 1:
        floodFill(board, oldColor, newColor, x, y + 1) # on box to down


def leftTopPixelCoordOfBox(boxx, boxy):
    # Returns the x and y of the left-topmost pixel of the xth & yth box.
    xmargin = int((WINDOWWIDTH - (boardWidth * boxSize)) / 2)
    ymargin = int((WINDOWHEIGHT - (boardHeight * boxSize)) / 2)
    return (boxx * boxSize + xmargin, boxy * boxSize + ymargin)


if __name__ == '__main__':
    main()
