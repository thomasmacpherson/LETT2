# AUTHOR: SCOTT BROWN 18/03/2013


import const

class thisapp():
	
	def inputReceived(self, args):
		self.xPressed = args[0]
		self.yPressed = args[1]
		
		if self.gridColours[self.yPressed][self.xPressed] == 5:
			self.api.writeToLCD(2, 1, "That's a wall!")
		elif self.xPressed == self.playerX:
			self.api.writeToLCD(2, 1, " ")
			if self.yPressed == (self.playerY + 1):
				self.direction = 0
				self.movePlayer(self.direction)
			if self.yPressed == (self.playerY - 1):
				self.direction = 1
				self.movePlayer(self.direction)
		elif self.yPressed == self.playerY:
			self.api.writeToLCD(2, 1, " ")
			if self.xPressed == (self.playerX + 1):
				self.direction = 2
				self.movePlayer(self.direction)
			if self.xPressed == (self.playerX - 1):
				self.direction = 3
				self.movePlayer(self.direction)
				
		self.inputReceived(self.api.waitForInput())	
	
	
	def movePlayer(self, direction) :
		self.api.clearSpace(self.playerX, self.playerY)
		if self.gridColours[self.yPressed][self.xPressed] == 4:
			self.win()
			
		self.playerX = self.xPressed
		self.playerY = self.yPressed
		self.api.setInk(204,204,204 , 4)
		self.api.drawPixel(self.playerX, self.playerY)
	
	
	def win(self) :
		self.api.writeToLCD(2, 1, "YOU WIN!")
		
		
	
	
	def __init__(self, api):
		print "SCAMPER: INITIALISE"
		self.api = api
		self.playerX = 1
		self.playerY = 0
		self.api.writeToLCD(2, 0, "Scamper")
		self.gridColours = [[5,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
							[5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5],
							[5,5,5,5,5,5,5,5,2,5,5,5,5,5,2,5],
							[5,2,2,2,2,2,2,2,2,5,2,2,2,2,2,5],
							[5,2,5,5,5,5,5,5,5,5,5,2,5,5,2,5],
							[5,2,2,5,2,2,2,2,5,2,2,2,5,2,2,5],
							[5,5,2,5,2,5,5,2,5,2,5,5,5,2,5,5],
							[5,2,2,5,2,2,5,2,5,2,2,2,5,2,2,5],
							[5,2,5,5,5,2,5,2,5,5,5,5,5,5,2,5],
							[5,2,2,2,5,2,5,2,5,2,2,2,2,2,2,5],
							[5,2,5,2,2,2,5,2,5,2,5,5,5,5,5,5],
							[5,2,5,5,5,5,5,2,5,2,5,5,2,2,2,5],
							[5,2,5,2,5,2,2,2,5,2,2,2,2,5,2,5],
							[5,2,5,2,5,2,5,5,5,5,5,5,5,4,4,5],
							[5,2,2,2,5,2,2,2,2,2,2,2,5,4,4,5],
							[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]
		
		
		self.api.setInk(204,204,204, 4)
		
		for x in range(len(self.gridColours)):
			for y in range(len(self.gridColours[x])):
			
				if self.gridColours[y][x] == 3:
					self.api.drawPixel(x, y)


		self.api.setInk(255,204,0, 4)
		
		for x in range(len(self.gridColours)):
			for y in range(len(self.gridColours[x])):
					
				if self.gridColours[y][x] == 4:
					self.api.drawPixel(x, y)
					
					
		self.api.setInk(255, 0,0 , 4)	
						
		for x in range(len(self.gridColours)):
			for y in range(len(self.gridColours[x])):					
				if self.gridColours[y][x] == 5:
					self.api.drawPixel(x, y)
				
		
		self.inputReceived(self.api.waitForInput())