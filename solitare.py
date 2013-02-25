#set board size
#wait for input



pieces = 33 # player 1, 2 and total pieces

gridSize = 7

center = gridSize/2 floored


animationSpeed = 10


resolution = 4
# send resolution to rainbowduino


actualGridSize = gridSize*(8/resolution)




winPrint = ("You won", "You lost")

pieceColours = ((255,0,0),(0,0,255),(0,255,0))


matrix[][]= ((0,0,1,1,1,0,0),
			 (0,0,1,1,1,0,0),
			 (1,1,1,1,1,1,1),
			 (1,1,1,2,1,1,1),
			 (1,1,1,1,1,1,1),
			 (0,0,1,1,1,0,0),
			 (0,0,1,1,1,0,0),	)init board


def checkInput(int x, int y):

	if 0 < x > gridSize or 0 < y > gridSize:
		printLCD(!turn, 1, "Out of bounds", 2)
		return 0
		
	elif matrix[x][y] == 0:
		printLCD(!turn, 1, "Out of board", 2)
		changePixel(x, y, Red, 2)
		return 0
		
	else:
		return matrix[x][y]



while (pieces > 1): # main game loop
	playable = False
	for each 1 in matrix get x,y:
		if matrix[x+1][y] ==1 or matrix[x-1][y] ==1 or matrix[x][y+1]==1 or matrix[x][y-1] == 1:
			True
			break
			
	if !playable:
		break
		
		
	wait for input and checkPlace(x, y) == 1:
		pass
		
		
	wait for input and checkPlace(x2, y2) == 2:
		pass
		
	if abs(x,x2)==2 or abs(y,y2)==2:
	
		if abs(x,x2)==2:
			if x < x2:
				if matrix[x+1][y]!=1:
		   			printLCD(!turn, 1, "Nothing to jump over", 2)
		   			
		   		else:	# acceptable move
		   			acceptableMove = True
		   		
			else:
				if matrix[x-1][y]!=1:
		   			printLCD(!turn, 1, "Nothing to jump over", 2)
		   		
		   		else:
		   			acceptableMove = True
		   			

		else:
			if y < y2:
				if matrix[x][y+1]!=1:
		   			printLCD(!turn, 1, "Nothing to jump over", 2)
		   			
		   		else:
		   			acceptableMove = True

		   		
			else:
				if matrix[x-1][y-1]!=1:
		   			printLCD(!turn, 1, "Nothing to jump over", 2)
		   		
		   		else:
		   			acceptableMove = True

		if acceptableMove:
			matrix[x][y] = 2
			matrix[x2][y2] = 1
			pieces--
			
						
if !playable:
	printLCD(0,1, "Can't make anymore moves!", 0)

else if matrix[center][center]==1:
	printLCD(0,1, "You won!", 0)


else
	printLCD(0,1, "Good effort!", 0)

