
numberOfColours = 11
colours = [[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[255,0,255],[0,255,255],[255,100,100],[100,255,100],[100,100,255],[255,255,255]]
gridSize = 16


norm = True #false if qr is inverted

class thisapp:
	
	def inputReceived(self, list):
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
		
		self.colourGrid = [[1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
						   [1,0,0,0,0,0,1,0,0,0,0,1,0,0,1],
						   [1,0,1,1,1,0,1,0,0,1,1,0,1,1,1],
						   [1,0,1,1,1,0,1,0,0,0,0,1,1,0,1],
						   [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
						   [1,0,0,0,0,0,1,0,1,0,0,0,1,0,0],
						   [1,1,1,1,1,1,1,0,1,1,1,0,0,0,1],
						   [0,0,0,0,0,0,0,0,1,0,0,1,1,0,0],
						   [1,1,1,1,0,1,1,0,0,1,1,1,0,0,1],
						   [0,0,0,1,1,0,1,0,0,0,0,1,0,1,1],
						   [1,1,0,0,1,1,1,0,0,1,1,0,0,0,1],
						   [0,1,0,0,0,1,0,0,1,0,1,0,1,1,0],
						   [1,1,0,1,1,0,1,1,0,1,1,1,0,1,1],
						   [0,1,0,0,1,1,0,0,1,0,1,1,0,1,1],
						   [1,0,1,0,0,0,0,1,1,0,0,1,0,0,1]]

		self.api.setInk(255,255,255,4)
		
		for i in range(0,16):
			self.api.drawPixel(0,i)
			self.api.drawPixel(i,0)
		
		for i in range(1,16):
			for j in range(1,16):
				if self.colourGrid[i][j] == norm:
					self.api.drawPixel(i,j)
		

