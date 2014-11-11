import hubo_ach as ha
import ach
import sys
import time
import math
import string
from ctypes import *
#reading file
f=open('hw7-ik.txt','r')
f2=file.read(f)
lin=f2.split()
x1=float(lin[0])
y1=float(lin[1])
z1=float(lin[2])
x2=float(lin[3])
y2=float(lin[4])
z2=float(lin[5])
x3=float(lin[6])
y3=float(lin[7])
z3=float(lin[8])
x4=float(lin[9])
y4=float(lin[10])
z4=float(lin[11])
x=0
for x in range (6):  
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	#ref.ref[ha.RSP] = -1.57 #set up
	#-------------------------------------------------
	print "first point"
	#setting shoulder 
	sang=math.atan(z1/(abs(x1)+.2145))
	ref.ref[ha.RSR] = sang #angle for shoulder. 
	#going to point. 
	d1=.17914
	d2=.18159
	theta2=math.acos((y1*y1+z1*z1-d1*d1-d2*d2)/(2*d1*d2))
	p=z1*(d1+d2*math.cos(theta2))-y1*(d2*math.sin(theta2))
	p1=y1*(d1+d2*math.cos(theta2))-z1*(d2*math.sin(theta2))
	theta1=math.atan(p/p1)
	print theta1
	print theta2
	ref.ref[ha.RSP] = theta1
	ref.ref[ha.REB] = theta2
	r.put(ref)
	time.sleep(3)
	#-------------------------------------------------
	print "second point"
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	#setting shoulder 
	sang=math.atan(z2/(abs(x2)+.2145))
	ref.ref[ha.RSR] = sang #angle for shoulder. 
	#going to point. 
	d1=.17914
	d2=.18159
	theta2=math.acos((y2*y2+z2*z2-d1*d1-d2*d2)/(2*d1*d2))
	p=z2*(d1+d2*math.cos(theta2))-y2*(d2*math.sin(theta2))
	p1=y2*(d1+d2*math.cos(theta2))-z2*(d2*math.sin(theta2))
	theta1=math.atan(p/p1)
	print theta1
	print theta2
	ref.ref[ha.RSP] = theta1
	ref.ref[ha.REB] = theta2
	r.put(ref)
	time.sleep(3)
#-------------------------------------------------
	print "third point"
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	#setting shoulder 
	sang=math.atan(z3/(abs(x3)+.2145))
	ref.ref[ha.RSR] = -sang #angle for shoulder. 
	#going to point. 
	d1=.17914
	d2=.18159
	theta2=math.acos((y3*y3+z3*z3-d1*d1-d2*d2)/(2*d1*d2))	
	p=z3*(d1+d2*math.cos(theta2))-y3*(d2*math.sin(theta2))
	p1=y3*(d1+d2*math.cos(theta2))-z3*(d2*math.sin(theta2))
	theta1=math.atan(p/p1)
	print theta1
	print theta2	
	ref.ref[ha.RSP] = -theta1
	ref.ref[ha.REB] = -theta2
	r.put(ref)
	time.sleep(3)
	#-------------------------------------------------
	print "fourth point"
	[statuss, framesizes] = s.get(state, wait=False, last=False)
	#setting shoulder 
	sang=math.atan(z4/(abs(x4)+.2145))
	ref.ref[ha.RSR] = sang #angle for shoulder. 
	#going to point. 
	d1=.17914
	d2=.18159
	theta2=math.acos((y4*y4+z4*z4-d1*d1-d2*d2)/(2*d1*d2))
	p=z4*(d1+d2*math.cos(theta2))-y4*(d2*math.sin(theta2))
	p1=y4*(d1+d2*math.cos(theta2))-z4*(d2*math.sin(theta2))
	theta1=math.atan(p/p1)
	print theta1	
	print theta2
	ref.ref[ha.RSP] = -theta1
	ref.ref[ha.REB] = -theta2
	r.put(ref)
	time.sleep(3)
	x=x+1
	r.close()
	s.close()	
