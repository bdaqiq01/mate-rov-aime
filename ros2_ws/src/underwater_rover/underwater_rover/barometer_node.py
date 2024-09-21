import rclpy
from rclpy.node import Node

# Import necessary ROS data types for data transferring
# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Float32

# TODO: Put external library imports below

import bluerobotics_navigator as navigator
import ms5837 #pressure sensor class 

#print("Initializing navigator module.")

navigator.init() #initialzing the navigator modula
i2c = navigator.i2c_bus()  # I2C bus initialization 
pressure_sensor = navigator.ms5837.MS5837(i2c)

if not pressure_sensor.init():
    print("Failed to initialize MS5837 sensor")
    exit(1) 


class barometer_node(Node):
    def __init__(self):
        super().__init__('barometer_node')
        self.publisher_handle = self.create_publisher(
            Float32,
            'barometer_reading',
            10,
        )

        timer_period = 1 / 10  # seconds
        self.timer = self.create_timer(timer_period, self.publish_data_onto_topic)
        
    def publish_data_onto_topic(self):
        # Create the message packet
        #read pressure data 
        pressure_sensor.read() 
        env_pressure = pressure_sensor.pressure()
        msg = Float32()
        msg.data = float(env_pressure)

        # Publish it on the topic "example_topic"
        self.publisher_handle.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = barometer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
