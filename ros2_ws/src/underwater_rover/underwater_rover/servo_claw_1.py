#Imports 
import rclpy
from rclpy.node import Node

# Importing necessary ros data types 
from std.msgs.msg import Float32Array
from std.msgs.msg import Bool32
 

#Converts one range of numbers to a different range of numbers given the input of x 
#Thanks to Arduino for providing the formula
def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

 
 
class servo_claw_1(Node): #creating a class for the 
  
  def __init__(self):
    super().__init__('servoData')
    self.subscriber_handle = self.create_subscription ( #creates the subscriber 
     Float32Array, #the data type the information is 
     'controller_input', #defines the topic the topic
     self.on_subscriber_data_received,
     10, #number of times the message is sent 
    )
    
    
    self.x_check = False
    self.is_left_claw_open = True
   
  def write_to_servo(self, deg):
    pwm = self.pwm_to_deg(deg)
    #TO DO: write to servo
    
    
  def pwm_to_deg(self, pwm):
    return map_range(pwm, 500,1200,0,180)

  def deg_to_pwm(self, deg):
    return map_range(deg,0,180,500,1200)
    
  def set_sero_pos(self, deg):
    pass
    # if servo_state == "Open":
    #   print("servo has moved to open position" + servo_open)
    # else:
    #   print("servo have mosed to closed position" + servo_close)


  
  #This is where your logic goes
  def on_subscriber_data_received(self, msg):
    
        self.get_logger().info(f'Received data: {msg.data}')

def main(args=None):
  rclpy.init(args=args)
  
  node = servo_claw_1()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
  
  
#Variables

x_button = bool()
x_check = False
servo_state = "Open"
#These two variables are the open and closed state of the servo 
servo_open = 0
servo_close = 180
#This is used to store the current value of the signal pin the servo is connected to
pwm = int()
#The folllowing two variables are the pwm ranges for the servo and it should only be two numbers
pwm_range = [500,1200]
#This sets displays the current pos. of the servo in degrees
current_angle = int()

#Functions


#Changes the servo position to an angle in degrees you must use an integer

  current_angle = map_range(pwm,500,2500,0,180)

# This checks the state of the x_button and the changes the position of the servo claw accordingly 
while True:
  if x_button == False & x_check == True:
    servo_state = servo_state
  if x_button == False & x_check == False:
     servo_state = servo_state 
  if x_button == True & x_check == True:
    servo_state = "closed"
    x_check = False
    set_sero_pos("closed")
  if x_button == True & x_check == False:
    servo_state = "open"
    x_check = True
    set_sero_pos("open")
  