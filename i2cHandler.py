#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3 

# SK Pang Electronics June 2012

import smbus
import sys
import getopt
import time 
import const


const.rdComm = 114

const.res = 16 # length in pixel
const.numberOfRDs = pow((res/8),2)
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
const.CMD_MOVE_UNTIl     =   0x2E
const.CMD_CLEAR_SPACE     =  0x2F

const.CMD_SET_SPRITE      =  0x30
const.CMD_ADD_TO_SPRITE   =  0x31
const.CMD_CHANGE_SPRITE_COLOUR = 0x32
const.CMD_CHANGE_SPRITE_SIZE = 0x33
const.CMD_FLASH_PIXEL     =  0x34
const.CMD_FLASH_SPRITE    =  0x35



CMD_totalArgs[MAX_WIRE_CMD] = [
#  0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - A - B - C - D - E - F 
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 0 - 0x00 -> 0x0F
	0,  2,  1,  2,  1,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,    # 1 - 0x10 -> 0x1F
	3,  3,  3,  0,  0,  0,  2,  4,  4,  0,  3,  3,  6,  1,  5,  2,    # 2 - 0x20 -> 0x2F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 3 - 0x30 -> 0x3F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 4 - 0x40 -> 0x4F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 5 - 0x50 -> 0x5F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 6 - 0x60 -> 0x6F
	0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0     # 7 - 0x70 -> 0x7F
# 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - A - B - C - D - E - F 
]



class handler:
	def __init_(self, qOut):
		self.qOut = qOut
		bus = smbus.SMBus(0)



		RDsAdrs=[]
		RainbowCMD=[]

		baseAdr = 0x40

		for i in range(0,4):
			RDsAdrs[i] = baseAdr + i




	def sendCMD(self, address, CMD, arguments):
		sendWireCommand(address, t)      # Transmit the command via I2C


	def sendWireCommand(self, add, len):
		bus.write_i2c_block_data(add,RainbowCMD[0:len+2]) 
		time.sleep(5)
		

	def drawSquare(self,address, x1, y1, x2, y2):
		RDCMD = [CMD_DRAW_SQUARE, x1, y1, x2, y2]
		sendWireCommand(address, RDCMD,CMD_total_Args[CMD_DRAW_SQUARE])
		
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
      	
      	
      	
def toByte(i):
	return map(i, -128, 127, 0, 255)

