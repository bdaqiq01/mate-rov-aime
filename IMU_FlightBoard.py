import rclpy
from rclpy.node import Node
import bluerobotics_navigator as navigator

# Import necessary ROS data types for data transferring
# See links for reference:
# - Data message specification: http://wiki.ros.org/msg
# - Source files for message types: https://github.com/ros/std_msgs/tree/kinetic-devel/msg
from std_msgs.msg import Float32, Float32MultiArray

# TODO: Put external library imports below


class AccelerationPublish(Node):
    def __init__(self):
        # TODO: Replace "example_publisher_node" with the name of the publisher node
        super().__init__('AccelerationPublish')


        # Creates a publisher attached to this node and posting to "example_topic"
        self.publisher_handle = self.create_publisher(
            # TODO: Replace "Int32" with the corresponding type of data sent over the topic
            Float32MultiArray,
            
            # TODO: Replace "example_topic" with the name of the topic
            'Acceleration',
            
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
        
        #Acceleration - Float value
        #read acceleration data in X,Y,Z directions
        acceleration = navigator.read_accel()
        msg = Float32()
        mgs.data = float(acceleration)

        #Angular Velocity - float value

        # Publish it on the topic "example_topic"
        self.publisher_handle.publish(msg)


def main(args=None):
    # Initialize ROS communication for this node
    rclpy.init(args=args)

    # Initialize the node
    node = AccelerationPublish()

    # Start up the node
    i = 1
    while i = 1:
        acceleration = navigator.read_accel()
        
        #Forward is +X direction. Backward is -X direction
        forwardAcceleration = acceleration.x
        
        #Left is +Y direction. Right is -Y direction 
        sideAcceleration = acceleration.y
        
        #Up is +Z direction. Down is -Z direction
        verticalAcceleration = acceleration.z
        
        print("-1-")
    else:

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
