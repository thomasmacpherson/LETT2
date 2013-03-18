import api
emulated = True
LEDGrided = False
LCDed = True
keyboardHacked= False

gameList = ('app','orthello','connect4','draughts','inkspill','pixelArt','simon','solitare','tetris','ticTacToe','missionmars')

api = api.api(emulated, LEDGrided, LCDed, keyboardHacked)

button = 9 #api.waitForScreenButtonPress()

while True:
	
	gameImport = __import__(gameList[button])

	game = gameImport.thisapp(api)
	
	#button = api.waitForScreenButtonPress()
