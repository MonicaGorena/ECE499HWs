#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*
# Copyright (c) 2013, Daniel M. Lofaro
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# */
#Hello World Code: 
##to open hubo:  hubo-ach sim openhubo physics
##to oppen robot: ./robot-view server
## hubo-ach console ->goto RAR 0.4
## hubo-ach read
## hubo-ach kill


import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

#RESET
#s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
#r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#state = ha.HUBO_STATE()
#ref = ha.HUBO_REF()
#[statuss, framesizes] = s.get(state, #wait=False,last=False)
#ref.ref[ha.LSR]= 0
#ref.ref[ha.LSY]= 0
#ref.ref[ha.LEB]= 0
#r.put(ref)
#time.sleep(10)
#r.close()
#s.close()



x=1
# while loop
while x != 0:# wile loop x value will change from 1 to 2 endlessly 
	if x==1:
		# Open Hubo-Ach feed-forward and feed-back (reference and state) channels		
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		# feed-forward will now be refered to as "state"
		state = ha.HUBO_STATE()
		# feed-back will now be refered to as "ref"
		ref = ha.HUBO_REF()
		# Get the current feed-forward (state) 
		[statuss, framesizes] = s.get(state, wait=False,last=False)
		ref.ref[ha.LSR]= 1.2
		ref.ref[ha.LSY]= 1.4
		ref.ref[ha.LEB]= -3
		# Write to the feed-forward channel
		r.put(ref)
		# Close the connection to the channels
		r.close()
		s.close()
		time.sleep(.5)
		x=2
		#print "x=",x
		#print "Joint = ", state.joint[ha.LEB].pos
	else:
		# Open Hubo-Ach feed-forward and feed-back (reference and state) channels		
		s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
		r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
		# feed-forward will now be refered to as "state"
		state = ha.HUBO_STATE()
		# feed-back will now be refered to as "ref"
		ref = ha.HUBO_REF()
		# Get the current feed-forward (state) 
		[statuss, framesizes] = s.get(state, wait=False,last=False)
		ref.ref[ha.LSR]= 1.2
		ref.ref[ha.LSY]= 1.4
		ref.ref[ha.LEB]= -.2
		# Close the connection to the channels
		r.put(ref)
		# Close the connection to the channels		
		r.close()
		s.close()
		time.sleep(.5)
		x=1
		#print "x=",x
		#print "Joint = ", state.joint[ha.LEB].pos
