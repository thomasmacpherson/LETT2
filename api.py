import Queue
#import RPi.GPIO as GPIO
import i2cHandler


RDsAdrs=[]
width = 2
length = 2




baseAdr = 0x10

for i in range(0,width):
	RDsAdrs.append([])
	for j in range(0,length):
		RDsAdrs[i].append(baseAdr + i*2+j)


class api:
	def __init__(self, emulated):
		self.qOut= Queue.Queue(maxsize=0)
		self.qIn = Queue.Queue(maxsize=0)
		
		self.lowerBoarder = 7
		self.res = 8
		
		self.mapping = {8:7,4:3,2:1,1:0}
		
		self.i2chandler = i2cHandler.handler(self.qOut)
		self.emulated = emulated
		

		
		if self.emulated:
			import em
			self.qOutEmulated = Queue.Queue(maxsize=0)
			self.emu = em.em(self.qOutEmulated, self.qIn)
		


	def printsomething(self):
		print "something"
	
	def printtoscreen(self,display):
		pass #self.emu.screenPrint(display)
	
	def readInput(self):
		self.emu.input()
		#print "here also"
		
	def closeApp(self):
		pass
		
	def waitForInput(self):
		print "waiting for input in api"
		return self.emu.waitForScreenPixelPress()
		
	def checkForInput(self):
		pass
		
	def drawSquare(self,x1,y1,x2,y2):
		self.squareSplit(x1,y1,x2,y2)
		
	def drawLine(self,x,y,ex,ey):
		if restrictedTo([x,ex],self.lowerBoarder)!=2:
			if restrictedTo([y,ey], self.lowerBoarder)!=2:
				self.i2chandler.drawLine(RDsAdrs[x/self.res][y/self.res], x%self.res, y%self.res, ex%self.res, ey%self.res) # send to single grid
			
			else:
				self.lineSplit(x,y,ex,ey,1)
		else:
			if restrictedTo([y,ey], self.lowerBoarder)!=2:
				self.lineSplit(x,y,ex,ey,0)
			else:
				pass

	def writeToLCD(self, LCD, message):
		if self.emulated:
			self.emu.writeLCD(LCD, message)
			
					
		
	def setInk(self, r, g, b, grid):
		if self.emulated:
			self.emu.setInk(r, g, b, grid)
				
		if grid >= 4:
			self.i2chandler.setInk(RDsAdrs[0][0], r, g, b)
			self.i2chandler.setInk(RDsAdrs[0][1], r, g, b)
			self.i2chandler.setInk(RDsAdrs[1][0], r, g, b)
			self.i2chandler.setInk(RDsAdrs[1][1], r, g, b)
			
		else:
			self.i2chandler.setInk(RDsAdrs[grid/2][grid%2], r, g, b)		
		
	def drawPixel(self, x, y):
		self.i2chandler.drawPixel(RDsAdrs[x/self.res][y/self.res], x%self.res, y%self.res)
		
		if self.emulated:
			grid = (x /self.res) + (y/self.res)*2
			self.emu.drawPixel(x,y,grid)

		
		
		
	def setBG(self, r1, g1, b1, r2, g2, b2):
		if self.res>1: #otherwise repeating pattern will not repeat
			self.i2chandler.setBG(RDsAdrs[0][0], r1, g1, b1, r2, g2, b2)
			self.i2chandler.setBG(RDsAdrs[0][1], r1, g1, b1, r2, g2, b2)
			self.i2chandler.setBG(RDsAdrs[1][0], r1, g1, b1, r2, g2, b2)
			self.i2chandler.setBG(RDsAdrs[1][1], r1, g1, b1, r2, g2, b2)
			
		else:
			self.i2chandler.setBG(RDsAdrs[0][0], r1, g1, b1, r1, g1, b1)
			self.i2chandler.setBG(RDsAdrs[0][1], r2, g2, b2, r2, g2, b2)
			self.i2chandler.setBG(RDsAdrs[1][0], r2, g2, b2, r2, g2, b2)
			self.i2chandler.setBG(RDsAdrs[1][1], r1, g1, b1, r1, g1, b1)								
								
	def setResolution(self, res):
		self.res = res
		self.lowerBoarder = self.mapping[res]
		
		self.i2chandler.setResolution(RDsAdrs[0][0], self.res)
		self.i2chandler.setResolution(RDsAdrs[0][1], self.res)
		self.i2chandler.setResolution(RDsAdrs[1][0], self.res)
		self.i2chandler.setResolution(RDsAdrs[1][1], self.res)		
		
		
		
	def moveUntil(self, x, y, ex, ey, delay):
		if restrictedTo([x,ex],self.lowerBoarder)!=2:
			if restrictedTo([y,ey], self.lowerBoarder)!=2:
				self.i2chandler.moveUntil(RDsAdrs[x/self.res][y/self.res], x%self.res, y%self.res, ex%self.res, ey%self.res, delay) # send to single grid
			
			else:
				self.moveUntilSplit(x,y,ex,ey,1,delay)
		else:
			if restrictedTo([y,ey], self.lowerBoarder)!=2:
				self.moveUntilSplit(x,y,ex,ey,0,delay)
			else:
				pass
		
		
	def movePiece(self,x1, y1, x2, y2):
		if restrictedTo([x1,x2],self.lowerBoarder)!=2 and restrictedTo([y1,y2],self.lowerBoarder)!=2:
			self.i2chandler.movePiece(RDsAdrs[x1/self.res][y1/self.res], x1%self.res, y1%self.res, x2%self.res, y2%self.res)
			
		else:
			self.i2chandler.clearSpace(RDsAdrs[x1/self.res][y1/self.res], x1%self.res, y1%self.res)
			self.i2chandler.drawPixel(RDsAdrs[x2/self.res][y2/self.res], x2%self.res, y2%self.res)
		
		
		
	def clearSpace(self,x,y):
		self.i2chandler.clearSpace(RDsAdrs[x/self.res][y/self.res], x%self.res, y%self.res)
		
		
	
	def drawSprite(self,spriteAddress, size, x, y, list):	
		pass
		
		
		
		
	def setSprite(self, grid, spriteAddress, size, list):
		if grid < 4:
			self.i2chandler.setSprite(RDsAdrs[grid/2][grid%2], spriteAddress, size, list)
		else:
			self.i2chandler.setSprite(RDsAdrs[0][0], spriteAddress, size, list)
			self.i2chandler.setSprite(RDsAdrs[0][1], spriteAddress, size, list)
			self.i2chandler.setSprite(RDsAdrs[1][0], spriteAddress, size, list)
			self.i2chandler.setSprite(RDsAdrs[1][1], spriteAddress, size, list)
		
		
	def displaySprite(self, grid, spriteAddress, x, y):
		if grid < 4:
			self.i2chandler.displaySprite(RDsAdrs[grid/2][grid%2], spriteAddress, x, y)
		else:
			self.i2chandler.setSprite(RDsAdrs[0][0], spriteAddress, x, y)
			self.i2chandler.setSprite(RDsAdrs[0][1], spriteAddress, x, y)
			self.i2chandler.setSprite(RDsAdrs[1][0], spriteAddress, x, y)
			self.i2chandler.setSprite(RDsAdrs[1][1], spriteAddress, x, y)
			
			
			
	def clearSprite(self, grid, spriteAddress):
		if grid < 4:
			self.i2chandler.clearSprite(RDsAdrs[grid/2][grid%2], spriteAddress)
		else:
			self.i2chandler.clearSprite(RDsAdrs[0][0], spriteAddress)
			self.i2chandler.clearSprite(RDsAdrs[0][1], spriteAddress)
			self.i2chandler.clearSprite(RDsAdrs[1][0], spriteAddress)
			self.i2chandler.clearSprite(RDsAdrs[1][1], spriteAddress)
			
			
	def moveSprite(self, grid, spriteAddress, newX, newY):
		if grid < 4:
			self.i2chandler.moveSprite(RDsAdrs[grid/2][grid%2], spriteAddress, newX, newY)
		else:
			self.i2chandler.moveSprite(RDsAdrs[0][0], spriteAddress, newX, newY)
			self.i2chandler.moveSprite(RDsAdrs[0][1], spriteAddress, newX, newY)
			self.i2chandler.moveSprite(RDsAdrs[1][0], spriteAddress, newX, newY)
			self.i2chandler.moveSprite(RDsAdrs[1][1], spriteAddress, newX, newY)
			
	
		
	def printChar(self, x, y, char):
		print "printing char"
		gridX = restrictedTo([x, x+5],self.lowerBoarder)
		gridY = restrictedTo([y, y+7], self.lowerBoarder)
		if gridX !=2:
		

			if gridY != 2:
				print "no split"
				self.i2chandler.printChar(RDsAdrs[gridX][gridY], x%self.lowerBoarder, y%self.lowerBoarder, char)
				
			else:
				print "split char on y axis"
				self.i2chandler.printChar(RDsAdrs[gridX][0], x%self.lowerBoarder, y%self.lowerBoarder, char)
				self.i2chandler.printChar(RDsAdrs[gridX][1], -self.lowerBoarder+x, y%self.lowerBoarder, char)

				
		else:
			if gridY != 2:
				print "split char on x axis"
				self.i2chandler.printChar(RDsAdrs[0][gridY], x%self.lowerBoarder, y%self.lowerBoarder, char)
				self.i2chandler.printChar(RDsAdrs[1][gridY], x%self.lowerBoarder, -self.lowerBoarder+y, char)	
							
			else:
				print "split char on both axises"
				self.i2chandler.printChar(RDsAdrs[0][0], x%self.lowerBoarder, y%self.lowerBoarder, char)
				self.i2chandler.printChar(RDsAdrs[0][1], -self.lowerBoarder+x, y%self.lowerBoarder, char)
				self.i2chandler.printChar(RDsAdrs[1][0], x%self.lowerBoarder, y%self.lowerBoarder, char)
				self.i2chandler.printChar(RDsAdrs[1][1], x%self.lowerBoarder, -self.lowerBoarder+y, char)	

				

						
		
	def clearchar(self, grid, x, y, char):
		if grid < 4:
			self.i2chandler.clearChar(RDsAdrs[grid/2][grid%2], x, y, char)
		else:
			self.i2chandler.clearChar(RDsAdrs[0][0], x, y, char)
			self.i2chandler.clearChar(RDsAdrs[0][1], x, y, char)
			self.i2chandler.clearChar(RDsAdrs[1][0], x, y, char)
			self.i2chandler.clearChar(RDsAdrs[1][1], x, y, char)
	
		
		
	def flashPixel(self):
		pass
		
		
		
		
		
		
	def squareSplit(self, x1,y1,x2,y2):
		gridX = restrictedTo([x1,x2], self.lowerBoarder)
		gridY = restrictedTo([y1,y2], self.lowerBoarder)
		if gridX !=2:
	
			if gridY !=2:
	
				x1 = x1-(self.res*gridX)
				x2 = x2-(self.res*gridX)
			
				y1 = y1-(self.res*gridY)
				y2 = y2-(self.res*gridY)
				
				self.i2chandler.drawSquare(RDsAdrs[gridX][gridY],x1,y1,x2,y2)
			
			else:
			
				self.lineSplit(x1,y1,x1,y2,1)
				self.lineSplit(x2,y1,x2,y2,1)
				
				if y1<y2:
					upX=0
					y2 = y2-self.res
				else:
					upX=1
					y1 = y1-self.res
					
					
				x1 = x1-(self.res*gridX)
				x2 = x2-(self.res*gridX)
					
				self.i2chandler.drawLine(RDsAdrs[gridX][upX], x1,y1,x2,y1)
				self.i2chandler.drawLine(RDsAdrs[gridX][not upX], x1,y2,x2,y2)
				
				
		else:

			if gridY !=2:
				self.lineSplit(x1,y1,x2,y1,0)
				self.lineSplit(x1,y2,x2,y2,0)
				
				if x1<x2:
					upY=0
					x2= x2-8
					
				else:
					upY=1
					x1=x1-8
					
				y1=y1-(self.res*gridY)
				y2=y2-(self.res*gridY)
				
				self.i2chandler.drawLine(RDsAdrs[upY][gridY], x1,y1,x1,y2)
				self.i2chandler.drawLine(RDsAdrs[not upY][gridY], x2,y1, x2,y2)
					
			
			else: # square is in all grids
				self.lineSplit(x1,y1,x2,y1,0)
				self.lineSplit(x1,y2,x2,y2,0)
				self.lineSplit(x1,y1,x1,y2,1)
				self.lineSplit(x2,y1,x2,y2,1)
			
			
			
	
	def lineSplit(self,x1,y1, x2,y2,axis):
		if axis == 0 : # crosses the y-axis only
			yGrid = restrictedTo([y1,y2],self.lowerBoarder)
			#y1 = y1-(self.res*yGrid)
			#y2 = y2-(self.res*yGrid)
			
			if x1 < x2:

				if y1==y2:
					newY1 = y1
					newY2 = y2
				else:
					gradient = (y2 - y1)/(x2 - x1)
					constant = y1 - gradient*x1
					
					newY1 = gradient*self.lowerBoarder + constant
					newY2 = gradient*(self.lowerBoarder+1) + constant
					
					#TODO: introduce res to this function
				self.i2chandler.drawLine(RDsAdrs[0][yGrid],x1,y1,self.lowerBoarder,newY1)
				self.i2chandler.drawLine(RDsAdrs[1][yGrid],0,newY2,x2%self.res,y2%self.res)
				
			else:
				pass
			
				
	
		elif axis == 1 : # cross the x-axis only
			xGrid = restrictedTo([x1,x2],self.lowerBoarder)
			#x1 = x1-(self.res*xGrid)
			#x2 = x2-(self.res*xGrid)
			
			if y1 < y2:

				if x1==x2:
					newX1 = x1
					newX2 = x2
				else:
					gradient = (y2 - y1)/(x2 - x1)
					constant = y1 - gradient*x1
					
					newX1 = gradient*self.lowerBoarder + constant
					newX2 = gradient*(self.lowerBoarder+1) + constant
					
					#TODO: introduce res to this function
				self.i2chandler.drawLine(RDsAdrs[xGrid][0],x1,y1,newX1,self.lowerBoarder)
				self.i2chandler.drawLine(RDsAdrs[xGrid][1],newX2,0,x2%self.res,y2%self.res)
			else:
				pass


		else:
	
			gradient = (y2 - y1)/(x2 - x1)
	
			constant = y1 - gradient*x1
	
			newY1 = gradient*7 + constant
			newY2 = gradient*8 + constant
	
			newX1 = (7 - constant) / gradient
			newX2 = (8 - constant) / gradient
		
					



	def moveUntilSplit(self,x1,y1, x2,y2,axis, delay):
		if axis == 0 : # crosses the y-axis only
			yGrid = restrictedTo([y1,y2],self.lowerBoarder)
			#y1 = y1-(self.res*yGrid)
			#y2 = y2-(self.res*yGrid)
			
			if x1 < x2:

				if y1==y2:
					newY1 = y1
					newY2 = y2
				else:
					gradient = (y2 - y1)/(x2 - x1)
					constant = y1 - gradient*x1
					
					newY1 = gradient*self.lowerBoarder + constant
					newY2 = gradient*(self.lowerBoarder+1) + constant
					
					#TODO: introduce res to this function
				self.i2chandler.moveUntil(RDsAdrs[0][yGrid],x1,y1,self.lowerBoarder,newY1,delay)
				self.i2chandler.moveUntil(RDsAdrs[1][yGrid],0,newY2,x2%self.res,y2%self.res,delay)
				
			else:
				pass
			
				
	
		elif axis == 1 : # cross the x-axis only
			xGrid = restrictedTo([x1,x2],self.lowerBoarder)
			#x1 = x1-(self.res*xGrid)
			#x2 = x2-(self.res*xGrid)
			
			if y1 < y2:

				if x1==x2:
					newX1 = x1
					newX2 = x2
				else:
					gradient = (y2 - y1)/(x2 - x1)
					constant = y1 - gradient*x1
					
					newX1 = gradient*self.lowerBoarder + constant
					newX2 = gradient*(self.lowerBoarder+1) + constant
					
					#TODO: introduce res to this function
				self.i2chandler.moveUntil(RDsAdrs[xGrid][0],x1,y1,newX1,self.lowerBoarder,delay)
				self.i2chandler.moveUntil(RDsAdrs[xGrid][1],newX2,0,x2%self.res,y2%self.res,delay)
			else:
				pass


		else:
	
			gradient = (y2 - y1)/(x2 - x1)
	
			constant = y1 - gradient*x1
	
			newY1 = gradient*7 + constant
			newY2 = gradient*8 + constant
	
			newX1 = (7 - constant) / gradient
			newX2 = (8 - constant) / gradient
		
		
def restrictedTo(list, number):
	first = list.pop()
	
	for x in list:
		if not(first <= number and x <= number) or (first > number and x > number):
			return 2
			
	if first <= number:
		return 0
		
	else:
		return 1
		
		


		
