
numberOfColours = 11
colours = [[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[255,0,255],[0,255,255],[255,100,100],[100,255,100],[100,100,255],[255,255,255]]
gridSize = 16




class thisapp:
	
	def inputReceived(self, list):
		oldColour = self.colourGrid[list[0]][[list[1]]
		print oldColour
		newColour = (oldColour + 1 )% 11
		
		self.colourGrid[list[0]][list[1]] = newColour
		inkColours = colours[newColour]
		self.api.setInk(inkColours[0], inkColours[1], inkColours[2],4)
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
		
