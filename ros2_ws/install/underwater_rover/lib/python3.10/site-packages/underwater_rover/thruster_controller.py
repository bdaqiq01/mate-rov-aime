
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import pigpio


class ThrusterController(Node):
    def __init__(self):
        super().__init__('thruster_controller') #initialzie with the'thruster controllr' name 
        self.subscription = self.create_subscription(  #creates a subscriptin to the thruster_speeds topic
            Float32MultiArray,  # msg type 
            'thruster_speeds', # name of the topic
            self.listener_callback, # the listener-callback is called when ever a msg is received
            10
        )
        self.subscription
        # Initialize pigpio 
        self.pi = pigpio.pi() #initialize the pigpio library for controlling GPIO pins
        self.ESS_PINS = [17, 18, 27, 22, 23, 24, 25, 5] #ECS pins 
        self.initialize_escs() # calls the method to initalize the pins

    def initiazlize_escs(self):
        for pin in self.ESS_PINS:
            self.pi.set_servo_pulsewidth(pin, 1500)
        self.get_logger().info('ESCs initialized neutral position') #logs the message indicating its state

    def listener_callback(self, msg): # method called whenever there is a msg received from the topib
        self.get_logger().info('Received thruster speed: "%s" ' % str(msg.data))
        self.set_thruster_speeds(msg.data) #calls the method to update the thruster speeds based on the data


    def set_thruster_speeds(self, speeds): # method to set the speeds
        for pin, speed in zip(self.ESS_PINS, speeds):
            self.pi.set_servo_pulsewidth(pin, speed) #sets the pulse widthe for each pin to control the speed 

def main(args = None):
    rclpy.init(args= args) #initiats ros2 communication
    thruster_controller = ThrusterController() #creats an instance of the node
    rclpy.spin(thruster_controller) #keeps the node running allowing it to process callbacks
    thruster_controller.destroy_node() #cleans up resources when the node is stopped 
    rclpy.shutdown() #shuts down ros2 client communication


if __name__ =='__main__':
    main()