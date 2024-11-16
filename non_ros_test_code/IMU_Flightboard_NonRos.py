# importing the Navigtor files 
import bluerobotics_navigator as navigator 

# importing the data type
from std_msgs.msg import Float32

# initalizing Navigator 
navigator.init()
if not navigator.init():                
    print("The Navigator did not initalize")
    exit(1)
print("The Navigator has initalized")



def main(args=None):

    i = 1
    while i = 1:
        acceleration = navigator.read_accel()
        forward_acc = acceleration.x
        side_acc = acceleration.y
        vert_acc = acceleration.z
        print("Forward Accel: ")
        print(forward_acc)
        print(". ")
        print("Side Accel: ")
        print(side_acc)
        print(". ")
        print("Vertical Accel: ")
        print(vert_acc)
        print(". ")
    
    else:
