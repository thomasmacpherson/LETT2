class thisapp():

	def __init__(self, api):
		self.api = api
		self.api.clearPacketCount()
		self.api.setInk(255,0,0,4)

		for i in range(0,8):
			for j in range(0,8):
				for k in range(0,2):
					for l in range(0,2):
						self.api.drawPixel(i+(k*8),j+(l*8))

		self.api.setInk(0,255,0,4)
		for i in range(0,8):
			for j in range(0,8):
				for k in range(0,2):
					for l in range(0,2):
						self.api.drawPixel(i+(k*8),j+(l*8))

		self.api.setInk(0,0,255,4)
		for i in range(0,8):
			for j in range(0,8):
				for k in range(0,2):
					for l in range(0,2):
						self.api.drawPixel(i+(k*8),j+(l*8))
