
class thisapp:

		
	def inputReceived(self, list):
		self.api.setInk(200,200,0,4)
		self.api.moveUntil(0,list[1],7,list[1],500)
	
		
	def __init__(self, api):
		self.api = api
		while True:
			list = self.api.waitForInput()
			self.inputReceived(list)
		
