import const


const.turnPrint = ("Opponent's turn", "Your turn")
const.winPrint = ("You won", "You lost", "It was a draw")
const.playerColours = ((100,255,200),(0,255,0))

class thisapp():



	def inputReceived(self, args):
		print "TICTACTOE: INPUT RECEIVED"
		if self.checkInput(args):
			print self.gridColours
			'''
			if self.checkForWin(args[0], args[1]):
				self.gameOver(self.turn)
				'''
	
		if self.pieces[2] >= self.totalGamePlaces:
			self.gameOver()
			
			
		self.api.writeToLCD(0,1,const.turnPrint[self.turn]) # player, line, message, time (0 stay until overridden)
		self.api.writeToLCD(1,1,const.turnPrint[not self.turn])
		
		self.turn = not self.turn
		self.inputReceived(self.api.waitForInput())			
			
			
			
	def gameOver(number): # redo TODO
		print "TICTACTOE: GAME OVER"
		if numer ==0:
			self.api.writeToLCD(0,1, const.winPrint[0])
			self.api.writeToLCD(1,1, const.winPrint[1])

		elif number == 1:
			self.api.writeToLCD(0,1, const.winPrint[1])
			self.api.writeToLCD(1,1, const.winPrint[0])	

		else:
			self.api.writeToLCD(2,1, const.winPrint[2]) # print same message to both lcds		
			



	def checkForWin(self, x, y):
		print "TICTACTOE: CHECK FOR WIN"
		
		xCheck = 1
		yCheck = 0
		
		
		print "x value ", x
		print "y value ", y
		
		while( yCheck !=0 or xCheck !=0):
			tempY = y
			tempX = x
			inARowCount = 1
			#print "here"
			while 0 <= (tempX + xCheck) and  (tempX + xCheck) < self.gridSize and 0 <= (tempY + yCheck) and (tempY + yCheck) < self.gridSize:
				
				tempX += xCheck
				tempY += yCheck
				print tempX
				print tempY
				if self.gridColours[tempX + xCheck][tempY + yCheck] == self.turn:
					inARowCount+=1
					tempX += xCheck
					tempY += yCheck
				
				else:
					break # end of this players colours in this line direction
			
			print "here"
				
			# change the line or direction of checking
				
			if inARowCount > 2:
				return 1
				

			if xCheck == 1 and yCheck == 0: #1
				xCheck == -1
				
			elif xCheck == -1 and yCheck == 0: #2
				inARowcount = 1
				xCheck = 0
				yCheck = 1
			
			elif xCheck == 0 and yCheck == 1: #3
				yCheck = -1
				
			elif xCheck == 0 and yCheck == -1: #4
				inARowCount = 1
				xCheck = 1
			
			elif xCheck == 1 and yCheck == -1: #5
				xCheck = -1
	
				
			elif xCheck == -1 and yCheck == -1: #6
				inARowCount = 1
				yCheck = 1
				
			elif xCheck == -1 and yCheck == 1: #7
				xCheck = 1
				
			elif xCheck == 1 and yCheck == 1:
				xCheck = 0
				yCheck = 0
				
			
			
	


	def checkInput(self, args):
		print "TICTACTOE: CHECK INPUT"
		if len(args) == 2:
			x = args[0]
			y = args[1]
			
			if self.validPos.count(x) and self.validPos.count(y): # is a valid place
				x = x/5
				y = y/5
				if self.gridColours[x][y] != 2:
					#self.api.printLCD(!turn, 1, "Can't go there", 2)	#only displayed for 2 seconds
					#self.api.flashPixel(x, y, Red, 2)
					return False
				
				else:
					self.pieces[self.turn] +=1
					self.pieces[2] +=1
					self.api.setInk(const.playerColours[self.turn][0],const.playerColours[self.turn][1],const.playerColours[self.turn][2],4)
					self.api.drawSprite(self.turn,4,x*5+1, y*5+1)
					#self.api.drawPixel(x,y)
					self.gridColours[x][y] = self.turn
				
					return True
					
					
			else:
				#self.api.flashPixel(x, y, Red, 2)
				pass
				
				
				
				
	def __init__(self, api):
		print "TICTACTOE: INITIALISE"
		self.api = api
		#self.api.set
		#self.api.setResolution()


		self.api.setInk(200,0,0,4) # red for grid lines
		
		self.api.drawLine(5,1,5,14) # first vertical line
		self.api.drawLine(10,1,10,14) #second vertical line
		self.api.drawLine(1,5,14,5) # first horizontal line
		self.api.drawLine(1,10,14,10) # second horizontal line


		self.api.setSprite(4,0,4,[0b10010110, 0b01101001])
		self.api.setSprite(4,1,4,[0b01101001, 0b10010110])
		
		self.pieces = [0,0,0] # player 1, 2 and total
		self.gridSize = 3
		
		self.gridColours = [[2,2,2],
							[2,2,2],
							[2,2,2]]

		self.totalGamePlaces = self.gridSize * self.gridSize


		self.turn = True # player1's turn first
		self.gridColours
		
		self.validPos = (1,2,3,4,6,7,8,9,11,12,13,14)
		self.placePositions = [1,6,11]
		
		self.api.writeToLCD(2,0,"TicTacToe")
		
		self.inputReceived(self.api.waitForInput())
