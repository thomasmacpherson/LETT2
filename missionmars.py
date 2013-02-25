import random

load sprite
move sprite right accross screen

level = 1
towerHeights = []
for i in range(0,16):
	towerHeights.append(random.random(0,level+1)
	
inputreceived():
	moveUntil(13, towerHeights-1) #falling bomb
	if towerHeights[x] >0:
		towerHeights[x]-=1 #tower height reduced
	
buildTowers():
	for i in range(0,16):
		self.api.drawLine(i,0,i,towerHeights[i],r,g,b)
		