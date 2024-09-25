#Imports 

 
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

#Converts one range of numbers to a different range of numbers given the input of x 
#Thanks to Arduino for providing the formula
def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

#Changes the servo position to an angle in degrees you must use an integer
def set_sero_pos(deg):
  if servo_state == "Open":
    print("servo has moved to open position" + servo_open)
  else:
    print("servo have mosed to closed position" + servo_close)

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
  