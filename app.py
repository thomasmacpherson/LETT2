
class thisapp:

		
	def inputReceived(self, list):
		self.api.setInk(200,200,0,4)
		self.api.drawPixel(list[0],list[1])
	
		
	def __init__(self, api):
		self.api = api
		list = self.api.waitForInput()
		self.inputReceived(list)
		
