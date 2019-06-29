import cv2
from pyA20.gpio import gpio, port
from time import sleep
from orangepwm import OrangePwm

SPEED_L = 70
SPEED_R = 68
SPEED_OUT = 100
SPEED_IN = 50

gpio.init()

le = port.PA21		# ENA
lb = port.PA18		# IN1
lf = port.PG8		  # IN2
rb = port.PG9		  # IN3
rf = port.PG6		  # IN4
re = port.PG7		  # ENB

lp = OrangePwm(100, le)
rp = OrangePwm(100, re)
gpio.setcfg(lf, 1)
gpio.setcfg(lb, 1)
gpio.setcfg(rf, 1)
gpio.setcfg(rb, 1)

lp.start(0)
gpio.output(lf, 1)
gpio.output(lb, 0)	# gpio.LOW : 0
gpio.output(re, 1)	# gpio.HIGH : 1
gpio.output(rf, 1)
rp.start(0)

c = cv2.VideoCapture(0)
c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
	_,full_image = c.read()
	        
	cv2.imshow('frame',full_image)
	    
	k = cv2.waitKey(5)
	if k == ord('q'):
		break
	if k > 0:
		print(k)
	if k == 82:		# UP
		lp.changeDutyCycle(SPEED_L)
		rp.changeDutyCycle(SPEED_R)
	elif k == 81:	# LEFT
		lp.changeDutyCycle(SPEED_IN)
		rp.changeDutyCycle(SPEED_OUT)
	elif k == 83:	# RIGHT
		lp.changeDutyCycle(SPEED_OUT)
		rp.changeDutyCycle(SPEED_IN)
	elif k == 84:	# DOWN
		lp.changeDutyCycle(0)
		rp.changeDutyCycle(0)
		
lp.stop()
rp.stop()
