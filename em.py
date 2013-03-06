import pygame, sys
from pygame.locals import *

#from pygame import gfxdraw


import const

const.red = (255,0,0)
const.green = (0,255,0)
const.blue = (0,0,255)
const.white = (255,255,255)
const.black = (0,0,0)
const.pink = (255,100,255)
const.orange = (255,133,10)
const.fuchsia = (255,10,133)
const.purple = (100, 0, 100)
const.yellow = (245, 250, 10)
const.turquoise = (0, 255, 240)
const.lime = (150, 255, 0)
const.teal = (0,128,128)
const.olive = (128,128,0)
const.tan = (139, 90, 43)
const.slateblue = (113, 113, 198)
const.salmon = (198,113,113)
const.maroon = (128,0,0)
const.melon = (227,168,105)

const.tableX = 100
const.tableY = 100

const.tableWidth = 520
const.tableHeight = 520

const.gridX = const.tableX + 100
const.gridY = const.tableY + 100

const.gridWidth = 20 *16
const.gridHeight = 20 * 16



const.modeButtonsX = const.tableX + 25
const.modeButtonsY = const.tableY + 145

const.modeButtonsWidth = 50
const.modeButtonsHeight = 230

const.gameSelectionColours = ((const.red,const.turquoise),(const.fuchsia,const.olive),(const.pink,const.yellow),(const.green,const.teal),
			(const.orange,const.blue),(const.maroon,const.tan),(const.slateblue,const.salmon),(const.purple,const.melon))

const.LCDX = const.tableX + 190
const.LCDY = [const.tableX + 25, const.tableY + 445]

const.LCDXtext = const.LCDX + 9
const.LCDYtext = [[const.LCDY[0] + 11,const.LCDY[0] + 25],[const.LCDY[1] + 11, const.LCDY[1] + 25]]



const.LCDOuterWidth = 140
const.LCDOuterHeight = 50
const.LCDInnerWidth = 130
const.LCDInnerHeight = 32



