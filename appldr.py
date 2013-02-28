import api
emulated = True

gameList = ('app','orthello','connect4','draughts','inkspill','pixelArt','simon','solitare','tetris','ticTacToe','missionmars')

api = api.api(emulated)

button = 0 #api.waitForScreenButtonPress()

while True:
	
	gameImport = __import__(gameList[button])

	game = gameImport.thisapp(api)
	
	button = api.waitForScreenButtonPress()
