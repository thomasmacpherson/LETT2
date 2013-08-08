import api
import time

eight = True

api = api.api(True,True,False,False)




api.setInk(0,200,0,4)
'''
for i in range(8):
	for j in range(8):
		api.drawPixel(i,j)

'''
time.sleep(2)
api.setInk(0,0,200,4)
if eight:
	#api.setSprite(1,0,8,[0b10111111,0b10000001,0b10000001,0b10000001,0b10000001,0b10000001,0b10000001,0b11011111])
        api.setSprite(0,0,8,[0b10000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000])
	api.setSprite(1,0,8,[0b10000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000])

        api.displaySprite(0,0,8,0,0)
	api.displaySprite(1,0,8,0,0)

	time.sleep(2)
#	api.displaySprite(1,0,8, 0,0)
	time.sleep(2)

	api.addToSprite(0,0,8,1,0,[0b11111111])
	api.addToSprite(0,0,8,0,1,[0b11111111])
	api.addToSprite(0,0,8,1,1,[0b11111111])

	api.addToSprite(1,0,8,2,0,[0b11111111])
	api.addToSprite(1,0,8,0,2,[0b11111111])
	api.addToSprite(1,0,8,2,2,[0b11111111])

	api.setInk(255,0,0,4)

	api.displaySprite(0,0,8,0,0)
	api.displaySprite(1,0,8,0,0)

	time.sleep(1)
	api.moveSprite(0,0,8, 0,0, 4,4)
	api.moveSprite(1,0,8, 0,0, 4,4)

else:

	api.setSprite(1,0,4,[0b10010110, 0b01101001])
	api.displaySprite(1,0,4, 0,0)
	time.sleep(2)
	api.drawPixel(7,7)
	time.sleep(1)
	api.addToSprite(1,0,4,1,0,[0b11111111])
	api.addToSprite(1,0,4,2,1,[0b11111111])
	api.addToSprite(1,0,4,2,3,[0b11111111])


	api.setInk(200,0,0,4)
	api.displaySprite(1,0,4,0,0)

	time.sleep(1)

	api.moveSprite(1,0,4, 0,0, 2,3)

while True:
	pass
