import rclpy
from rclpy.node import Node

# Import necessary ROS data types for data transferring
# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Float32MultiArray

# Library imports
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import numpy as np

class thruster_controller_node(Node):
    def __init__(self):
        super().__init__('thruster_controller_node')

        # defines the duty cycle when using direction functions
        self.magnitude = 0.5

        # Creates a subscriber attached to this node and listening to "controller_data"
        self.subscriber_handle = self.create_subscription(
            Float32MultiArray,  
            
            'controller_data',
            
            self.on_Controller_data_received,
            
            10,
        )

        # at this line i have the msg stored in he msg varible which means I can start my while loop with if statments checking on msg
        # check turtlebot 4 python programs
           
            


    #  expected a list of 6 values, each corresponds to a thruster and this function assigns each of them with a pwm signal
    def set_pwm_channels_values(values):
        for i, value in enumerate(values):
            navigator.set_pwm_channels_duty_cycle(PwmChannel.Ch[i+1], value)

    

    # direction functions assign pwm channels with signal for certain movement
    def go_up(self):
        # array of values for which thruster should turn on in which directon positive or negative
        up = np.array(1, 1, 0, 0, 0, 0)
        # array is multiplied by magnitude to adjust the speed of movement
        up_result = np.array(up * self.magnitude)
        # outputs pwm signal to correct thrusters for movement
        set_pwm_channels_values(up_result)

    def go_down(self):
        down = np.array(-1, -1, 0, 0, 0, 0)
        down_result = np.array(down * self.magnitude)
        set_pwm_channels_values(down_result)

    def go_left(self):
        left = np.array(0, 0, -1, 0, -1, 0)
        left_result = np.array(left * self.magnitude)
        set_pwm_channels_values(left_result)

    def go_right(self):
        right = np.array(0, 0, 0, -1, 0, -1)
        right_result = np.array(right * self.magnitude)
        set_pwm_channels_values(right_result)

    def go_back(self):
        back = np.array(0, 0, 0, 0, 1, 1)   
        back_result = np.array(back * self.magnitude)
        set_pwm_channels_values(back_result)

    def go_forward(self):
        forward = np.array(0, 0, 1, 1, 0, 0)
        forward_result = np.array(forward * self.magnitude)
        set_pwm_channels_values(forward_result)

    # turns all thrusters off
    def off(self):
        navigator.set_pwm_channels_duty_cycle(PwmChannel.All, 0)


    """
    Callback function for when data is received via 'example_topic'
    """

    # msg will hold the information from the topic
    def on_Controller_data_received(self, msg):
        self.get_logger().info(f'Received data: {msg.data}')

        if self.msg.data == 0:
            self.off()
        elif self.msg.data == 1:
            self.go_up()
        elif self.msg.data == 2:
            self.go_down()
        elif self.msg.data == 3:
            self.go_left()
        elif self.msg.data == 4:
            self.go_right()
        elif self.msg.data == 5:
            self.go_back()
        elif self.msg.data == 6:
            self.go_forward()        

# Initializes the Navigator module with default settings.
bluerobotics_navigator.init()
# Setup for PWM Channels 
# Referencing PWM Channels "PwmChannel.Ch1" or "PwmChannel.All"
navigator.set_pwm_freq_hz(1000)
# Enables or disables the PWM chip
navigator.set_pwm_enable(True)

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

def main(args=None):
    # Initialize ROS communication for this node
    rclpy.init(args=args)

    # Initialize the node
    node = thruster_controller_node()

    # Start up the node
    # NOTE: This line will block until a shutdown command is received (like Ctrl + C)
    rclpy.spin(node)

    # while loop with code goes here



    # Destroy the node explicitly
    # NOTE: optional - otherwise it will be done automatically when the garbage collector destroys it
    node.destroy_node()

    # Shutdown ROS communication for this node
    rclpy.shutdown()


# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()

