import RPi.GPIO as GPIO  # Assuming Raspberry Pi with RPi.GPIO library
import time

# Define pins
trigPin1 = 8
echoPin1 = 9
trigPin2 = 5
echoPin2 = 6
led1 = 2
led2 = 3

# Set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin1, GPIO.OUT)
GPIO.setup(echoPin1, GPIO.IN)
GPIO.setup(trigPin2, GPIO.OUT)
GPIO.setup(echoPin2, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

def measure_distance(trigPin, echoPin):
    # Trigger sensor
    GPIO.output(trigPin, False)
    time.sleep(2e-6)  # Delay 2 microseconds
    GPIO.output(trigPin, True)
    time.sleep(10e-6)  # Delay 10 microseconds
    GPIO.output(trigPin, False)

    # Measure echo pulse duration
    duration = GPIO.input(echoPin)
    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()
    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()

    # Calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound in cm/s
    return distance

while True:
    # Measure distances for both sensors
    distance1 = measure_distance(trigPin1, echoPin1)
    distance2 = measure_distance(trigPin2, echoPin2)

    # Control LEDs based on distances
    GPIO.output(led1, distance1 < 50)
    GPIO.output(led2, distance2 < 50)

    time.sleep(0.1)  # Optional delay for stability
