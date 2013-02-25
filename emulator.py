
import pygame, sys
from pygame.locals import *
#from pygame import gfxdraw

pygame.init()
pygame.display.set_caption('LETT Emulator')
screen = pygame.display.set_mode((1000,700),0,32)


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
pink = (255,100,255)
orange = (255,133,10)
fuchsia = (255,10,133)
purple = (100, 0, 100)
yellow = (245, 250, 10)
turquoise = (0, 255, 240)
lime = (150, 255, 0)
teal = (0,128,128)
olive = (128,128,0)
tan = (139, 90, 43)
slateblue = (113, 113, 198)
salmon = (198,113,113)
maroon = (128,0,0)
melon = (227,168,105)

backgroundColour = (72,209,204)
screen.fill(backgroundColour)


tableX = 100
tableY = 100

tableWidth = 520
tableHeight = 520

pygame.draw.rect(screen, (0,0,0),(tableX, tableY,tableWidth,tableHeight),4)
pygame.draw.rect(screen, (255,255,255),(tableX, tableY,tableWidth,tableHeight),0)

gridX = tableX + 100
gridY = tableY + 100

gridWidth = 20 *16
gridHeight = 20 * 16


modeButtonsX = tableX + 145
modeButtonsY = tableY + 25

modeButtonsWidth = 230
modeButtonsHeight = 50

gameSelectionColours = ((red,turquoise,fuchsia,olive,pink,yellow,green,teal),
			(orange,blue,maroon,tan,slateblue,salmon,purple,melon))

for i in range(2):
	for j in range(8):
		pygame.draw.rect(screen, gameSelectionColours[i][j], ( modeButtonsX + j*30 , modeButtonsY + i*30 ,20,20),0) 
		pygame.draw.rect(screen, (0,0,0), ( modeButtonsX + j*30 , modeButtonsY + i*30 ,20,20),1) 

LCD1X = tableX + 25
LCD1Y = tableX + 190

LCD2X = tableX + 445
LCD2Y = tableY + 190


pygame.draw.rect(screen, (0,0,0),(LCD1X, LCD1Y,50,140),2)
pygame.draw.rect(screen, (0,0,0),(LCD1X+9, LCD1Y+5,32,130),1)

pygame.draw.rect(screen, (0,0,0),(LCD2X, LCD2Y,50,140),2)
pygame.draw.rect(screen, (0,0,0),(LCD2X+9, LCD2Y+5,32,130),1)


font = pygame.font.Font(None, 20)

LCD1Line1= "LCD1 Line 1"
LCD1Line2= "LCD1 Line 2"

LCD2Line1= "LCD2 Line 1"
LCD2Line2= "LCD2 Line 2"

displayLCD1Line1 = font.render(LCD1Line1, 1, (0,0,0))
pygame.transform.rotate(displayLCD1Line1, 90)

displayLCD1Line2 = font.render(LCD1Line2, 1, (0,0,0))
displayLCD2Line1 = font.render(LCD2Line1, 1, (0,0,0))
displayLCD2Line2 = font.render(LCD2Line2, 1, (0,0,0))
	
screen.blit(displayLCD1Line1, (LCD1X, LCD1Y))
screen.blit(displayLCD1Line2, (LCD1X, LCD1Y))
screen.blit(displayLCD2Line1, (LCD2X, LCD2Y))
screen.blit(displayLCD2Line2, (LCD2X, LCD2Y))


#pygame.gfxdraw.aatrigon(screen, 30,30, 60,60, 30, 60, (30,200,100))



mouse_click = False
change = True


gridColours = []
for i in range(16):
	row = []
	for j in range(16):
		row.append((255,255,255))
	gridColours.append(row)

for i in range(16):
	for j in range(16):
		pygame.draw.rect(screen, gridColours[i][j], (gridX+i*20,gridY+j*20,20,20),0) 
		pygame.draw.rect(screen, (0,0,0), (gridX+i*20,gridY+j*20,20,20),2) 



while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
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

           	if event.type == MOUSEBUTTONUP:
			mouse_click = True
               		mousex, mousey = event.pos
			change = True


	if mouse_click:
		if (mousex > gridX and mousex < gridX + gridWidth) and (mousey > gridY and mousey < gridY + gridHeight):
			mousex -= gridX
			mousey -= gridY
		
			mousex = mousex/20
			mousey = mousey/20

			#if mousex == previousMouseX and mousey == previouseMouseY:
				
			#previousMouseX = mousex
			#previousMouseY = mousey

			gridColours[mousex][mousey]=(gridColours[mousex][mousey][0]-40,0,0)


			pygame.draw.rect(screen, gridColours[mousex][mousey], (gridX+mousex*20,gridY+mousey*20,20,20),0) 
			pygame.draw.rect(screen, (0,0,0), (gridX+mousex*20,gridY+mousey*20,20,20),2) 
		elif (mousex > modeButtonsX and mousex < modeButtonsX + modeButtonsWidth) and (mousey > modeButtonsY and mousey < modeButtonsY + modeButtonsHeight):
			for i in range(2):
				for j in range(8):
					if (mousex > modeButtonsX + j*30  and mousex < modeButtonsX + j*30 + 20) and (mousey > modeButtonsY + i*30  and mousey < modeButtonsY + i*30 + 20):
						print i;
						print j;

		mouse_click =False


	#x,y = pygame.mouse.get_pos()
	#x -= mouse_c.get_width()/2
	#y -= mouse_c.get_height()/2

	#for i in range(16):
	#	for j in range(16):
	#		pygame.draw.rect(screen, gridColours[i][j], (gridX+i*20,gridY+j*20,20,20),0) 
	#		pygame.draw.rect(screen, (0,0,0), (gridX+i*20,gridY+j*20,20,20),2) 

	#screen.blit(mouse_c,(x,y))
	if change:
		change = False
		pygame.display.update()
