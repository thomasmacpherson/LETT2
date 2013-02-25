def startThis(queue):
	while True:
		answer = queue.get()
		if answer ==1:
			print "one"
		elif answer == "this":
			print "this"
			break
		elif answer == 2:
			print "two"
		print "."