import api
emulated = True
LEDGrided = True
LCDed = False
keyboardHacked = True
touch = False

gameList = ('app','orthello','connect4','draughts','inkspill','pixelArt','simon','solitare','tetris','ticTacToe','missionmars','scamper','gridTest','flame')

# 0       1             2           3          4      5           6         7        8         9          10           11    12      
api = api.api(emulated, LEDGrided, LCDed, keyboardHacked, touch)

button = 4 #api.waitForScreenButtonPress()

#while True:
	
gameImport = __import__(gameList[button])
print "ldr1"
game = gameImport.thisapp(api)
print "ldr2"
	#button = api.waitForScreenButtonPress()
