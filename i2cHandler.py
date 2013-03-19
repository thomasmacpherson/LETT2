#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3 

# SK Pang Electronics June 2012

import smbus as smbus
import sys
import getopt
import time 
import const
import lcd

const.rdComm = 114
const.rev2 = False

const.res = 16 # length in pixel
const.numberOfRDs = pow((16/8),2)
const.MAX_WIRE_CMD  =        0x80

const.CMD_NOP       =        0x00

const.CMD_SWAP_BUF  =        0x10
const.CMD_COPY_FRONT_BUF =   0x11
const.CMD_SHOW_AUX_BUF   =   0x12

const.CMD_CLEAR_BUF       =  0x20
const.CMD_SET_PAPER       =  0x21
const.CMD_SET_INK         =  0x22
const.CMD_CLEAR_PAPER     =  0x25
const.CMD_DRAW_PIXEL    =    0x26
const.CMD_DRAW_LINE     =    0x27
const.CMD_DRAW_SQUARE    =   0x28
const.CMD_PRINT_CHAR     =   0x2A
const.CMD_DRAW_ROW_MASK  =   0x2B

const.CMD_SET_BOARD_BG   =   0x2C
const.CMD_SET_BOARD_SIZE =   0x2D
const.CMD_MOVE_UNTIL    =   0x2E
const.CMD_CLEAR_SPACE     =  0x2F

const.CMD_SET_SPRITE      =  0x30
const.CMD_ADD_TO_SPRITE   =  0x31
const.CMD_DISPLAY_SPRITE = 0x32
const.CMD_CHANGE_SPRITE_SIZE = 0x33
const.CMD_FLASH_PIXEL     =  0x34
const.CMD_FLASH_SPRITE    =  0x35
const.CMD_MOVE_PIECE		= 0x36
const.CMD_CLEAR_SPRITE		= 0x37
const.CMD_MOVE_SPRITE		= 0x38


const.CMD_CLEAR_CHAR		= 0x40


const.CMD_totalArgs = [
#  0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - A - B - C - D - E - F 
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 0 - 0x00 -> 0x0F
	0,  2,  1,  2,  1,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,    # 1 - 0x10 -> 0x1F
	3,  3,  3,  0,  0,  0,  2,  4,  4,  0,  3,  3,  6,  1,  5,  2,    # 2 - 0x20 -> 0x2F
	0,  -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 3 - 0x30 -> 0x3F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 4 - 0x40 -> 0x4F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 5 - 0x50 -> 0x5F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 6 - 0x60 -> 0x6F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0     # 7 - 0x70 -> 0x7F
# 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - A - B - C - D - E - F 
]



class handler:
	def __init__(self, qOut, LEDGrided, LCDed):
		self.LCDed = LCDed
		self.LEDGrided = LEDGrided
		self.qOut = qOut
		self.bus = smbus.SMBus(const.rev2)
		
		if self.LCDed:
			self.setUpLCD()
			
		self.packetNumber = 0


	def setUpLCD(self):
		self.lcd = lcd.lcd(self.bus)
		
		
	def writeLCD(self, LCD, line, message):
		if LCD < 2:
			self.lcd.writeLCD(LCD, line, message)
		else:
			self.lcd.writeLCD(0, line, message)
			self.lcd.writeLCD(1, line, message)
			
			
					
	def sendWireCommand(self, add, RDCMD):

		stayInLoop = True
		
		while stayInLoop:
			stayInLoop = False
			try:
				self.bus.write_i2c_block_data(add,self.packetNumber,RDCMD)
				time.sleep(0.05)
			except:
				stayInLoop = True
		
		self.packetNumber +=1
		
		
	
	def drawPixel(self, address, x,y):
		self.sendWireCommand(address,[const.CMD_DRAW_PIXEL, x, y])


	def setBG(self, address, r1, g1, b1, r2, g2, b2):
		self.sendWireCommand(address,[const.CMD_SET_BOARD_BG, r1, g1, b1, r2, g2, b2])
	
	
	def setInk(self, address, r, g, b):	
		self.sendWireCommand(address,[const.CMD_SET_INK, r, g, b])	
		
		
	def drawLine(self, address, x1, y1, x2, y2):
		self.sendWireCommand(address,[const.CMD_DRAW_LINE, x1, y1, x2, y2])
		
	def drawSquare(self,address, x1, y1, x2, y2):
		self.sendWireCommand(address, [const.CMD_DRAW_SQUARE, x1, y1, x2, y2])

	def movePiece(self, address, x1, y1, x2, y2):
		self.sendWireCommand(address,[const.CMD_MOVE_PIECE, x1, y1, x2, y2])


	def clearSpace(self, address, x, y):
		self.sendWireCommand(address,[const.CMD_CLEAR_SPACE, x, y])


	def setResolution(self, address, res):
		self.sendWireCommand(address,[const.CMD_SET_BOARD_SIZE, res])


	def moveUntil(self, address, x1, y1, x2, y2, delay):
		self.sendWireCommand(address,[const.CMD_MOVE_UNTIL, x1, y1, x2, y2, delay])


	def setSprite(self, address, spriteSize, spriteAddress, spriteValues):
	    spriteValues.insert(0,spriteAddress)
	    spriteValues.insert(0,spriteSize)
	    spriteValues.insert(0,const.CMD_SET_SPRITE)
	    self.sendWireCommand(address,spriteValues)
			
				
	def displaySprite(self, address, spriteAddress, x, y):
		self.sendWireCommand(address,[const.CMD_DISPLAY_SPRITE, spriteAddress, x, y])
		
		
	def clearSprite(self, address, spriteAddress):
		self.sendWireCommand(address,[const.CMD_CLEAR_SPRITE, spriteAddress])
		
		
	def moveSprite(self, address, spriteAddress, newX, newY):
		self.sendWireCommand(address,[const.CMD_MOVE_SPRITE, spriteAddress, newX, newY])
		
		
	def flashSprite(self, address):
		self.sendWireCommand(address,[const.CMD_FLASH_SPRITE, x, y])

	def changeSpriteSize(self, address):
		self.sendWireCommand(address,[const.CMD_CHANGE_SPRITE_SIZE, x, y])
		
	def addToSprite(self, address):
		pass
					

	def printChar(self, address, x, y, char):
		print "i2c printing char"
		self.sendWireCommand(address,[const.CMD_PRINT_CHAR, x, y, char])

	def clearChar(self, address, x, y, char):
		self.sendWireCommand(address,[const.CMD_CLEAR_CHAR, x, y, char])
		
		
	
	def flashPixel(self, x, y):
		self.sendWireCommand(address,[const.CMD_FLASH_PIXEL, x, y])
		
				
'''     	
      	
      	
def toByte(i):
	return map(i, -128, 127, 0, 255)

'''