import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
from wave import *
import math
w=1
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()
[statuss, framesizes] = s.get(state, wait=False,last=False)
print "starting up straight"
ref.ref[ha.RAP]=0
ref.ref[ha.RHP]=0
ref.ref[ha.RKN]=0
ref.ref[ha.LAP]=0
ref.ref[ha.LHP]=0
ref.ref[ha.LKN]=0
ref.ref[ha.LEB]=0
x=0
z=0
a=0
print "start waving" 
ref.ref[ha.LSR]= 1.2
ref.ref[ha.LSY]= 1.4
while a<1.5:
		ref.ref[ha.LEB]=(1.3* math.cos(a*4))-1.3
		r.put(ref)
		a=a+0.1
		time.sleep(.5)
a=0

print "setting hips"
while x < .1: #While loop for moving the hips slowly
	ref.ref[ha.RHR] = x
	ref.ref[ha.LHR] = x
	ref.ref[ha.RAR]=-x
	ref.ref[ha.LAR]=-x
	x=x+.02
	r.put(ref)
	time.sleep(.5)
while z<3:#while loop for flexing leg
	while a<1.5:#going dow
		ref.ref[ha.LEB]=(1.3* math.cos(a*4))-1.3
		x=x+.2
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		ref.ref[ha.LAP]= -a/2
		ref.ref[ha.LHP]= -a/2
		ref.ref[ha.LKN]=a
		print "a=",a
		time.sleep(2)
		r.put(ref)
		a=a+0.1
	while a>0:#going up
		ref.ref[ha.LEB]=(1.3* math.cos(a*4))-1.3
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		ref.ref[ha.LAP]= -a/2
		ref.ref[ha.LHP]= -a/2
		ref.ref[ha.LKN]=a
	 	a=a-0.1
		time.sleep(2)
		r.put(ref)
	z=z+1
print "waiting 5s. while continuing to wave"
tim=state.time
ntim=0
stim=0
p=0
while ntim<5:
	while p<1.5:
		ref.ref[ha.LEB]=(1.3* math.cos(p*4))-1.3
		r.put(ref)
		p=p+0.1
		time.sleep(.5)
	[statuss, framesizes] = s.get(state, wait=False,last=False)
	stim=state.time	
	ntim=stim-tim
print "stop waving and stand up straight"
#stop waving 
ref.ref[ha.LEB]=0
ref.ref[ha.LSR]= 0
ref.ref[ha.LSY]= 0
#moving hips back to place
x=.1
while x > 0: 
	ref.ref[ha.RHR] = x
	ref.ref[ha.LHR] = x
	ref.ref[ha.RAR]=-x
	ref.ref[ha.LAR]=-x
	x=x-.02
	r.put(ref)
	time.sleep(.5)
r.close()
s.close()
