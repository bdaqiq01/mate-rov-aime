import rclpy
from rclpy.node import node
from std_msgs.msg import Int32, Int32MultArray


class ExamplePublisherNode(Node):
    def __init__(self):
        # TODO: replace 'example_publisher_node'with name of publisher node
        super().__init__('example_publisher_node')

        self.publisher_handle = self.create_publisher(
            # TODO replace "Int32" with the corresponding data type sent over the topic
            Int32,
            
            
            'example_topic',

            #number messages to be sent
            10,
        )

        TImer_period = 1/10 # seconds

        self.timer = self.create_timer(timer_period.)