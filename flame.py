import const
import random

class thisapp():
	
	def inputReceived(self, args):
		self.xPressed = args[0]
		self.yPressed = args[1]
		
		
			
			
		# Cause Loop here if winner found
		if self.check == 1:
			self.inputReceived(self.api.waitForInput())
		
		if self.gridColours[self.yPressed][self.xPressed] == 3:
			self.api.writeToLCD(1, 1, "Don't click there!")
			self.inputReceived(self.api.waitForInput())
		if self.gridColours[self.yPressed][self.xPressed] == 4:
			self.api.writeToLCD(1, 1, "Don't click there!")
			self.inputReceived(self.api.waitForInput())
		
		# Set Fires Vert and Hor
		self.setFire()
		
		# Check if all areas on fire
		self.checkWin()
		
		# Change turn
		if self.turn == 1:
			self.turn = 2
			self.api.writeToLCD(1, 0, "Player 2's Turn")
			self.api.writeToLCD(1, 1, "")
		else:
			self.turn = 1
			self.api.writeToLCD(1, 0, "Player 1's Turn")
			self.api.writeToLCD(1, 1, "")
		
		for y in range(len(self.gridColours)):
			print(self.gridColours[y])
		
		
		self.inputReceived(self.api.waitForInput())	
	
	
	def setFire(self) :
		
		self.api.writeToLCD(1, 1, "Nice Move!")
		# Initial
		
		if self.turn == 1:
			if self.gridColours[self.yPressed][self.xPressed] == 1 or self.gridColours[self.yPressed][self.xPressed] == 0:
				self.gridColours[self.yPressed][self.xPressed] = 3
			else :
				self.gridColours[self.yPressed][self.xPressed] = 1
				
		elif self.turn == 2:
			if self.gridColours[self.yPressed][self.xPressed] == 2 or self.gridColours[self.yPressed][self.xPressed] == 0:
				self.gridColours[self.yPressed][self.xPressed] = 4
			else :
				self.gridColours[self.yPressed][self.xPressed] = 2
		
		# Spreading
		for x in range(self.xPressed+1, len(self.gridColours)):
			if self.gridColours[self.yPressed][x] != 3 and self.gridColours[self.yPressed][x] != 4:
				self.gridColours[self.yPressed][x] = self.turn
			else:
				break
				
		for x in reversed(range(0, self.xPressed)):
			if self.gridColours[self.yPressed][x] != 3 and self.gridColours[self.yPressed][x] != 4:
				self.gridColours[self.yPressed][x] = self.turn
			else:
				break
		
		for y in range(self.yPressed+1, len(self.gridColours)):
			if self.gridColours[y][self.xPressed] != 3 and self.gridColours[y][self.xPressed] != 4:
				self.gridColours[y][self.xPressed] = self.turn
			else:
				break
		
		for y in reversed(range(0, self.yPressed)):
			if self.gridColours[y][self.xPressed] != 3 and self.gridColours[y][self.xPressed] != 4:
				self.gridColours[y][self.xPressed] = self.turn
			else:
				break
		
			
		self.updateAreas()
		
	
	def updateAreas(self) :
		# Update GUI
		for x in range(len(self.gridColours)):
			for y in range(len(self.gridColours[x])):
				if self.gridColours[y][x] == 0:
					self.api.setInk(0,0,0,4)
					self.api.drawPixel(x, y)
				if self.gridColours[y][x] == 2:
					self.api.setInk(0,255,0,4)
					self.api.drawPixel(x, y)
				if self.gridColours[y][x] == 1:
					self.api.setInk(255,0,0,4)
					self.api.drawPixel(x, y)
				if self.gridColours[y][x] == 4:
					self.api.setInk(0,150,0,4)
					self.api.drawPixel(x, y)
				if self.gridColours[y][x] == 3:
					self.api.setInk(150,0,0,4)
					self.api.drawPixel(x, y)
					
					
	def checkWin(self) :
		self.check  = 1
		self.oneScore = 0
		self.twoScore = 0
		# Loop through all areas checking for empty area AND count scores
		for x in range(len(self.gridColours)):
			for y in range(len(self.gridColours[x])):
				if self.gridColours[y][x] == 0:
					self.check = 0
				if self.gridColours[y][x] == 2 or self.gridColours[y][x] == 4:
					self.twoScore+= 1
				if self.gridColours[y][x] == 1 or self.gridColours[y][x] == 3:
					self.oneScore+= 1
		
		# If no empty areas announce winner!
		if self.check == 1:
			self.win()
		
	def win(self) :
		# Print Scores and cause infinite loop!
		self.api.writeToLCD(1, 0, "P1:"+str(self.oneScore))
		self.api.writeToLCD(1, 1, "P2:"+str(self.twoScore))
		
		if self.oneScore > self.twoScore:
			self.api.writeToLCD(0, 1, "Player 1 Wins!!")
		elif self.twoScore > self.oneScore:
			self.api.writeToLCD(0, 1, "Player 2 Wins!!")
		elif self.twoScore > self.oneScore:
			self.api.writeToLCD(0, 1, "It's a draw!")
		
		self.inputReceived(self.api.waitForInput())	
	
	
	def __init__(self, api):
		print "FLAME: INITIALISE"
		self.api = api
		self.turn = random.randint(1, 2)
		
		if self.turn == 1:
			self.api.writeToLCD(1, 0, "Player 1's Turn")
		elif self.turn == 2:
			self.api.writeToLCD(1, 0, "Player 2's Turn")
		
		self.check = 0
		self.api.writeToLCD(0, 0, "Flame Game")
		
		# Initialise blank areas
		self.gridColours = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
							[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
		
		
		# Update Colours
		for x in range(len(self.gridColours)):
			for y in range(len(self.gridColours[x])):
				if self.gridColours[y][x] == 0:
					self.api.setInk(0,0,0,4)
					self.api.drawPixel(x, y)
				if self.gridColours[y][x] == 2:
					self.api.setInk(0,255,0,4)
					self.api.drawPixel(x, y)
				if self.gridColours[y][x] == 1:
					self.api.setInk(255,0,0,4)
					self.api.drawPixel(x, y)
				
		
		self.inputReceived(self.api.waitForInput())