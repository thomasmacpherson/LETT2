import api

api = api.api(False,False,False,True)

api.i2chandler.setInk(0x14, 0,200,200)
#for i in range(8):
#	for j in range(8):
api.i2chandler.drawPixel(0x14, 0,0)


api.i2chandler.setInk(0x14, 0,0,200)
api.i2chandler.drawPixel(0x14, 0,1)

api.i2chandler.setInk(0x14, 200,0,0)
api.i2chandler.drawPixel(0x14, 1,0)


api.i2chandler.setInk(0x14, 0,200,0)
api.i2chandler.drawPixel(0x14, 1,1)

api.i2chandler.setInk(0x14, 200,200,0)
api.i2chandler.drawPixel(0x14, 2,0)


api.i2chandler.setInk(0x14, 255, 80,   0)
api.i2chandler.drawPixel(0x14, 2,1)
