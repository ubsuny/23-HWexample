#This is a python code for finding slope of two points on a line.
def getslope (x0,y0,x1,y1):	# two points on a line
num= y1-y0 #numerator 
den= x1-x0# denominator
if abs (den)>0.0001:
	slope=num/den 		#defining slope
else:
Print 'Invalid input'
slope=num
return slope
#unit tests
print 'unit test 1'
x0 =0.0
y0 = 0.0
x1 = 0.0
y1 = 1.0
slope = getslope (x0,y0,x1,y1)
print slope
