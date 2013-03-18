
class thisapp():

	def inputReceived(self, args):
		self.move +=1
		print "input received ", self.move
		
		if self.checkInput(args):
			self.checkForFlips(args[0], args[1])
	
		if self.pieces[2] >= self.totalGamePlaces:
			pass#self.gameOver()
			
			
		self.api.writeToLCD(0,0,self.turnPrint[self.turn]) # player, line, message, time (0 stay until overridden)
		self.api.writeToLCD(1,0,self.turnPrint[not self.turn])
		self.inputReceived(self.api.waitForInput())			
			
			
			
	def gameOver():
		if self.pieces[0] > self.pieces[1]:
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
		print "check input ", self.move
		if len(args) == 2:
			x = args[0]
			y = args[1]
			
			if self.gridColours[x][y] != 2:
				#self.api.printLCD(!turn, 1, "Can't go there", 2)	#only displayed for 2 seconds
				#self.api.flashPixel(x, y, Red, 2)
				return False
			
			else:
				self.turn = not self.turn
				self.api.setInk(self.playerColours[self.turn][0],self.playerColours[self.turn][1],self.playerColours[self.turn][2],4)
				self.api.drawPixel(x,y)
				self.gridColours[x][y] = self.turn
				self.pieces[self.turn] +=1
				self.pieces[2] +=1
				
				return True



	def checkForFlips(self, x, y):
		print "check for flips ", self.move
		xCheck = 1
		yCheck = 0

	
		while( yCheck !=0 or xCheck !=0):
			print "xCheck ", xCheck
			print "yCheck ", yCheck
			tempY = y
			tempX = x
			inARowCount = 0
			checkDirection = 0
	
			while 0 <= (tempX + xCheck) < self.gridSize and 0 <= (tempY + yCheck) < self.gridSize:
				print checkDirection 
				#tempX += xCheck
				#tempY += yCheck

				if self.gridColours[tempX + xCheck][tempY + yCheck] != self.turn and self.gridColours[tempX + xCheck][tempY + yCheck] != 2: #other players colour
					print "other player found ", self.move
					tempX += xCheck
					tempY += yCheck
					inARowCount +=1
			
				elif self.gridColours[tempX + xCheck][tempY + yCheck] == self.turn and inARowCount > 0:
					tempX += xCheck
					tempY += yCheck
					
					print "turning pieces ", self.move
					self.api.setInk(self.playerColours[self.turn][0],self.playerColours[self.turn][1],self.playerColours[self.turn][2],4)
					#self.api.drawLine(x,y,tempX,tempY)
					self.pieces[self.turn] += inARowCount
					newTempx = x
					newTempy = y
					
					print "new temp x ",newTempx
					print "new temp y ", newTempy
					print "temp x ", tempX
					print "temp y ", tempY
					
					
					while newTempx != tempX or newTempy != tempY:
						print "turning"
						newTempx += xCheck
						newTempy += yCheck
						self.api.drawPixel(newTempx,newTempy)
						self.gridColours[newTempx][newTempy] = self.turn
					break
					
					
				
				else:
					break # end of this players colours in this line direction
			checkDirection +=1


			# switching through all the possible directions
			
			if xCheck == 1 and yCheck == 0:
				xCheck = -1
			
			elif xCheck == -1 and yCheck == 0:
				xCheck = 0
				yCheck = 1
		
			elif xCheck == 0 and yCheck == 1:
				yCheck = -1
			
			elif xCheck == 0 and yCheck == -1:
				xCheck = 1
		
			elif xCheck == 1 and yCheck == -1:
				xCheck = -1
				
			
			elif xCheck == -1 and yCheck == -1:
				yCheck = 1
			
			elif xCheck == -1 and yCheck == 1:
				xCheck = 1
			
				
			elif xCheck == 1 and yCheck == 1: # fall out clause
				xCheck = 0
				yCheck = 0
			
			
			
			
				
				
	def __init__(self, api):
		self.api = api
		self.move = 0

		self.pieces = [0,0,0] # player 1, 2 and total pieces
		self.gridSize = 16
		self.res = 8

		self.totalGamePlaces = self.gridSize * self.gridSize
		self.turnPrint = ("Opponent's turn", "Your turn")
		self.winPrint = ("You won", "You lost", "It was a draw")
		self.playerColours = ((255,0,0),(0,0,150))

		self.turn = True # player1's turn first


		self.api.writeToLCD(0,0,self.turnPrint[self.turn]) # player, line, message, time (0 stay until overridden)
		self.api.writeToLCD(1,0,self.turnPrint[not self.turn])
		
		self.rowColours = []
		self.gridColours = []
		for i in range(self.res):
			self.rowColours.append(2)
		for i in range(self.res):
			self.gridColours.append(self.rowColours)
		
		print self.gridColours
		'''
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

		'''
		self.inputReceived(self.api.waitForInput())



