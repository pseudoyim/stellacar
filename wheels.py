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


# Function to drive wheels.
def wheel(wheel_dir, duration):

    # Duration is initially received as a str.
    duration = float(duration)
    
    if wheel_dir == ('lf','rf'):
        print 'Forward for {} seconds'.format(duration)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

    elif wheel_dir == ('lr','rr'):
        print 'Backward for {} seconds'.format(duration)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)

    elif wheel_dir == ('lf', 'rr'):
        print 'Rightward pivot for {} seconds'.format(duration)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)

    elif wheel_dir == ('lr', 'rf'):
        print 'Leftward pivot for {} seconds'.format(duration)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
