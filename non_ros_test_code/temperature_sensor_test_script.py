
# importing the Navigtor files 
import bluerobotics_navigator as navigator 
import tsys01

# importing the data type
from std_msgs.msg import Float32

# initalizing Navigator 
navigator.init()
if not navigator.init():                
    print("The Navigator did not initalize")
    exit(1)
print("The Navigator has initalized")

# seting up the i2c bus for the temperature sensor
i2c = navigator.i2c_bus(0) # setting it to bus zero

temperature_sensor = navigator.tsys01.TSYS01(i2c) # Setting up the sensor and making it connect to the 12c bus

# initalizng the temperature sensor
temperature_sensor.init()
if not temperature_sensor.init():
    print("The temperature sensor did not initalize")
    exit(1)
if temperature_sensor.init():
    print("The temperature sensor has initalized")

class test_temperature_sensor():
    # function that stores the action code for the temperature sensor
    def sensor_active_duty(self):
        # reading the temperature and sending the status of the reading
        temperature_sensor.read()
        if not temperature_sensor.read():
            print("Error reading sensor")
            exit(1)
        print("The temperture has read the surroundings")
        
        # gets the reading of the temperature and stores it in temp_reading
        temp_reading = temperature_sensor.temperature()
        if not temperature_sensor.temperautre():
            print("The temperature reading has failed to be stored")
            exit(1)
        print("The temperature reading has been stored in temp_reading")
        
        # setting the message type and sets the data for the message equal to the reading
        msg = Float32()
        msg.data = float(temp_reading)
        print("The temperature is that was read is " + msg.data)

    # function for the timer
    # this is probably not needed to run an check if the code is ran properly
    def timer(self):
        time_period = 1/10
        self.timer = self.create.timer(time_period, self.msg.data)
        
    
