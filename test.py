import RPi.GPIO as GPIO
import time

# Activating GPIO pins and number arrangement.
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


# LEFT-FORWARD: pin 13 (yellow wire)
lf = 13

# LEFT-REVERSE: pin 11 (red wire)
lr = 11

# RIGHT-FORWARD: pin 15 (green wire)
rf = 15

# RIGHT-REVERSE: pin 12 (orange wire)
rr = 12


# Activating GPIO pins.
GPIO.setup(lf, GPIO.OUT)
GPIO.setup(lr, GPIO.OUT)
GPIO.setup(rf, GPIO.OUT)
GPIO.setup(rr, GPIO.OUT)



# Function for Stella to use.
def wheel(wheel_dir, duration):

  if wheel_dir == lf:
	print 'left-forward'
	GPIO.output(13, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(13, GPIO.LOW)

'''
# Tests.
GPIO.output(lf, GPIO.HIGH)
print 'left-forward'
time.sleep(1.0)
GPIO.output(lf, GPIO.LOW)

GPIO.output(lr, GPIO.HIGH)
print 'left-reverse'
time.sleep(1.0)
GPIO.output(lr, GPIO.LOW)

GPIO.output(rf, GPIO.HIGH)
print 'right-forward'
time.sleep(1.0)
GPIO.output(rf, GPIO.LOW)

GPIO.output(rr, GPIO.HIGH)
print 'right-reverse'
time.sleep(1.0)
GPIO.output(rr, GPIO.LOW)

'''

if __name__ == "__main__":
  wheel(lf, 2.0)
