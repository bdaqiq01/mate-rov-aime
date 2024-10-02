import rclpy
from rclpy.node import Node

# Import necessary ROS data types for data transferring
# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Float32MultiArray

# Library imports
import sys
import pygame
from pygame.locals import *

class controller_node(Node):
    def __init__(self):
        super().__init__('controller_node')


        # Creates a publisher attached to this node and posting to "example_topic"
        self.publisher_handle = self.create_publisher(
            Float32MultiArray,
            
            'controller_data',
            
            10,
        )

        timer_period = 1 / 10  # seconds

        # Creates a timer that publishes to "example_topic" via a fixed time period
        self.timer = self.create_timer(timer_period, self.publish_data_onto_topic)
        
    """
    Callback function for publishing data to 'example_topic'
    """
    
    def publish_data_onto_topic(self):
        data_array = [0, 0, 0, 0, 0, 0, 0]       # [buttonPress, LeftJoyX, LeftJoyY, RightJoyX, RightJoyY, DpadX, DpadY]

        for event in pygame.event.get(): #Accesses event class that reads controller interactions

            if event.type == JOYBUTTONDOWN:

                data_array[0] = float(event.button) #'button' is a part of the JOYBUTTONDOWN class

            if event.type == JOYBUTTONUP:
                data_array[0] = float(0)
            # checks which joystick is moving in which axis then outputs value to corresponding array location
            if event.type == JOYAXISMOTION:
                if event.axis == 0:
                    data_array[1] = event.value
                elif event.axis == 1:
                    data_array[2] = -event.value
                elif event.axis == 2:
                    data_array[3] = event.value
                elif event.axis == 3:
                    data_array[4] = -event.value
                else:
                    data_array[1] = 0
                    data_array[2] = 0
                    data_array[3] = 0
                    data_array[4] = 0

            # checks for Dpad being pressed and outputs event value to corresponding array location
            if event.type == JOYHATMOTION:

                data_array[5] = float(event.value[0])       #'value' is a port of the JOYHATMOTION class
                data_array[6] = float(event.value[1])

            self.get_logger().info(data_array) 

        # Create the message packet
        msg = Float32MultiArray()
        msg.data = data_array

        # Publish it on the topic "example_topic"
        self.publisher_handle.publish(msg)


def main(args=None):
    # Initialize ROS communication for this node
    rclpy.init(args=args)

    # Initialize the node
    node = controller_node()

    # Start up the node
    rclpy.spin(node)

    # Destroy the node explicitly
    node.destroy_node()

    # Shutdown ROS communication for this node
    rclpy.shutdown()


# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()