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



const.modeButtonsX = const.tableX + 145
const.modeButtonsY = const.tableY + 25

const.modeButtonsWidth = 230
const.modeButtonsHeight = 50

gameSelectionColours = ((const.red,const.turquoise,const.fuchsia,const.olive,const.pink,const.yellow,const.green,const.teal),
			(const.orange,const.blue,const.maroon,const.tan,const.slateblue,const.salmon,const.purple,const.melon))

const.LCD1X = const.tableX + 25
const.LCD1Y = const.tableX + 190

const.LCD2X = const.tableX + 445
const.LCD2Y = const.tableY + 190


#font = pygame.font.Font(None, 20)

LCD1Line1= "LCD1 Line 1"
LCD1Line2= "LCD1 Line 2"

LCD2Line1= "LCD2 Line 1"
LCD2Line2= "LCD2 Line 2"






class em:
	def __init__(self,qOut,qIn):
		self.qOut = qOut
		self.qIn = qIn
		self.pygame = pygame
		self.pygame.init()
		pygame.display.set_caption('LETT Emulator')
		self.screen = pygame.display.set_mode((1000,700),0,32)
		self.setBGColour(200,200,200)
		self.drawTable()
		self.drawButtons()
		self.drawScreenPixels()
		
		
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
		if change:
			change = False
			self.pygame.display.update()
	
	
	
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
		self.backgroundColour = (72,209,204)
		self.screen.fill(self.backgroundColour)



	def drawTable(self):
		self.pygame.draw.rect(self.screen, (0,0,0),(const.tableX, const.tableY, const.tableWidth, const.tableHeight),4)
		self.pygame.draw.rect(self.screen, (255,255,255),(const.tableX, const.tableY, const.tableWidth, const.tableHeight),0)

	def waitForScreenPixelPress(self):
		while True:
			for event in self.pygame.event.get():
				if event.type == MOUSEBUTTONUP:
				    mousex, mousey = event.pos
				
					if (mousex > const.gridX and mousex < const.gridX + const.gridWidth) and (mousey > const.gridY and mousey < const.gridY + const.gridHeight):
						mousex -= const.gridX
						mousey -= const.gridY
	
						mousex = mousex/20
						mousey = mousey/20
						return [mousex, mousey]
						
'''						
	def drawScreenPixel(self):
		self.gridColours[mousex][mousey]=(gridColours[mousex][mousey][0]-40,0,0)
		self.pygame.draw.rect(self.screen, gridColours[mousex][mousey], (gridX+mousex*20,gridY+mousey*20,20,20),0) 
		self.pygame.draw.rect(self.screen, (0,0,0), (const.gridX+mousex*20,gridY+mousey*20,20,20),2) 


		mouse_click =False #dont know where to put this
						




	def drawButtons(self):
		for i in range(2):
			for j in range(8):
				self.pygame.draw.rect(self.screen, gameSelectionColours[i][j], ( modeButtonsX + j*30 , modeButtonsY + i*30 ,20,20),0) 
				self.pygame.draw.rect(self.screen, (0,0,0), ( modeButtonsX + j*30 , modeButtonsY + i*30 ,20,20),1) 


	def drawLCDOutline(self):
		self.pygame.draw.rect(screen, (0,0,0),(LCD1X, LCD1Y,50,140),2)
		self.pygame.draw.rect(screen, (0,0,0),(LCD1X+9, LCD1Y+5,32,130),1)

		self.pygame.draw.rect(screen, (0,0,0),(LCD2X, LCD2Y,50,140),2)
		self.pygame.draw.rect(screen, (0,0,0),(LCD2X+9, LCD2Y+5,32,130),1)



	def writeLCD(self, LCD, message):
		
		if LCD <2:
			pass
		else:
			
			#displayLCD1Line1 = font.render(LCD1Line1, 1, (0,0,0))
			#pygame.transform.rotate(displayLCD1Line1, 90)

			#displayLCD1Line2 = font.render(LCD1Line2, 1, (0,0,0))
			#displayLCD2Line1 = font.render(LCD2Line1, 1, (0,0,0))
			#displayLCD2Line2 = font.render(LCD2Line2, 1, (0,0,0))
	
			#screen.blit(displayLCD1Line1, (LCD1X, LCD1Y))
			#screen.blit(displayLCD1Line2, (LCD1X, LCD1Y))
			#screen.blit(displayLCD2Line1, (LCD2X, LCD2Y))
			#screen.blit(displayLCD2Line2, (LCD2X, LCD2Y))
			


			mouse_click = False
			change = True



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
'''

	'''		

	def waitForButtonScreenPress(self):
		if (mousex > modeButtonsX and mousex < modeButtonsX + modeButtonsWidth) and (mousey > modeButtonsY and mousey < modeButtonsY + modeButtonsHeight):
			for i in range(2):
				for j in range(8):
					if (mousex > modeButtonsX + j*30  and mousex < modeButtonsX + j*30 + 20) and (mousey > modeButtonsY + i*30  and mousey < modeButtonsY + i*30 + 20):
						print i;
						print j;	
						
						
'''

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

