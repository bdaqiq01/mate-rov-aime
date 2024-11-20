# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
# from std_msgs.msg import Float32MultiArray

# Library imports
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import numpy as np
import time

# Defining which pwm channels correspond to which thruster
# Ch1 = left vertical thruster
# Ch2 = right vertical thruster
# Ch3 = front left thruster
# Ch4 = front right thruster
# Ch5 = back left thruster
# Ch6 = back right thruster

# bluerobotics_navigator.set_pwm_channel_value(PWMCHANNEL, VALUE)
# VALUE = 4095 * pulse_duration / cycle_period = 4095 * duty cycle

# navigator.set_pwm_channels_duty_cycle(PWMCHANNEL, VALUE)
# sets duty cycle of pwm pin, value is a number between 0 and 1
# takes an array of data to set up the pwm duty cycles

# Initializes the Navigator module with default settings.
navigator.init()
# Setup for PWM Channels 
# Referencing PWM Channels "PwmChannel.Ch1" or "PwmChannel.All"
navigator.set_pwm_freq_hz(1000)
# Enables or disables the PWM chip
navigator.set_pwm_enable(True)

# defines the duty cycle when using direction functions
magnitude = 0.5

pwm_channels = [
    None,
    PwmChannel.Ch1,
    PwmChannel.Ch2,
    PwmChannel.Ch3,
    PwmChannel.Ch4,
    PwmChannel.Ch5,
    PwmChannel.Ch6,
    PwmChannel.Ch7,
    PwmChannel.Ch8,
    PwmChannel.Ch9,
    PwmChannel.Ch10,
    PwmChannel.Ch11,
    PwmChannel.Ch12,
    PwmChannel.Ch13,
    PwmChannel.Ch14,
    PwmChannel.Ch15,
    PwmChannel.Ch16,
]

#  expected a list of 6 values, each corresponds to a thruster and this function assigns each of them with a pwm signal
def set_pwm_channels_values(value):
    for i, value in enumerate(value):
        navigator.set_pwm_channels_duty_cycle([pwm_channels[i+1]], value)

# direction functions assign pwm channels with signal for certain movement
def go_up():
    # array of values for which thruster should turn on in which directon positive or negative
    up = np.array([1, 1, 0, 0, 0, 0])
    # array is multiplied by magnitude to adjust the speed of movement
    up_result = np.array(up * magnitude)
    # outputs pwm signal to correct thrusters for movement
    set_pwm_channels_values(up_result)

def go_down():
    down = np.array([-1, -1, 0, 0, 0, 0])
    down_result = np.array(down * magnitude)
    set_pwm_channels_values(down_result)

def go_left():
    left = np.array([0, 0, -1, 0, -1, 0])
    left_result = np.array(left * magnitude)
    set_pwm_channels_values(left_result)

def go_right():
    right = np.array([0, 0, 0, -1, 0, -1])
    right_result = np.array(right * magnitude)
    set_pwm_channels_values(right_result)

def go_back():
    back = np.array([0, 0, 0, 0, 1, 1])   
    back_result = np.array(back * magnitude)
    set_pwm_channels_values(back_result)

def go_forward():
    forward = np.array([0, 0, 1, 1, 0, 0])
    forward_result = np.array(forward * magnitude)
    set_pwm_channels_values(forward_result)

# turns all thrusters off
def off():
    navigator.set_pwm_channels_duty_cycle([PwmChannel.All], 0)

def main(args=None):
    # while loop with code goes here
    print('Going forward...')
    go_forward()
    time.sleep(5)
    print('Stopping...')
    off()
    # while True:
    #     # checks which button on d pad is pressed. if none are turns thrusters off
    #     if msg.data[5] == -1:
    #         go_left()
    #     elif msg.data[5] == 1:
    #         go_right()
    #     elif msg.data[6] == -1:
    #         go_back()
    #     elif msg.data[6] == 1:
    #         go_forward() 
    #     else:
    #         off()



# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
