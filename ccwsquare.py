def checksum (p):
	len(p)	
	check=0
	for i in range(len(p)-3):
		check=check+p[i+2] 
	newcheck=~check 
	#print "checksum is=", newcheck & 0xff
	p[len(p)-1]= newcheck & 0xff
	#print "packet", p  
	#return newcheck & 0xff 
	return p

#creates a valid command packet for velocity. 
def velocity (ID, vel):		
	if vel<0:
		vel = vel & 0xFFFF
		vel=(~vel)+1
		velL = vel & 0x00FF
		velH = vel & 0xFF00
		velH = velH >> 8
	else: 
		velL = vel & 0x00FF
		velH = vel & 0xFF00
		velH = velH | 0x0400
		velH = velH >> 8
	
	velpack=[0xff, 0xff, ID, 0x04, 0x20, velL, velH, 0]
	velpack=checksum(velpack)
	#print "velocity packet is", velpack
	return velpack
