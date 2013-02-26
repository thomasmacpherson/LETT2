import Queue
#import RPi.GPIO as GPIO
import i2cHandler


class api:
	def __init__(self, emulated):
		self.qOut= Queue.Queue(maxsize=0)
		self.qIn = Queue.Queue(maxsize=0)
		
		self.i2chandler = i2cHandler.handler(self.qOut)
		self.emulated = emulated
		
		#if emulated:
		import em
		self.qOutEmulated = Queue.Queue(maxsize=0)
		self.emu = em.em(self.qOutEmulated, self.qIn)

	def printsomething(self):
		print "something"
	
	def printtoscreen(self,display):
		self.emu.screenPrint(display)
	
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
		pass
	def drawLine(self):
		pass
	def drawPixel(self):
		pass
	def setBG(self, r1, g1, b1, r2, g2, b2):
		pass
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
		
	
	def writeToLCD(self, LCD, message):
		if emulated:
			self.emu.writeToLCD(LCD, message)
		
	
	