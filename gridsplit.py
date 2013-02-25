


def restrictedTo(list, number):
	first = list.pop()
	
	for x in list:
		if not(first <= number and x <= number) or (first > number and x > number):
			return 1
			
	if first <= number:
		return 0
		
	else:
		return 2
		
		
		


if restrictedTo(xlist, number)!= 1 :
	if restrictedTo(yList, number)!=1: #check if contained within one grid
		# send cmd as contained in one grid
	
else :
	if restrictedTo(yList, number)!=1:
			

def lineSplit(x,y,ex,ey, axis):
	#axis 
	
	
	
	gradient = (ey - y)/(ex - x)
	
	constant = y - gradient*x
	
	newY1 = gradient*7 + constant
	newY2 = gradient*8 + constant
	
	newX1 = (7 - constant) / gradient
	newX2 = (8 - constant) / gradient



def squareSplit(x1,y1,x2,y2,x3,y3,x4,y4,axis):
	lineSplit(x1,y1,x2,y2)
	lineSplit(x2,y2,x3,y3)
	lineSplit(x3,y3,x4,y4)	
	lineSplit(x4,y4,x1,y1)