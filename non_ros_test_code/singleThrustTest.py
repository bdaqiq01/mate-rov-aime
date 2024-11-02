# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msgfrom std_msgs.msg import Float32MultiArray

# Library imports
import time
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

# Initializes the Navigator module with default settings.
navigator.init()
# Setup for PWM Channel 1
navigator.set_pwm_freq_hz(1000)
# Enables the PWM chip
navigator.set_pwm_enable(True)

# defines the duty cycle when using direction functions
magnitude = 0.5

# Sets PWM duty cycle for Channel 1 only
def set_pwm_channel_1(value):
    navigator.set_pwm_channels_duty_cycle([PwmChannel.Ch1], value)

# Movement functions that only affect the thruster on channel 1
def go_up():
    set_pwm_channel_1(0.7)

def go_down():
    set_pwm_channel_1(0.2)

# Turns the thruster off
def off():
    set_pwm_channel_1(0.5)

def main(args=None):
    # Example control logic for a single thruster
    while True:
        print("forward")
        go_up()
        time.sleep(2)
        print("back")
        go_down()
        print("Done")
        time.sleep(5)
        off()

# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
