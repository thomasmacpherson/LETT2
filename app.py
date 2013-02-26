
class thisapp:
	
	def __init__(self, api):
		self.api = api
		self.api.set
		self.api.setBG()
		self.api.setResolution()
		self.api.waitForInput(inputReceived)
		
		
	def inputReceived(self):
		self.api.printsomething()
	
	def somethinghappens(self):
		self.api.drawPixel(
