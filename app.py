
class thisapp:
	
	def __init__(self, api):
		self.api = api
		self.api.set
		self.api.setBG()
		self.api.setResolution()
		self.api.waitForInput(inputReceived)
		
		
	def inputReceived(self, list):
		self.api.setInk(200,200,0,4)
		self.api.drawPixel(list[0],list[1])
	