class thisapp():
	def __init__(self, api):
		self.api = api
		self.api.set
		self.api.setResolution()
		self.api.setBG()

		self.api.waitForInput(inputReceived)
		self.pieces = (0,0,0) # player 1, 2 and total pieces
		self.gridSize = 16

		self.totalGamePlaces = gridSize * gridSize
		self.turnPrint = ("Opponent's turn", "Your turn")
		self.winPrint = ("You won", "You lost", "It was a draw")
		self.playerColours = ((0,0,0),(255,255,255))

		self.turn = True # player1's turn first
		self.gridColours


	def inputReceived(self, args):
		if self.checkInput(args):
			self.checkForFlips(args[0], args[1])
	
		if pieces[2] >= totalGamePlaces:
			self.gameOver()
			
			
		self.api.printLCD(0,1,turnPrint1[turn],0) # player, line, message, time (0 stay until overridden)
		self.api.printLCD(1,1,turnPrint2[!turn],0)
		self.turn = !self.turn
		self.api.waitForInput(inputReceived)			
			
			
			
	def gameOver():
		if pieces[0] > pieces[1]:
			printLCD(0,1, winPrint[0], 0)
			printLCD(1,1, winPrint[1], 0)

		elif pieces[1] > pieces[0]:
			printLCD(0,1, winPrint[1], 0)
			printLCD(1,1, winPrint[0], 0)	

		elif:
			printLCD(3,1, winPrint[2], 0)		
			





	def checkInput(self, args):
		if args.length == 2:
		
			if gridColours[x][y] =! 2:
				self.api.printLCD(!turn, 1, "Can't go there", 2)	#only displayed for 2 seconds
				self.api.flashPixel(x, y, Red, 2)
				return False
			
			else:
				self.api.drawPixel(x,y, playerColours[turn])
				gridColours[x][y] = turn
			
				return True


