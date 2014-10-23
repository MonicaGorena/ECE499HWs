import diff_drive
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np

dd = diff_drive
ref = dd.H_REF()
tim = dd.H_TIME()

ROBOT_DIFF_DRIVE_CHAN   = 'robot-diff-drive'
ROBOT_CHAN_VIEW   = 'robot-vid-chan'
ROBOT_TIME_CHAN  = 'robot-time'
# CV setup 
cv.NamedWindow("wctrl", cv.CV_WINDOW_AUTOSIZE)
newx = 320
newy = 240

nx = 640
ny = 480

x=0

r = ach.Channel(ROBOT_DIFF_DRIVE_CHAN)
r.flush()
v = ach.Channel(ROBOT_CHAN_VIEW)
v.flush()
t = ach.Channel(ROBOT_TIME_CHAN)#time chanel, geting time from simulator
t.flush()

while True:
    # Get Frame
    img = np.zeros((newx,newy,3), np.uint8)
    c_image = img.copy()
    vid = cv2.resize(c_image,(newx,newy))
    [status, framesize] = v.get(vid, wait=False, last=True)
    if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
        vid2 = cv2.resize(vid,(nx,ny))
        img = cv2.cvtColor(vid2,cv2.COLOR_BGR2RGB)
        #cv2.imshow("wctrl", img)
	cv2.waitKey(10)
    else:
        raise ach.AchException( v.result_string(status) )
    [status, framesize] = t.get(tim, wait=False, last=True)
    if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
        pass
    else:
        raise ach.AchException( v.result_string(status) )
    st=tim.sim[0]
    newst=0
    #print 'Sim Time = ', st
    ib,ig,ir = cv2.split(img) 
    ret,threshr = cv2.threshold(ir,1,1,cv2.THRESH_BINARY_INV)
    n=1
    val=0
    mm=cv2.moments(threshr)
    if mm["m00"] != 0:
        x=mm["m10"]/mm["m00"]
        y=mm["m01"]/mm["m00"]
        cv2.circle(img, (int(x),int(y)), 5, (0,0,200), -1,8,0) 
        cv2.putText(img, str(x)+","+str(y),(int(x),int(y)),cv2.FONT_HERSHEY_PLAIN,1,[0,0,102])#,1,8,1)
        error=320-x
        #print error
            
        if error<0: #move right, clockwise 
            ref.ref[0] = -.1*(abs(error)/9)
            ref.ref[1] = .1*(abs(error)/9)
        elif error>0: #move counterclockwise
            ref.ref[0] = .1* (abs(error)/9)
            ref.ref[1] = -.1*(abs(error)/9)
        else: 
            ref.ref[0] = 0
            ref.ref[1] = 0
    cv2.imshow("wctrl", img)
    r.put(ref);
    ## Sleeps
    while newst<0.04:
	[status, framesize] = t.get(tim, wait=False, last=True)
        newst=tim.sim[0]-st
    
