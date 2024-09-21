import rclpy
from rclpy.node import Node

# Import necessary ROS data types for data transferring
# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Int32, Int32MultiArray

# TODO: Put external library imports below


class ExampleSubscriberNode(Node):
    def __init__(self):
        # TODO: Replace "example_subscriber_node" with the name of the subscriber node
        super().__init__('example_subscriber_node')

        
        # Creates a subscriber attached to this node and listening to "example_topic"
        self.subscriber_handle = self.create_subscription(
            # TODO: Replace "Int32" with the corresponding type of data sent over the topic
            Int32,
            
            # TODO: Replace "example_topic" with the name of the topic
            'example_topic',
            
            # TODO: Replace "on_subscriber_data_received" with the name of the callback function
            self.on_subscriber_data_received,
            
            # NOTE: This parameter sets how many messages are to be received
            10,
        )


    """
    Callback function for when data is received via 'example_topic'
    """

    def on_subscriber_data_received(self, msg):
        self.get_logger().info(f'Received data: {msg.data}')


def main(args=None):
    # Initialize ROS communication for this node
    rclpy.init(args=args)

    # Initialize the node
    node = ExampleSubscriberNode()

    # Start up the node
    # NOTE: This line will block until a shutdown command is received (like Ctrl + C)
    rclpy.spin(node)

    # Destroy the node explicitly
    # NOTE: optional - otherwise it will be done automatically when the garbage collector destroys it
    node.destroy_node()

    # Shutdown ROS communication for this node
    rclpy.shutdown()


# Only run the 'main()' code when calling this script directly
if __name__ == '__main__':
    main()
