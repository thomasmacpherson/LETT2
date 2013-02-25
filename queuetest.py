import Queue
import queueTest2
import threading
# maxsize of 0 means that we can put an unlimited number of events
# on the queue
q = Queue.Queue(maxsize=0)
number =1
q.put(number)
t= threading.Thread(target= queueTest2.startThis(q))
t.start


q.put(2)


q.put(2)


q.put("this")
