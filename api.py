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
		
		self.i2chandler = i2cHandler.handler(self.qOut)
		self.emulated = emulated
		
		if emulated:
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
		self.qIn.get()
		return 
		
	def checkForInput(self):
		pass
		
	def drawSquare(self):
		i2chandler.const.CMD_DRAW_SQUARE
		
	def drawLine(self,x,y,ex,ey):
		self.i2chandler.drawLine(RDsAdrs[0][0], x, y, ex, ey)
		
	def setInk(self, r, g, b):
		self.i2chandler.setInk(RDsAdrs[0][0], r, g, b)
		
		
	def drawPixel(self, x, y):
		xGrid = restrictedTo([x],7)
		yGrid = restrictedTo([y],7)
		self.i2chandler.drawPixel(RDsAdrs[xGrid][yGrid], x, y)
		
		
		
	def setBG(self, r1, g1, b1, r2, g2, b2):
		self.i2chandler.setBG(RDsAdrs[0][0], r1, g1, b1, r2, g2, b2)
		self.i2chandler.setBG(RDsAdrs[0][1], r1, g1, b1, r2, g2, b2)
		self.i2chandler.setBG(RDsAdrs[1][0], r1, g1, b1, r2, g2, b2)
		self.i2chandler.setBG(RDsAdrs[1][1], r1, g1, b1, r2, g2, b2)
						
								
	def setResolution(self):
		pass
	def moveUntil(self):
		pass
	def movePiece(self):
		pass
	def clearSpace(self):
		pass
	def printChar(self):
		pass
	def setSprite(self):
		pass
	def flashPixel(self):
		pass
		
		
def restrictedTo(list, number):
	first = list.pop()
	
	for x in list:
		if not(first <= number and x <= number) or (first > number and x > number):
			return 1
			
	if first <= number:
		return 0
		
	else:
		return 2
		
'''		
		

def split():
	if restrictedTo(xlist, number)!= 1 :
		if restrictedTo(yList, number)!=1: #check if contained within one grid
		# send cmd as contained in one grid
			pass
	
	else :
		if restrictedTo(yList, number)!=1:
				pass

	def lineSplit(x,y,ex,ey, axis):
	 
	
	
	
	gradient = (ey - y)/(ex - x)
	
	constant = y - gradient*x
	
	newY1 = gradient*7 + constant
	newY2 = gradient*8 + constant
	
	newX1 = (7 - constant) / gradient
	newX2 = (8 - constant) / gradient



def squareSplit(x1,y1,x2,y2,x3,y3,x4,y4,axis):
	lineSplit(x1,y1,x2,y2)
	lineSplit(x2,y2,x3,y3)
	lineSplit(x3,y3,x4,y4)	
	lineSplit(x4,y4,x1,y1)		
	'''	
		
		
'''	
	def writeToLCD(self, LCD, message):
		if emulated:
			self.emu.writeToLCD(LCD, message)
		
	
'''