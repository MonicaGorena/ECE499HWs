import diff_drive
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import controller_include as ci
from ctypes import *

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
c = ach.Channel(ci.CONTROLLER_REF_NAME)#
controller = ci.CONTROLLER_REF()#
c.put(controller)#
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
	
    ib,ig,ir = cv2.split(img)
    ret,threshb = cv2.threshold(ib,1,1,cv2.THRESH_BINARY_INV)   
    ret,threshr = cv2.threshold(ir,1,1,cv2.THRESH_BINARY_INV)
    img3= threshb & threshr 
    n=1
    val=0
    for x in range (0,640):
        px = img3[205,x]
        val=val+x*px
        n=n+1*px
    if val/n >0:
        cv2.circle(img, (val/n,205), 5, (0,0,200), -1,8,0) 
        cv2.putText(img, str(val/n)+",205",(val/n,205),cv2.FONT_HERSHEY_PLAIN,1,[0,0,102])#,1,8,1)

    px = img3[205,320]
    #print "px is", px
    [statuss, framesizes] = c.get(controller, wait=False, last=False)
    ref.ref[0] = controller.mot1
    ref.ref[1] = controller.mot2
    cv2.imshow("wctrl", img)
    r.put(ref);
    # Sleeps
    time.sleep(0.1)

