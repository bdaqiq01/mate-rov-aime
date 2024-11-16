# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Float32MultiArray

# Library imports
import time
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
from inti_rov_thruster_esc_test import init_rov_thrusters

# Initializes the Navigator module with default settings.
navigator.init()

# init_rov_thrusters(pwm_freq=200, channels=[PwmChannel.Ch1, PwmChannel.Ch2, PwmChannel.Ch3, PwmChannel.Ch4], run_full_init_cycle=True)
# Setup for PWM Channels
navigator.set_pwm_freq_hz(1000)
# Enables the PWM chip
navigator.set_pwm_enable(True)

# Defines the duty cycle when using direction functions
magnitude = 0.5

# Sets PWM duty cycle for all four channels
def set_pwm_channels(values):
    # Ensure that values correspond to PWM channels 1, 2, 3, and 4
    navigator.set_pwm_channels_duty_cycle([PwmChannel.Ch1, PwmChannel.Ch2, PwmChannel.Ch3, PwmChannel.Ch4], values)

# Movement functions that affect all four thrusters
def go_up():
    set_pwm_channels([0.7, 0.7, 0.7, 0.7])  # All thrusters go forward

def go_down():
    set_pwm_channels([0.2, 0.2, 0.2, 0.2])  # All thrusters go backward

def go_left():
    set_pwm_channels([0.7, 0.2, 0.7, 0.2])  # Thrusters 1 and 3 forward, 2 and 4 backward (simulate left turn)

def go_right():
    set_pwm_channels([0.2, 0.7, 0.2, 0.7])  # Thrusters 1 and 3 backward, 2 and 4 forward (simulate right turn)

def rotate_left():
    set_pwm_channels([0.7, 0.2, 0.2, 0.7])  # Thrusters 1 and 4 forward, 2 and 3 backward (simulate left rotation)

def rotate_right():
    set_pwm_channels([0.2, 0.7, 0.7, 0.2])  # Thrusters 1 and 4 backward, 2 and 3 forward (simulate right rotation)

# Turns off all thrusters
def off():
    set_pwm_channels([0.5, 0.5, 0.5, 0.5])

def main(args=None):
    # Example control logic for four thrusters
    while True:
        print("Going up")
        go_up()
        time.sleep(2)
        
        print("Going down")
        go_down()
        time.sleep(2)
        
        print("Turning left")
        go_left()
        time.sleep(2)
        
        print("Turning right")
        go_right()
        time.sleep(2)

        print("Rotating left")
        rotate_left()
        time.sleep(2)
        
        print("Rotating right")
        rotate_right()
        time.sleep(2)

        print("Stopping")
        off()
        time.sleep(5)

# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
