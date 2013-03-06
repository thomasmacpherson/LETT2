
numberOfColours = 11
colours = [[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[255,0,255],[0,255,255],[255,100,100],[100,255,100],[100,100,255],[255,255,255]]
gridSize = 16




class thisapp:
	
	def inputReceived(self, list):
		self.colourGrid[list[0]][list[1]] = self.colourGrid[list[0]][[list[1]]+1%numberOfColours
		self.inkColours[] = colours[self.colourGrid[list[0]][list[1]]]
		self.api.setInk(self.inkColours[0], self.inkColours[1], self.inkColours[2],4)
		self.api.drawPixel(list[0],list[1])
	
		
	def __init__(self, api):
		self.api = api
		
		self.colourGrid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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

		while True:
			list = self.api.waitForInput()
			print list
			self.inputReceived(list)
		
