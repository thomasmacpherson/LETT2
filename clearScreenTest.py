import api
api = api.api(False,True,False,False)

api.setInk(200,0,0,4)

for i in range (0,16):
	for j in range(0,16):
		api.drawPixel(i,j)

api.clearScreen(4)

