import i2cHandler

import Queue

q = Queue.Queue()


i2c= i2cHandler.handler(q)

i2c.drawSquare(0x10,4,4,4,4)