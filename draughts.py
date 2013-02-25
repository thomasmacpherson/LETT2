#set board size
#wait for input

pieces[]= (12,12) # player 1, 2 and total pieces

gridSize = 8


resolution = 4
# send resolution to rainbowduino


winPrint = ("You won", "You lost","Draw")

pieceColours = ((255,0,0),(0,0,255),(0,255,0))

pieceCodes = [0,1,3,4]



matrix[][]= ((1,2,1,2,1,2,1,2),
			 (2,1,2,1,2,1,2,1),
			 (1,2,1,2,1,2,1,2),
			 (2,2,2,2,2,2,2,2),
			 (2,2,2,2,2,2,2,2),
			 (2,0,2,0,2,0,2,0),
			 (0,2,0,2,0,2,0,2),
			 (2,0,2,0,2,0,2,0))# init board 0=white, 1=black, 2=empty




while (pieces[0] > 1 or pieces[1]> 1): # main game loop

	play = True
	
	while play:
		wait for input x,y: check is this piece turn matrix[x][y] == turn
	
	
	
		while True:
			wait for input x2, y2: check is +-1 on x
			
			if not KING:
				if y2 == y +1 and (x2 == x+1 or x2 == x-1) matrix[x2][y2] == 2 :
				
				elif y2 == y+2 and matrix[x2][y2]==2:
					if x2 == x+2:
						matrix[y+1][x+1] == pieceCodes[!turn] or matrix[y+1][x+1] == pieceCodes[!turn+2]:
					elif x2 == x-2:
						matrix[y+1][x-1] == pieceCodes[!turn] or matrix[y+1][x-1] == pieceCodes[!turn+2]:
						
						
			else:
			
			
		
		