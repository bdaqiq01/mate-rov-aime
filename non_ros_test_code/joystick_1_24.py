# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msgfrom std_msgs.msg import Float32MultiArray

# Library imports
import time
#import bluerobotics_navigator as navigator
#from bluerobotics_navigator import PwmChannel
#from inti_rov_thruster_esc_test import *
import pygame
import sys
from pygame.locals import *

#navigator.init() # Initializes the Navigator module with default settings.
pygame.init() 
pygame.joystick.init() #Initializes joystick module
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())] #Initializes an array of joysticks detected
for joystick in joysticks:
    print(joystick.get_name())

ACTIVE_PWM_CHANNELS = [
    #PwmChannel.Ch1,
    #PwmChannel.Ch2,
    #PwmChannel.Ch3,
    # PwmChannel.Ch4,
]

#init_rov_thrusters(
    #pwm_freq = 200,
    #channels = ACTIVE_PWM_CHANNELS,
    #run_full_init_cycle=True
#)


# Movement functions that only affect the thruster on channel 1
def go_up():
    #set_pwm_channels(0.5, ACTIVE_PWM_CHANNELS)
    # navigator.set_pwm_channels_value([PwmChannel.Ch1], calc_pwm_value(1.9))
    print('Going up..')


def go_down():
    #set_pwm_channels(-0.5, ACTIVE_PWM_CHANNELS)
    # navigator.set_pwm_channels_value([PwmChannel.Ch1], calc_pwm_value(1.1))
    print('Going down..')

# Turns the thruster off
def off():
    #set_pwm_channels(0.0, ACTIVE_PWM_CHANNELS)
    # navigator.set_pwm_channels_value([PwmChannel.Ch1], calc_pwm_value(1.5))
    print('Thrusters off..')
    
def main(args=None):
    # Example control logic for a single thruster
    try:
        while True:

            for event in pygame.event.get():
                #Processes event types for controller input and printing out their data
                if event.type == JOYBUTTONDOWN:
                    print(event.button)
                    if event.button == 9:
                        print('Quitting per user request')
                        pygame.quit()
                        sys.exit()
                    if event.button == 1:
                        go_up()
                        time.sleep(0)
                    if event.button == 2:
                        go_down()
                        time.sleep(0)
                    if event.button == 3:
                        print("Turning left")
                        #go_left()
                        time.sleep(0)
                    if event.button == 4:
                        print("Turning right")
                        #go_right()
                        time.sleep(0)
                    if event.button == 6:
                        print("Rotating left")
                        #rotate_left()
                        time.sleep(0)
                    if event.button == 7:
                        print("Rotating right")
                        #rotate_right()
                        time.sleep(0)
                if event.type == JOYBUTTONUP:
                        off()
                        time.sleep(0)
                if event.type == JOYAXISMOTION:
                    print(event.value)

                if event.type == JOYHATMOTION:
                    print(event.value)
    except KeyboardInterrupt as ex:
        print('Exiting per user request...')
    finally:
        off()

# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()