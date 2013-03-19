import const
import sys
import time


const.turnPrint = ("Opponent's turn", "Your turn")
const.winPrint = ("You won", "You lost", "It was a draw")
const.playerColours = [[0,255,0],[0,0,255]]

class thisapp():



	def inputReceived(self, args):
		print "TICTACTOE: INPUT RECEIVED"
		if self.checkInput(args):
			#print self.gridColours
			
			if self.checkForWin(args[0], args[1]):
				self.gameOver(self.turn)
			
			
			self.pieces[self.turn] +=1
			self.pieces[2] +=1
			
			if self.pieces[2] >= self.totalGamePlaces:
				self.gameOver(2)
			
			
			self.turn = not self.turn
			self.api.writeToLCD(0,1,const.turnPrint[self.turn]) # player, line, message, time (0 stay until overridden)
			self.api.writeToLCD(1,1,const.turnPrint[not self.turn])
		else:
			self.api.writeToLCD(self.turn, 1, "You can't go there")
			
		self.inputReceived(self.api.waitForInput())			
			
			
			
	def gameOver(self, number): # redo TODO
		print "TOTAL PIECES ", self.pieces[2]
		print "TOTAL GAME PIECES ", self.totalGamePlaces
		print "TICTACTOE: GAME OVER"
		if number ==0:
			self.api.writeToLCD(0,1, const.winPrint[0])
			self.api.writeToLCD(1,1, const.winPrint[1])

		elif number == 1:
			self.api.writeToLCD(0,1, const.winPrint[1])
			self.api.writeToLCD(1,1, const.winPrint[0])	

		else:
			self.api.writeToLCD(2,1, const.winPrint[2]) # print same message to both lcds (draw)		
		
		time.sleep(3)		
		sys.exit(0)




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
				if self.gridColours[tempY + yCheck][tempX + xCheck] == self.turn:
					inARowCount+=1
					tempX += xCheck
					tempY += yCheck
				
				else:
					break # end of this players colours in this line direction
			
			
				
			# change the line or direction of checking
				
			if inARowCount > 2:
				return 1
				

			if xCheck == 1 and yCheck == 0: #1
				print "here1"
				xCheck = -1
				
			elif xCheck == -1 and yCheck == 0: #2
				print "here2"
				inARowcount = 1
				xCheck = 0
				yCheck = 1
			
			elif xCheck == 0 and yCheck == 1: #3
				print "here3"
				yCheck = -1
				
			elif xCheck == 0 and yCheck == -1: #4
				print "here4"
				inARowCount = 1
				xCheck = 1
			
			elif xCheck == 1 and yCheck == -1: #5
				print "here5"
				xCheck = -1
	
				
			elif xCheck == -1 and yCheck == -1: #6
				print "here6"
				inARowCount = 1
				yCheck = 1
				
			elif xCheck == -1 and yCheck == 1: #7
				print "here7"
				xCheck = 1
				
			elif xCheck == 1 and yCheck == 1:
				print "here8"
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
					self.api.writeToLCD(not self.turn, 1, "Can't go there")	#only displayed for 2 seconds
					#self.api.flashPixel(x, y, Red, 2)
					return False
				
				else:
					print "turn print ", self.turn
					r = const.playerColours[self.turn][0]
					g = const.playerColours[self.turn][1]
					b = const.playerColours[self.turn][2]
					self.api.setInk(r,g,b,4)
					self.api.drawSprite(self.turn,4,x*5+1, y*5+1)
					#self.api.drawPixel(x,y)
					self.gridColours[y][x] = self.turn
				
					return True
					
					
			else:
				#self.api.flashPixel(x, y, Red, 2)
				return False
				
				
				
				
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


		self.api.writeToLCD(0,1,const.turnPrint[self.turn]) # player, line, message, time (0 stay until overridden)
		self.api.writeToLCD(1,1,const.turnPrint[not self.turn])
					
		self.inputReceived(self.api.waitForInput())
