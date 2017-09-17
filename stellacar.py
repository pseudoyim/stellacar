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

  elif wheel_dir == lr:
	print 'left-reverse'
	GPIO.output(11, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(11, GPIO.LOW)

  elif wheel_dir == rf:
	print 'right-forward'
	GPIO.output(15, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(15, GPIO.LOW)

  elif wheel_dir == rr:
	print 'right-reverse'
	GPIO.output(12, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(12, GPIO.LOW)
