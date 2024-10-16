#The following is the original logic used to create the Subscriber Node

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

#current_angle = map_range(pwm,500,2500,0,180)

 # This checks the state of the x_button and the changes the position of the servo claw accordingly 
def check_test(x_button: bool, x_check: bool):
   if x_button == False & x_check == True:
     servo_state = servo_state
     print("same")
   if x_button == False & x_check == False:
      servo_state = servo_state
      print("same") 
   if x_button == True & x_check == True:
     servo_state = "closed"
     x_check = False
     print("closed")
   if x_button == True & x_check == False:
     servo_state = "open"
     x_check = True
     print("open")


check_test(False, True)
check_test(False, False)
check_test(True, True)
check_test(True, False)

