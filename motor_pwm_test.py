from pyA20.gpio import gpio, port
from time import sleep
from orangepwm import OrangePwm

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

lp.start(100)
gpio.output(lf, 1)
gpio.output(lb, 0)	# gpio.LOW : 0
gpio.output(re, 1)	# gpio.HIGH : 1
gpio.output(rf, 1)

lp.start(70)
rp.start(100)

sleep(1)

lp.changeDutyCycle(100)
rp.changeDutyCycle(70)

sleep(1)

lp.stop()
rp.stop()
