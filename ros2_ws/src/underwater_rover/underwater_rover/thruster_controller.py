
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import pigpio


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
        # Initialize pigpio 
        self.pi = pigpio.pi()
        self.ESS_PINS = [17, 18, 27, 22, 23, 24, 25, 5] #ECS pins 
        self.initialize_escs()

    def initiazlize_escs(self):
        for pin in self.ESS_PINS:
            self.pi.set_servo_pulsewidth(pin, 1500)
        self.get_logger().info('ESCs initialized neutral position')

    def listener_callback(self, msg):
        self.get_logger().info('Received thruster speed: "%s" ' % str(msg.data))
        self.set_thruster_speeds(msg.data)


    def set_thruster_speeds(self, speeds):
        for pin, speed in zip(self.ESS_PINS, speeds):
            self.pi.set_servo_pulsewidth(pin, speed)

def main(args = None):
    rclpy.init(args= args)
    thruster_controller = ThrusterController()
    rclpy.spin(thruster_controller)
    thruster_controller.destroy_node()
    rclpy.shutdown()


if __name__ =='__main__':
    main()