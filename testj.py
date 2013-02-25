class A(object):
	def __init__(self, arg):
		self.arg = arg
	def call(self, arg):
		print "I look like a function but really I'm %s"%repr(self)


from random import random
my_a = A("Set in the module" + str(random()))