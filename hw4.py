#Using the "key frame" methods discussed in class make the Hubo2+ or DRC Hubo walk forward 2 foot lengths.
#- Submit YouTube link of system working
#- Submit link to program on github
#- Submit 1-2 paragraphs on your methodology, assumptions, etc. that you used for this assignment.
#- You may use Python or C/C++
import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# starting up straighthub
time.sleep(5)
s=0
x=0.01
print "shifting weights to the right foot." 
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()
[statuss, framesizes] = s.get(state, wait=False,last=False)	
while x < .16: 
	ref.ref[ha.RHR]= x
	ref.ref[ha.LHR]= x
	ref.ref[ha.RAR]=-x
	ref.ref[ha.LAR]=-x
	x=x+.01
	time.sleep(.5)
	r.put(ref)
print "x=",x
print "lifting left foot"
y=0
while y<.19:
	ref.ref[ha.LHP]=-y
	y=y+0.01
	time.sleep(.5)
	r.put(ref)
print "y=",y
p=0
while p<5:
# 
	print "bending right foot down"
	a=0
	while a<y*2:	
		ref.ref[ha.LAP]= a/2	
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		a=a+0.1
		time.sleep(.5)
		r.put(ref)
	print "a=",a
	print "Shifting weight to left foot"
	while x > -.16:	
		ref.ref[ha.RHR] = x
		ref.ref[ha.LHR] = x
		ref.ref[ha.RAR]=-x
		ref.ref[ha.LAR]=-x
		x=x-.01
		time.sleep(.5)
		r.put(ref)
	print"xnow=",x
	print "straighten left foot" 
	c=a/2
	while c>0.01:
		ref.ref[ha.LHP]=-c
		ref.ref[ha.LAP]=c
		c=c-.01
		time.sleep(.5)
		r.put(ref)
	print "c=",c
	print "liftting right foot" 
	d=0
	while d<.19: #*2?
		ref.ref[ha.RHP]=-d
		d=d+0.01
		time.sleep(.5)
		r.put(ref)
	print "d=",d
	print "straightening Right foot" 
	f=-a/2
	while f<0:
		ref.ref[ha.RKN]=-f
		#ref.ref[ha.RAP]=-f
		f=f+0.01
		time.sleep(.5)
		r.put(ref)
	print "bending left foot down"
	g=0
	while g<.19*2:	
		ref.ref[ha.LAP]= -g/2	
		ref.ref[ha.RAP]= g/2
		ref.ref[ha.LHP]= -g/2
		ref.ref[ha.LKN]=g
		g=g+0.1
		time.sleep(.5)
		r.put(ref)
	
	print "Shifting weight to right foot"
	while x <.16:	
		ref.ref[ha.RHR] = x
		ref.ref[ha.LHR] = x
		ref.ref[ha.RAR]=-x
		ref.ref[ha.LAR]=-x
		x=x+.01
		time.sleep(.5)
		r.put(ref)
	print"xnow=",x
	print "straighten right foot" 
	c=a/2
	while c>0.01:
		ref.ref[ha.RHP]=-c
		ref.ref[ha.RAP]=c
		c=c-.01
		time.sleep(.5)
		r.put(ref)
	print "c=",c
	print "lifting left foot"
	y=0
	while y<.19:
		ref.ref[ha.LHP]=-y
		y=y+0.01
		time.sleep(.5)
		r.put(ref)
	print "y=",y
	print "straightening left foot" 
	f=-.4/2
	while f<0:
		ref.ref[ha.LKN]=-f
		#ref.ref[ha.RAP]=-f
		f=f+0.01
		time.sleep(.5)
		r.put(ref)

p=p+1

r.close()
s.close()
print "done" 
