#!/usr/bin/env python3
import rclpy;
from rclpy.node import Node

import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel

# Initializes the Navigator module with default settings.
bluerobotics_navigator.init()

navigator.set_pwm_freq_hz(1000)
navigator.set_pwm_channel_duty_cycle(PwmChannel.Ch1, 0.5)
# Enables or disables the PWM chip
navigator.set_pwm_enable(True)
bluerobotics_navigator.set_pwm_channel_value(PwmChannel.Ch1, 0.5)
#value = 4095 * pulse_duration / cycle_period

# Turn off all PWM Signals

bluerobotics_navigator.set_pwm_channel_value(PwmChannel.All, 0)
Function for direction would have 6 of these based on table in Thruster Controller Notes
# Set PWM Signal



class MyNode(Node):

    def __init__(self):
        super().__init__("Thruster_controller")
        self.create_timer(0.001, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Ros2")

class bluerobotics_navigator.PWMChannel
    Ch1 =
    

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== '__main__':
    main()