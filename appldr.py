import api
emulated = True

gameList = ('orthello','connect4','draughts','inkspill','pixelArt','simon','solitare','tetris','ticTacToe','missionmars')

api = api.api(emulated)

button = api.waitForScreenButtonPress()

while True:
	
	gameImport = __import__(gameList[button])

	game = gameImport.thisapp(api)
	
	button = api.waitForScreenButtonPress()
