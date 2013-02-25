

def trythis(qOut, qIn):
	print "trythis"
	while True:
		if not qOut.empty():
			something = qOut.get()
			print something
			somethingelse = "else"
			something = str(something) + somethingelse
			qIn.put(something)
