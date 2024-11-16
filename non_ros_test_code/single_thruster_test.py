# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Float32MultiArray

# Library imports
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

# Initializes the Navigator module with default settings.
bluerobotics_navigator.init()
# Setup for PWM Channel 1
navigator.set_pwm_freq_hz(1000)
# Enables the PWM chip
navigator.set_pwm_enable(True)

# defines the duty cycle when using direction functions
magnitude = 0.5

# Sets PWM duty cycle for Channel 1 only
# def set_pwm_channel_1(value):
#     navigator.set_pwm_channels_duty_cycle(PwmChannel.Ch1, value)

# Movement functions that only affect the thruster on channel 1
def go_up():
    set_pwm_channel_1(magnitude)

def go_down():
    set_pwm_channel_1(-magnitude)

# Turns the thruster off
def off():
    set_pwm_channel_1(0)


def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

calc_pwm_value = lambda duration_on_ms: int(4095 * (duration_on_ms / TOTAL_PERIOD_DURATION_MS))
def set_pwm_channel(val, channels):
    calc_ms = map_range(val, -1.0, 1.0, )
    navigator.set_pwm_channels_value(channels, calc_pwm_value(PWM_LOW_DURATION_MS))

def main(args=None):
    # Example control logic for a single thruster
    while True:
        # Use msg data to decide the direction, assuming msg is being updated externally
        if msg.data[5] == 1:  # Example condition, adjust based on input method
            go_up()
        elif msg.data[5] == -1:
            go_down()
        else:
            off()

# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
