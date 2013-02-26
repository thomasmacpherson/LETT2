import random

class thisapp():
	def __init__(self, api):
		self.api = api
		self.api.set
		self.api.setBG()
		self.api.setResolution()
		self.api.waitForInput(inputReceived)
		self.gridSize = 16


		self.turn = True # player1's turn first
		self.gridColours

		load sprite
		move sprite right accross screen

		self.level = 1
		self.towerHeights = []
		for i in range(0,16):
			self.towerHeights.append(random.random(0,level+1)
	
	def inputreceived(self):
		self.api.moveUntil(13, towerHeights-1) #falling bomb
		
		if towerHeights[x] >0:
			towerHeights[x]-=1 #tower height reduced
	
	def buildTowers(self):
		for i in range(0,16):
			self.api.drawLine(i,0,i,self.towerHeights[i],r,g,b)
		