
class thisapp:
	
	def __init__(self, api):
		self.api = api
		self.api.set
		self.api.setBG()
		self.api.setResolution()
		self.api.waitForInput(inputReceived)
		
		
	def inputReceived(self, [x,y]):
		self.api.setInk(200,200,0,4)
		self.api.drawPixel(x,y)
	
	def somethinghappens(self):
		self.api.drawPixel(
