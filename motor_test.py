from pyA20.gpio import gpio, port
from time import sleep

gpio.init()

re = port.PA21		  # ENA
rb = port.PA18		  # IN1
rf = port.PG8		    # IN2
lf = port.PG9		    # IN3
lb = port.PG6		    # IN4
le = port.PG7		    # ENB

gpio.setcfg(le, 1)	# gpio.OUTPUT : 1
gpio.setcfg(lf, 1)
gpio.setcfg(lb, 1)
gpio.setcfg(rf, 1)
gpio.setcfg(rb, 1)
gpio.setcfg(re, 1)

gpio.output(le, 1)	# gpio.HIGH : 1
gpio.output(lf, 1)
gpio.output(lb, 0)	# gpio.LOW : 0
gpio.output(re, 1)	# gpio.HIGH : 1
gpio.output(rf, 1)
gpio.output(rb, 0)	# gpio.LOW : 0

sleep(1)

gpio.output(le, 0)
gpio.output(re, 0)
