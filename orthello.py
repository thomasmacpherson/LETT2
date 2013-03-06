
class thisapp():
	def __init__(self, api):
		self.api = api


		self.pieces = (0,0,0) # player 1, 2 and total pieces
		self.gridSize = 16

		self.totalGamePlaces = self.gridSize * self.gridSize
		self.turnPrint = ("Opponent's turn", "Your turn")
		self.winPrint = ("You won", "You lost", "It was a draw")
		self.playerColours = ((0,0,0),(255,255,255))

		self.turn = True # player1's turn first

		self.gridColours = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
							[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

		
		self.inputReceieved(self.api.waitForInput())


	def inputReceived(self, args):
		if self.checkInput(args):
			self.checkForFlips(args[0], args[1])
	
		if pieces[2] >= totalGamePlaces:
			pass#self.gameOver()
			
			
		#self.api.printLCD(0,1,turnPrint1[turn],0) # player, line, message, time (0 stay until overridden)
		#self.api.printLCD(1,1,turnPrint2[!turn],0)
		self.turn = not self.turn
		self.inputReceived(self.api.waitForInput())			
			
			
			
	def gameOver():
		if self.pieces[0] > self/pieces[1]:
			#printLCD(0,1, winPrint[0], 0)
			#printLCD(1,1, winPrint[1], 0)
			pass

		elif self.pieces[1] > self.pieces[0]:
			#printLCD(0,1, winPrint[1], 0)
			#printLCD(1,1, winPrint[0], 0)	
			pass

		else:
			#printLCD(3,1, winPrint[2], 0)	
			pass	
			





	def checkInput(self, args):
		if args.length == 2:
		
			if self.gridColours[x][y] != 2:
				#self.api.printLCD(!turn, 1, "Can't go there", 2)	#only displayed for 2 seconds
				#self.api.flashPixel(x, y, Red, 2)
				return False
			
			else:
				self.setInk(playerColours[turn],4)
				self.api.drawPixel(x,y)
				self.gridColours[x][y] = turn
			
				return True



	def checkForFlips(x, y):

		yCheck = 0
		xCheck = 1
	
		while( yCheck !=0 or xCheck !=0):
			tempY = y
			tempX = x
		
	
			while 0 <= tempX + xCheck < self.gridSize and 0 <= tempY + yCheck < self.gridSize:
				tempX += xCheck
				tempY += yCheck

				if self.gridColours[tempX + xCheck][tempY + yCheck] != turn and self.gridColours[tempX + xCheck][tempY + yCheck] != 2: #other players colour
					tempX += xCheck
					tempY += yCheck
			
				else:
					break # end of this players colours in this line direction
		
#use draw line 
		# replace with switch statement equivalent (dictionary) 
		
			if xCheck == 1 and yCheck == 0:
				xCheck == -1
			
			elif xCheck == -1 and yCheck == 0:
				inARowcount = 1
				xCheck = 0
				yCheck = 1
		
			elif xCheck == 0 and yCheck == 1:
				yCheck = -1
			
			elif xCheck == 0 and yCheck == -1:
				inARowCount = 1
				xCheck = 1
		
			elif xCheck == 1 and yCheck == -1:
				xCheck = -1
				yCheck = 1
			
			elif xCheck == -1 and yCheck == 1:
				inARowCount = 1
				yCheck = -1
			
			elif xCheck == -1 and yCheck == -1:
				xCheck = 1
				yCheck = 1

