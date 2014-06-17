# Ink Spill (a Flood It clone)
# http://inventwithpython.com/pygame
# By Al Sweigart al@inventwithpython.com
# Released under a "Simplified BSD" license

import random, sys, webbrowser, copy, pygame, time
from pygame.locals import *



EASY = 0   # arbitrary but unique value
MEDIUM = 1 # arbitrary but unique value
HARD = 2   # arbitrary but unique value

difficulty = MEDIUM # game starts in "medium" mode
maxLife = 35
boardWidth = 16
boardHeight = 16

colourCount = 6

#            R    G    B

RED      = (0,200,200)
GREEN    = (0,0,200)
BLUE     = (200,0,0)
YELLOW   = (0,200,0)
ORANGE   = (200,200,0)
PURPLE   = (255, 80,   0)

colours = []
colours.append(RED)
colours.append(GREEN)
colours.append(BLUE)
colours.append(YELLOW)
colours.append(ORANGE)
colours.append(PURPLE)
import const


spriteArray = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]
spriteArray[0][0] = 1

class thisapp():




    def hasWon(self, board):
        # if the entire board is the same color, player has won
        for x in reversed(range(boardWidth)):
            for y in reversed(range(boardHeight)):
                if board[x][y] != board[0][0]:
                    return False # found a different color, player has not won
        return True





    def flashBorderAnimation(self, color, board, animationSpeed=30):
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



    def generateRandomBoard(self, width, height, difficulty=MEDIUM):
        # Creates a board data structure with random colors for each box.
        board = []
        for x in range(width):
            column = []
            for y in range(height):
                column.append(random.randint(0, colourCount - 1))
            board.append(column)

        # Make board easier by setting some boxes to same color as a neighbor.

        # Determine how many boxes to change.
        if difficulty == EASY:
            boxesToChange = 100

        elif difficulty == MEDIUM:
            boxesToChange = 50

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


    def floodFill(self, board, oldColor, newColor, x, y, visited, added, spriteArray):
        # This is the flood fill algorithm.
        #print ""
        #print "Checking ", x, " ", y

        # if pixel already been visited, don't do anything
        if visited[x][y] == 1:
            #print "Already Visited"
            return

        visited[x][y] = 1
       
        #print "New colour ", newColor
        #print "Old colour ", oldColor
        #print "Pixel colour", board[y][x] 
        if board[y][x] == newColor:
            i = x/8
            j= (y/8)*2
            self.api.addToSprite(i+j,0,8,x%8,y%8,[0b11111111])
            added = True
            #print "Added " , x , " " , y, " to sprite"        
            # add to sprite array
            spriteArray[y][x] = 1

        # if board not new colour, and not part of sprite, don't check neighbours
        elif spriteArray[y][x] == 0:
            #print "Returning"
            return
        
	# board needs to be set to new color
        #print "Updated to new colour"
        board[y][x] = newColor # change the color of the current box
        
        # display checked pixels in white
        #self.api.setInk(255,255,255,4)        
        #self.api.drawPixel(x,y)

        # Make the recursive call for any neighboring boxes: 
        if x > 0:
            self.floodFill(board, oldColor, newColor, x - 1, y, visited, added, spriteArray) # on box to the left
        if x < boardWidth - 1:
            self.floodFill(board, oldColor, newColor, x + 1, y, visited, added, spriteArray) # on box to the right
        if y > 0:
            self.floodFill(board, oldColor, newColor, x, y - 1, visited, added, spriteArray) # on box to up
        if y < boardHeight - 1:
            self.floodFill(board, oldColor, newColor, x, y + 1, visited, added, spriteArray) # on box to down

    def newGame(self, api):
        
        print "INKSPILL initialised"
        self.api = api
        self.api.writeToLCD(2, 0, "Inkspill")
        self.api.clearScreen(4)


        self.mainBoard = self.generateRandomBoard(boardWidth, boardHeight, difficulty)
        
        #spriteColour = self.mainBoard[0][0]
        #print "sprite colour ", spriteColour


        self.life = maxLife
        string =str(self.life)
        string = string + " lives left"
        self.api.writeToLCD(2, 1, string)

        button = 0
        for i in range (0,6):
            self.api.setInk(colours[i][0],colours[i][1],colours[i][2], 4)

            self.api.colourButton(colours[i][0],colours[i][1],colours[i][2],button%2,button/2)
            button +=1

            for x in range(boardWidth):
                for y in range(boardHeight):
                    if self.mainBoard[y][x] == i:
                        self.api.drawPixel(x, y)



        self.api.setSprite(0,0,8,[0b10000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000])
        self.api.setSprite(1,0,8,[0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000])
        self.api.setSprite(2,0,8,[0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000])
        self.api.setSprite(3,0,8,[0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000])

        #v = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]   		    
        #self.floodFill(temp,temp[0][0], temp[0][0], 0,0, v, False, spriteArray)
        #return temp


    def __init__(self,api):
        #self.mainBoard = self.newGame(api)
        self.newGame(api)

        spriteArray = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]
        spriteArray[0][0] = 1

        lastPaletteClicked = None
        paletteClicked = self.mainBoard[0][0]
        
        v2 = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]   		    
        self.floodFill(self.mainBoard, self.mainBoard[0][0],paletteClicked, 0,0, v2, False, spriteArray)
        
        while True: # main game loop
            #print "current board"
            #print self.mainBoard
            paletteClicked = self.api.waitForButtonPress()

            if paletteClicked >= 6:
                paletteClicked = None

            if paletteClicked != None and paletteClicked != lastPaletteClicked:
                # a palette button was clicked that is different from the
                # last palette button clicked (this check prevents the player
                # from accidentally clicking the same palette twice)
                #print "button clicked received ", paletteClicked
                lastPaletteClicked = paletteClicked

            	self.api.setInk(colours[paletteClicked][0],colours[paletteClicked][1],colours[paletteClicked][2],4)
               
                # check if repeated colour
                if self.mainBoard[0][0] == paletteClicked: 
                        pass
                
                # init visited to 0 for floodfill
                v2 = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]   		    

                self.floodFill(self.mainBoard, self.mainBoard[0][0],paletteClicked, 0,0, v2, False, spriteArray)
                self.api.displaySprite(0,0,8,0,0)
                self.api.displaySprite(1,0,8,0,0)
                self.api.displaySprite(2,0,8,0,0)
                self.api.displaySprite(3,0,8,0,0)
                '''
                # print top left 3x3
                for y in range(3):
                    print self.mainBoard[y][0], " ", self.mainBoard[y][1], " ", self.mainBoard[y][2]
                    #print spriteArray[y][0], " ", spriteArray[y][1], " ", spriteArray[y][2]
                '''
                self.life -= 1
                string =str(self.life)
                if self.life == 1:
                    string = string + " life left"
                    self.api.writeToLCD(2, 1, string)		
                else:
		            string = string + " lives left"
		            self.api.writeToLCD(2, 1, string)

                self.resetGame = False

                if self.hasWon(self.mainBoard):
                    #print self.mainBoard
                    self.api.writeToLCD(2, 1, "You Win")
                    print "You Win"
                    print "Lives left: ", self.life
                    self.resetGame = True
                    time.sleep(2) # pause so the player can bask in victory
                    self.api.writeToLCD(2, 1, "")

                elif self.life == 0:
                    self.api.writeToLCD(2, 1, "You lose")
                    print "You Lose"                   
                    self.resetGame = True
                    time.sleep(2) # pause so the player can suffer in their defeat
                    self.api.writeToLCD(2, 1, "")

                if self.resetGame:
                    # start a new game
                    self.newGame(api)
                    #print "new board made"
                    #print self.mainBoard
                    lastPaletteClicked = None
                    paletteClicked = self.mainBoard[0][0]
                    
                    # reset sprite array                    
                    spriteArray = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]
                    spriteArray[0][0] = 1

                    v2 = [[0 for x in xrange(boardWidth)] for x in xrange(boardHeight)]   		    
                    self.floodFill(self.mainBoard, self.mainBoard[0][0],paletteClicked, 0,0, v2, False, spriteArray)
                    
                    





