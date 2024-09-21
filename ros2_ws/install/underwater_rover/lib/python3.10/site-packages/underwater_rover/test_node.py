#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class myNode(Node):  #node class 
    def __init__(self):
        super().__init__('first_node')   #the node name when we run it 
        self.get_logger().info("hello from ross 2") #this is what the node says when it is executed

def main(args = None):
    rclpy.init(args= args)  #initialize ros2 communication 
    node = myNode()
    rclpy.spin(node)  #
    rclpy.shutdown()  #shit down ros2 communication
    
if __name__ == '__main__':
    main()