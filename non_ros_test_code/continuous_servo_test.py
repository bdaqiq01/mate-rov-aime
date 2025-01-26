
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
navigator.set_pwm_channel_duty_cycle(PwmChannel.Ch1, 7.5)

# Sets rotation full speed clockwise
def rotate_cw():
    navigator.set_pwm_channels_duty_cycle(5)

# Stops rotation can be set to 82-98 degrees
def stop():
    navigator.set_pwm_channels_duty_cycle(7.5)

# Sets rotation at full speed counter clockwise
def rotate_ccw():
    navigator.set_pwm_channels_duty_cycle(10)

# Sets rotation speed 0-81 cw, 82-98 degrees stop, 99-180 ccw
def rotate_velocity(degree):
    duty = (degree/36) + 5
    navigator.set_pwm_channels_duty_cycle(duty)

def main(args=None):
    while True:
        print("Rotating full speed clockwise")
        rotate_cw():
        time.sleep(2)

        print("Stopping")
        def stop():
        time.sleep(2)

        print("Rotating full speed counter clockwise")
        def rotate_ccw():
        time.sleep(2)

if __name__ == '__main__':
    main()