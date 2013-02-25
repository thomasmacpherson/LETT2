
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
		self.api.qOut.put(1)
		display=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		self.api.printtoscreen(display)
		display[0][1] = 1
		print " "
		self.api.printtoscreen(display)
		
		self.api.readInput()
		#print "and here"
		print self.api.qIn.get()
