import time
import importreftest2
import Queue
import threading

qOut= Queue.Queue(maxsize=0)

qIn = Queue.Queue(maxsize=0)

qOut.put(1)
qOut.put(2)
qOut.put("hello")

print "here"


t = threading.Thread(target = importreftest2.trythis, args = (qOut,qIn,))
t.start()


qOut.put("maz smells great")

qOut.put(1)
qOut.put(2)
qOut.put("hello")

while True:
	if not qIn.empty():
		print qIn.get()
