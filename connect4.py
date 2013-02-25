#set board size
#initialise board with very dim grid to show resolution?
#initialise array matrix and column count values
#wait for input
#check left right up down and diagonals for four in a row
#if found, that player wins



pieces = (0,0,0) # player 1, 2 and total pieces

gridSize = 16

totalGamePlaces = gridSize * gridSize
animationSpeed = 10
columnCounts = (0)

winner = 2


turnCount = 0 # used for gravity reverse mode, to know when to
gravity = 0 # use for gravity reverse mode, to show if reversed




gridColour[x][columnCount[x]] = 0 # initialise all to 2

# for horizontal connect4
for x in range(0,gridSize): # add enough counts for the number of columns 
	columnCounts.append(0)


# for diagonal connect4 //
columnTotals = (1)
for x in range(0,gridSize):
	columnCounts.append(0)
	columnTotals.append(columnsTotals[-1]+1)
	
for x in range(gridSize,(gridSize*2)-1):
	columnCount.append(0)
	columnTotals.append(columnsTotals[-1]-1)
# //



turnPrint = ("Opponent's turn", "Your turn")
winPrint = ("You won", "You lost", "It was a draw")

playerColours = ((255,0,0),(0,0,255))

turn = True # player1's turn first


def checkInput(int x, int y):
	if columnCount[x] == gridSize:
		printLCD(!turn, 1, "Can't go there", 2)
		changePixel(x, gridSize, Red, 2)
		return False
	else:
		gridColour[x][columnCount[x]]=turn
		moveUntil(x, gridSize, x, columnCount, playerColours[turn],animationSpeed)
		return True



def checkDiagonalInput(int x, int y):
	XAY = 1
	
	if x>y:
		XOY = 1
		x-y
		
	elif y>x:
		XOY = 0
		
	else:
		XAY = 0
	
	column = 7 XOY + 7
	
	
	
	if columnCount == columnsTotals[]:
		printLCD(!turn, 1, "Can't go there", 2)
		changePixel(..., Red, 2)

	else:

		gridColour[x][columnCount[x]]=turn
		moveUntil(x - (XOY*difference*XAY) , y - (!XOY*difference*XAY), (x - (XOY*difference*XAY)) - , columnCount, playerColours[turn],animationSpeed)
		return True		
	
	
	
	
	
			

def checkForWin(int x, int y):
	inARowCount = 1

	yCheck = 0
	xCheck = 1
	
	while( yCheck !=0 or xCheck !=0):
		tempY = y
		tempX = x
		
	
		while 0 <= tempX + xCheck < gridSize and 0 <= tempY + yCheck < gridSize:
			tempX += xCheck
			tempY += yCheck

			if gridColour[tempX + xCheck][tempY + yCheck] == turn:
				inARowCount++
				tempX += xCheck
				tempY += yCheck
			
			else:
				break # end of this players colours in this line direction
		
		
			
		# change the line or direction of checking
			
		if inARowCount > 3:
			# win
			
		# replace with switch statement equivalent (dictionary) 
		
		if xCheck == 1 and yCheck == 0:
			xCheck == -1
			
		else if xCheck == -1 and yCheck == 0:
			inARowcount = 1
			xCheck = 0
			yCheck = 1
		
		else if xCheck == 0 and yCheck == 1:
			yCheck = -1
			
		else if xCheck == 0 and yCheck == -1:
			inARowCount = 1
			xCheck = 1
		
		else if xCheck == 1 and yCheck == -1:
			xCheck = -1
			yCheck = 1
			
		else if xCheck == -1 and yCheck == 1:
			inARowCount = 1
			yCheck = -1
			
		else if xCheck == -1 and yCheck == -1:
			xCheck = 1
			yCheck = 1
	
	
def reverseGravity():
	gravity = !gravity
	
	
	
	
			


while (pieces[2] < totalGamePlaces and (pieces[2]>1...): # main game loop
	printLCD(0,1,turnPrint1[turn],0) # player, line, message, time (0 stay until overridden)
	printLCD(1,1,turnPrint2[!turn],0)

	wait for input and checkInput(x, y):
		pass
	
	turnCount++
	
	if turnCount % 3 == 0:
		reverseGravity()
		
	if checkForWin(x, y,turn):
		winner = turn
		break
	
	
	turn = !turn


if winner != 0:
	printLCD(0,1, winPrint[2], 0)
	printLCD(1,1, winPrint[2], 0)

elif turn:
	printLCD(0,1, winPrint[0], 0)
	printLCD(1,1, winPrint[1], 0)
	
else:
	printLCD(0,1, winPrint[1], 0)
	printLCD(1,1, winPrint[0], 0)	

