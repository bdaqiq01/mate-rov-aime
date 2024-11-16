# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msgfrom std_msgs.msg import Float32MultiArray

# Library imports
import time
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
from inti_rov_thruster_esc_test import *

# Initializes the Navigator module with default settings.
navigator.init()

ACTIVE_PWM_CHANNELS = [
    PwmChannel.Ch1,
    PwmChannel.Ch2,
    PwmChannel.Ch3,
]

init_rov_thrusters(
    pwm_freq = 200,
    channels = ACTIVE_PWM_CHANNELS,
    run_full_init_cycle=True
)


# Movement functions that only affect the thruster on channel 1
def go_up():
    set_pwm_channels(0.5, ACTIVE_PWM_CHANNELS)
    # navigator.set_pwm_channels_value([PwmChannel.Ch1], calc_pwm_value(1.9))


def go_down():
    set_pwm_channels(-0.5, ACTIVE_PWM_CHANNELS)
    # navigator.set_pwm_channels_value([PwmChannel.Ch1], calc_pwm_value(1.1))

# Turns the thruster off
def off():
    set_pwm_channels(0.0, ACTIVE_PWM_CHANNELS)
    # navigator.set_pwm_channels_value([PwmChannel.Ch1], calc_pwm_value(1.5))

def main(args=None):
    # Example control logic for a single thruster
    try:
        while True:
            print("forward")
            go_up()
            time.sleep(2)
            
            print("back")
            go_down()
            
            print("Done")
            time.sleep(5)
            off()
    except KeyboardInterrupt as ex:
        print('Exiting per user request...')
    finally:
        off()


# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
