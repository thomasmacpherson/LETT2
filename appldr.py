import api
emulated = True
LEDGrided = True
LCDed = True
keyboardHacked= True
touch = False

gameList = ('app','orthello','connect4','draughts','inkspill','pixelArt','simon','solitare','tetris','ticTacToe','missionmars','scamper','gridTest','flame')

# 0       1             2           3          4      5           6         7        8         9          10           11    12      
api = api.api(emulated, LEDGrided, LCDed, keyboardHacked, touch)

button = 1 #api.waitForScreenButtonPress()

#while True:
	
gameImport = __import__(gameList[button])

game = gameImport.thisapp(api)
	
	#button = api.waitForScreenButtonPress()