class em:
	def __init__(self,qOut,qIn):
		#self.qOut = qOut
		#self.qIn = qIn
		self.pygame = pygame
		self.pygame.init()
		pygame.display.set_caption('LETT Emulator')
		self.screen = pygame.display.set_mode((1000,700),0,32)

		self.font = pygame.font.Font(None, 18)
		self.setBGColour(200,200,0)

		self.ink = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
		
		self.LCDTexts= [["LCD1 Line 1","LCD1 Line 2"],["LCD2 Line 1","1234567890123456"]]
		
		self.drawTable()
		#self.pygame.display.flip()
		self.drawButtons()
		self.drawBlankScreen()
		self.drawLCDOutline()
		self.writeLCD(3, "hello")
		self.refreshScreen()

		
		
	def screenPrint(self,display):
		print display[0]
		print display[1]
		print display[2]
		print display[3]
	
	
	def input(self):
		self.qIn.put(raw_input('-->'))
		#print "here"

	def writeToLCDs(self):
		pass


	def refreshScreen(self):
		#if change:
			#change = False
		#self.pygame.display.update()
		self.pygame.display.flip()
	
	
	
	def drawBlankScreen(self):		
		self.gridColours = []
		for i in range(16):
			row = []
			for j in range(16):
				row.append((255,255,255))
			self.gridColours.append(row)

		for i in range(16):
			for j in range(16):
				self.pygame.draw.rect(self.screen, self.gridColours[i][j], (const.gridX+i*20,const.gridY+j*20,20,20),0) 
				self.pygame.draw.rect(self.screen, (0,0,0), (const.gridX+i*20,const.gridY+j*20,20,20),2) 





	def setBGColour(self, r, g, b): #call at startup to set the 'table' colour
		self.backgroundColour = r, g, b
		self.screen.fill(self.backgroundColour)

	def setInk(self, r, g, b, grid):
		if grid >= 4:
			for i in range(0,4):
				self.ink[i][0]=r
				self.ink[i][1]=g
				self.ink[i][2]=b
		else:
			self.ink[grid][0]=r
			self.ink[grid][1]=g
			self.ink[grid][2]=b
			
			
	def drawTable(self):
		self.pygame.draw.rect(self.screen, (0,0,0),(const.tableX, const.tableY, const.tableWidth, const.tableHeight),4)
		self.pygame.draw.rect(self.screen, (255,255,255),(const.tableX, const.tableY, const.tableWidth, const.tableHeight),0)

	def waitForScreenPixelPress(self):
		print "waiting for screen pixel press in em"
		while True:
			for event in self.pygame.event.get():
				if event.type == MOUSEBUTTONUP:
					mousex, mousey = event.pos
					print mousex
					
					if ((mousex > const.gridX) and (mousex < (const.gridX + const.gridWidth))) and ((mousey > const.gridY) and( mousey < (const.gridY + const.gridHeight))):
						mousex -= const.gridX
						mousey -= const.gridY
						
						mousex = mousex/20
						mousey = mousey/20
						return [mousex, mousey]
	
	def drawButtons(self):
		for i in range(8):
			for j in range(2):
				self.pygame.draw.rect(self.screen, const.gameSelectionColours[i][j], ( const.modeButtonsX + j*30 , const.modeButtonsY + i*30 ,20,20),0) 
				self.pygame.draw.rect(self.screen, (0,0,0), ( const.modeButtonsX + j*30 , const.modeButtonsY + i*30 ,20,20),1) 

	
	
						
						
	def drawPixel(self, x, y, grid):
		
		self.gridColours[x][y]=(self.ink[grid])
		self.pygame.draw.rect(self.screen, self.gridColours[x][y], (const.gridX+x*20,const.gridY+y*20,20,20),0) 
		self.pygame.draw.rect(self.screen, (0,0,0), (const.gridX+x*20,const.gridY+y*20,20,20),2) 
		self.refreshScreen()

						



	def drawLCDOutline(self):
		self.pygame.draw.rect(self.screen, (0,0,0),(const.LCDX, const.LCDY[0], const.LCDOuterWidth,const.LCDOuterHeight),2)
		self.pygame.draw.rect(self.screen, (0,0,0),(const.LCDX+5, const.LCDY[0]+9,const.LCDInnerWidth, const.LCDInnerHeight),1)

		self.pygame.draw.rect(self.screen, (0,0,0),(const.LCDX, const.LCDY[1],const.LCDOuterWidth,const.LCDOuterHeight),2)
		self.pygame.draw.rect(self.screen, (0,0,0),(const.LCDX+5, const.LCDY[1]+9,const.LCDInnerWidth, const.LCDInnerHeight),1)



	def writeLCD(self, LCD, message):
		if len(message) > 16:
			return 0
			
		if LCD <4:
			displayText = self.font.render(message ,1, (0,0,0)) #black
			self.screen.blit(displayText, (const.LCDXtext, const.LCDYtext[LCD/2][LCD%2]))			
			
		elif LCD == 4:
			displayText = self.font.render(message ,1, (0,0,0)) #black
			self.screen.blit(displayText, (const.LCDXtext, const.LCDYtext[LCD/2][LCD%2]))
			
			displayText = self.font.render(message ,1, (0,0,0)) #black
			self.screen.blit(displayText, (const.LCDXtext, const.LCDYtext[LCD/2][LCD%2]))
			
		return 1	
			
		'''	
		elif LCD == 5:
		
			
			displayLCD1Line1 = self.font.render(self.LCD1Line1, 1, (0,0,0))
		
			displayLCD1Line2 = self.font.render(self.LCD1Line2, 1, (0,0,0))
			displayLCD2Line1 = self.font.render(self.LCD2Line1, 1, (0,0,0))
			displayLCD2Line2 = self.font.render(self.LCD2Line2, 1, (0,0,0))
	
			self.screen.blit(displayLCD1Line1, (const.LCD1Xtext, const.LCD1YtextLine1))
			self.screen.blit(displayLCD1Line2, (const.LCD1Xtext, const.LCD1YtextLine2))
			self.screen.blit(displayLCD2Line1, (const.LCD2Xtext, const.LCD2YtextLine1))
			self.screen.blit(displayLCD2Line2, (const.LCD2Xtext, const.LCD2YtextLine2))
		'''




	'''
	def waitForControlPress(self):	#physical buttons, must move this as requires optional emulator to be running
		while True:
			for event in self.pygame.event.get():
				if event.type==QUIT:
					self.pygame.quit()
					self.sys.exit()
					
				if event.type==KEYDOWN:
					if event.key==K_LEFT:
						pass
					elif event.key==K_RIGHT:
						pass
					elif event.key==K_UP:
						pass
					elif event.key==K_DOWN:
						pass

				if event.type==KEYUP:
					if event.key==K_LEFT:
						pass
					elif event.key==K_RIGHT:
						pass
					elif event.key==K_UP:
						pass
					elif event.key==K_DOWN:
						pass


	def waitForScreenPress():
		if event.type == MOUSEBUTTONUP:
			mouse_click = True
          	mousex, mousey = event.pos
    		change = True
	

	def waitForButtonScreenPress(self):
		if (mousex > modeButtonsX and mousex < modeButtonsX + modeButtonsWidth) and (mousey > modeButtonsY and mousey < modeButtonsY + modeButtonsHeight):
			for i in range(2):
				for j in range(8):
					if (mousex > modeButtonsX + j*30  and mousex < modeButtonsX + j*30 + 20) and (mousey > modeButtonsY + i*30  and mousey < modeButtonsY + i*30 + 20):
						print i;
						print j;	
						
						


			#if mousex == previousMouseX and mousey == previouseMouseY:
				
			#previousMouseX = mousex
			#previousMouseY = mousey



	#x,y = pygame.mouse.get_pos()
	#x -= mouse_c.get_width()/2
	#y -= mouse_c.get_height()/2

	#for i in range(16):
	#	for j in range(16):
	#		pygame.draw.rect(screen, gridColours[i][j], (gridX+i*20,gridY+j*20,20,20),0) 
	#		pygame.draw.rect(screen, (0,0,0), (gridX+i*20,gridY+j*20,20,20),2) 

	#screen.blit(mouse_c,(x,y))

	'''