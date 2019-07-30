from pyA20.gpio import gpio, port
from time import sleep
from orangepwm import OrangePwm

gpio.init()

re = port.PA21		# ENA
rb = port.PA18		# IN1
rf = port.PG8		# IN2
lf = port.PG9		# IN3
lb = port.PG6		# IN4
le = port.PG7		# ENB

lp = OrangePwm(100, le)
rp = OrangePwm(100, re)
gpio.setcfg(lf, 1)
gpio.setcfg(lb, 1)
gpio.setcfg(rf, 1)
gpio.setcfg(rb, 1)

gpio.output(lf, 1)	# gpio.HIGH : 1
gpio.output(lb, 0)	# gpio.LOW : 0
gpio.output(rb, 0)
gpio.output(rf, 1)

print('40% Power')
lp.start(40)
rp.start(40)
sleep(1)

print('70% Power')
lp.changeDutyCycle(70)
rp.changeDutyCycle(70)
sleep(1)

print('100% Power')
lp.changeDutyCycle(100)
rp.changeDutyCycle(100)
sleep(1)

lp.stop()
rp.stop()
