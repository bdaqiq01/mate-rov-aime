import rclpy
from rclpy.node import Node

# Import necessary ROS data types for data transferring
# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Int32, Int32MultiArray

# TODO: Put external library imports below


class ExamplePublisherNode(Node):
    def __init__(self):
        # TODO: Replace "example_publisher_node" with the name of the publisher node
        super().__init__('example_publisher_node')


        # Creates a publisher attached to this node and posting to "example_topic"
        self.publisher_handle = self.create_publisher(
            # TODO: Replace "Int32" with the corresponding type of data sent over the topic
            Int32,
            
            # TODO: Replace "example_topic" with the name of the topic
            'example_topic',
            
            # NOTE: This parameter sets how many messages are to be sent
            10,
        )

        timer_period = 1 / 10  # seconds

        # Creates a timer that publishes to "example_topic" via a fixed time period
        self.timer = self.create_timer(timer_period, self.publish_data_onto_topic)
        

    """
    Callback function for publishing data to 'example_topic'
    """
    def publish_data_onto_topic(self):
        # Create the message packet
        msg = Int32()
        msg.data = 42

        # Publish it on the topic "example_topic"
        self.publisher_handle.publish(msg)


def main(args=None):
    # Initialize ROS communication for this node
    rclpy.init(args=args)

    # Initialize the node
    node = ExamplePublisherNode()

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
