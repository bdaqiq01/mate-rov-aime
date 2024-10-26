# Library imports
import bluerobotics_navigator as navigator
from bluerobotics_navigator import PwmChannel
import numpy as np
import time
 
navigator.init()

#Converts one range of numbers to a different range of numbers given the input of x 
#Thanks to Arduino for providing the formula
def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

 
 
class servo_claw_1(): # Creates a node
  def __init__(self): #Initializes the node 
    # super().__init__('servoData')
    # self.subscriber_handle = self.create_subscription ( #creates the subscriber 
    #  Float32Array, #the data type the information is 
    #  'controller_data', #defines the topic the topic
    #  self.on_subscriber_data_received,
    #  1, #number of times the message is sent 
    # )
    
    #Set of variables to used to decide the position of a servo based on a button 
    #TO DO: make self.x_button grab indext 0 from the topic controller_input
    self.x_button = 0
    self.x_check = False
    # The angle of the open of closed state of the claw set in degrees
    self.left_claw_open = 0
    self.left_claw_closed = 180
   
 #takes a pwm value and turns it into degrees   
  def pwm_to_deg(self, pwm):
    return map_range(pwm, 500,1200,0,180)

  #takes a degree value and turns it into pwm
  def deg_to_pwm(self, deg):
    return map_range(deg,0,180,500,1200)
    
   # Changes the servo position with a degree value
  def set_sero_pos(self, deg):
    pwm = self.deg_to_pwm(deg)
    navigator.set_pwm_channel_value(PwmChannel.Ch8, pwm)

  
  #This is where your logic goes
  def on_subscriber_data_received(self, x_pressed):
    navigator.set_pwm_freq_hz(1200)
    navigator.set_pwm_enable(True)
    self.x_button = x_pressed
    # Toggles the position of the claw to being either open of closed with a push of a button
    if self.x_button != True & self.x_check == True:
        
        pass
    if self.x_button != True & self.x_check == False:
        
        pass
    if self.x_button == True & self.x_check == True:
        
        self.set_sero_pos(self.left_claw_close)
        self.x_check = False
    if self.x_button == True & self.x_check == False:
        self.set_sero_pos(self.left_claw_open)
        self.x_check = True

    # print(f'Received data: {msg.data}')

def main(args=None):
  node = servo_claw_1()

  node.on_subscriber_data_received(False)
  time.sleep(2)

  node.on_subscriber_data_received(True)
  time.sleep(2)

  node.on_subscriber_data_received(False)

if __name__ == '__main__':
  main()
  


#The following is the original logic used to create the Subscriber Node

# #Variables

# x_button = bool()
# x_check = False
# servo_state = "Open"
# #These two variables are the open and closed state of the servo 
# servo_open = 0
# servo_close = 180
# #This is used to store the current value of the signal pin the servo is connected to
# pwm = int()
# #The folllowing two variables are the pwm ranges for the servo and it should only be two numbers
# pwm_range = [500,1200]
# #This sets displays the current pos. of the servo in degrees
# current_angle = int()

# #Functions


# #Changes the servo position to an angle in degrees you must use an integer

#   current_angle = map_range(pwm,500,2500,0,180)

# # This checks the state of the x_button and the changes the position of the servo claw accordingly 
# while True:
#   if x_button == False & x_check == True:
#     servo_state = servo_state
#   if x_button == False & x_check == False:
#      servo_state = servo_state 
#   if x_button == True & x_check == True:
#     servo_state = "closed"
#     x_check = False
#     set_sero_pos("closed")
#   if x_button == True & x_check == False:
#     servo_state = "open"
#     x_check = True
#     set_sero_pos("open")
  