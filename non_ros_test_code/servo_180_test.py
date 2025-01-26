# Ethan Noritake
# Last edited 1/26/25

import time
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

# Initializes the Navigator module with default settings.
navigator.init()

# Setup for PWM Channels
# Sets speed of rotation. Can be 20-200 Hz. Higher frequency faster motion but less precision.
navigator.set_pwm_freq_hz(50)
# Enables the PWM chip
navigator.set_pwm_enable(True)
# Sets the initial servo position to 0 degrees
navigator.set_pwm_channel_duty_cycle(PwmChannel.Ch1, 5)

# Sets rotation at 0 degrees
def rotate_0():
    navigator.set_pwm_channels_duty_cycle(5)

# Sets rotation at 90 degrees
def rotate_90():
    navigator.set_pwm_channels_duty_cycle(7.5)

# Sets rotation at 180 degrees
def rotate_180():
    navigator.set_pwm_channels_duty_cycle(10)

# Sets rotation at custom degree angle
def rotate_degrees(degree):
    duty = (degree/36) + 5
    navigator.set_pwm_channels_duty_cycle(duty)

def main(args=None):
    while True:
        print("Rotating to 90 degrees")
        def rotate_90():
        time.sleep(2)

        print("Rotating to 180 degrees")
        def rotate_180():
        time.sleep(2)

        print("Rotating to 0 degrees")
        def rotate_0():
        time.sleep(2)

if __name__ == '__main__':
    main()