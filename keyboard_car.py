import cv2
from pyA20.gpio import gpio, port
from orangepwm import OrangePwm

SPEED_L = 40
SPEED_R = 40
SPEED_OUT = 60
SPEED_IN = 20

gpio.init()

re = port.PA21		# ENA
rb = port.PA18		# IN1
rf = port.PG8		  # IN2
lf = port.PG9		  # IN3
lb = port.PG6		  # IN4
le = port.PG7		  # ENB

lp = OrangePwm(100, le)
rp = OrangePwm(100, re)
gpio.setcfg(lf, 1)
gpio.setcfg(lb, 1)
gpio.setcfg(rf, 1)
gpio.setcfg(rb, 1)

lp.start(0)
gpio.output(lf, 1)	# gpio.HIGH : 1
gpio.output(lb, 0)	# gpio.LOW : 0
gpio.output(rb, 0)
gpio.output(rf, 1)
rp.start(0)

while True:
	img = cv2.imread('car.jpg', cv2.IMREAD_COLOR)
	        
	cv2.imshow('car',img)
	    
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
