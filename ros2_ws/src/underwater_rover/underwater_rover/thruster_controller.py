
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class ThrusterController(Node):
    def __init__(self):
        super().__init__('thruster_controller')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'thruster_speeds',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('Received thruster speed: "%s" ' % str(msg.data)) 

    def main(args = None):
        rclpy.init(args= args)
        thruster_controller = ThrusterController()
        rclpy.spin(thruster_controller)
        rclpy.shutdown()