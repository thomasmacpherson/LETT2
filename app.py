
numberOfColours = 11
colours = [[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[255,0,255],[0,255,255],[255,100,100],[100,255,100],[100,100,255],[255,255,255]]
gridSize = 16




class thisapp:
	
	def inputReceived(self, list):
		print "app3"
		x = list[0]
		y = list[1]
		oldColour = self.colourGrid[x][y]
		newColour = (oldColour + 1 )% 11
		
		self.colourGrid[x][y] = newColour
		inkColours = colours[newColour]
		self.api.setInk(inkColours[0], inkColours[1], inkColours[2],4)
		self.api.drawPixel(x,y)
	
		
	def __init__(self, api):
		self.api = api
		print "app2"
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
			print "app1"
			inputList = self.api.waitForInput()
			print inputList
			self.inputReceived(inputList)
		
