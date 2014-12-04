import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

#sim time - state.time
time.sleep(5)
s=0
x=0.01

while x < .16: #While loop for moving the hips slowly
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = x
	ref.ref[ha.LHR] = x
	ref.ref[ha.RAR]=-x
	x=x+.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
time.sleep(5)

y=0
while y<1.3:#while loop for making hubo raise one leg slowly
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = .15
	ref.ref[ha.LHR] = .15
	ref.ref[ha.RAR]=-.15	
	ref.ref[ha.LHP]=-y
	ref.ref[ha.LKN]=y
	#print "JointLHP = ", state.joint[ha.LHP].pos
	y=y+0.01
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
z=0
a=0

while z<7:#while loop for flexing leg
	while a<1.5:#going down
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		state = ha.HUBO_STATE()
		ref = ha.HUBO_REF()
		[statuss, framesizes] = s.get(state, wait=False,last=False)	
		ref.ref[ha.RHR] = .15
		ref.ref[ha.LHR] = .15
		ref.ref[ha.RAR]=-.15
		ref.ref[ha.LHP]=-1.3
		ref.ref[ha.LKN]=1.3	
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		#print "JointRKN = ", state.joint[ha.LHP].pos
	 	a=a+0.1
		print "a=",a
		time.sleep(.5)
		r.put(ref)
		r.close()
		s.close()
	while a>0:#going up
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		state = ha.HUBO_STATE()
		ref = ha.HUBO_REF()
		[statuss, framesizes] = s.get(state, wait=False,last=False)	
		ref.ref[ha.RHR] = .15
		ref.ref[ha.LHR] = .15
		ref.ref[ha.RAR]=-.15
		ref.ref[ha.LHP]=-1.3
		ref.ref[ha.LKN]=1.3	
		ref.ref[ha.RAP]= -a/2
		ref.ref[ha.RHP]= -a/2
		ref.ref[ha.RKN]=a
		#print "JointRKN = ", state.joint[ha.LHP].pos
	 	a=a-0.1
		time.sleep(.5)
		r.put(ref)
		r.close()
		s.close()
	z=z+1

print "done"

