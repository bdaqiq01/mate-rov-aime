# !/usr/bin/env python3

# importing the basic python commands, functions, and classes
import rclpy
from rclpy.node import Node

# Importing necessary ros data types transferring 
from std_msgs.msg import Float32

# ask about this on tuesday - having trouble downloading libraries 
# sudo apt-get update // sudo apt-get install -y -python3-smbus
import bluerobotics_navigator as navigator
import tsys01 # i think this is the temperature sensor classs

navigator.init() # this is initalizing navigator
i2c = navigator.i2c_bus(0) # this is setting the bus and initalizing 

'''temperature_sensor = navigator.tsys01.TSYS01(i2c) ''' # this is probably not needed, check with team
# or 
temperature_sensor = tsys01.TSYS01(i2c)

temperature_sensor.init() # this is initalizing the sensor

if not temperature_sensor.init():
    print("Error initalizing sensor")
    exit(1)

# this may not be nessescary, ask on tuesday, i think that this is always never going to have reading because it is positioned before the code even tell the senors to do the reading
'''
if not temperature_sensor.read():
    print("Error reading sensor")
    exit(1)
'''


class temerature_node(Node): # creating the class for the temperature class

    def __init__(self): # initalize temperature_node
        super().__init__('check_temp') # family initalize
        self.publisher_handle = self.create_publisher( # create a publisher using the temperature class and storing it sel.publisher_handle
            Float32,        # data type Float32
            'temp_data',    # name of topic
            10,             # The amount of times that the message is sent
        )
        self.get_logger().info("External temperature is being read") # telling that the data is being read but it might spam it 

        # timer_period_sec = 1 / 10 {{This may not be needed ask about it on friday}}
        timer_period_sec = 1/10 # seconds 
        self.timer = self.create_timer(timer_period_sec, self.publish_temp_into_topic) # every 
    
    def publish_temp_into_topic(self):
        # creating a message packet
        # reading the temperature data
        temperature_sensor.read()
        temp_reading = temperature_sensor.temperature() # this get the temperature in default unit Celcius and storing it in temp_reading
        msg = Float32()                                 # setting the msg variablie = Float32 data type
        msg.data = float(temp_reading)                  # storing temp_reading as a float inside the msg variable as data

        # Publish it in the topic temp_data
        self.publisher_handle.publish(msg) # takes the data from publisher handle and publishes it into the temp_data topic

        


def main(args=None):
    rclpy.init(args=args)
    node = temerature_node
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



