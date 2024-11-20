import bluerobotics_navigator as navigator
import time

navigator.init()

def barometer_sensor_active_duty():

    pressure_reading = navigator.read_pressure()
    # mag_reading = navigator.read_mag()
    acclearation_reading = navigator.read_accel()
    gyro_reading = navigator.read_gyro()

    print("The pressure reading is: " + str(pressure_reading))
    # print("The magnetic reading is: " + str(mag_reading))     
    print("The acceleration reading is: " + str(acclearation_reading.x)) # add the corresponding coordinate plane
    print("The yaw reading is: " + str(gyro_reading.z)) # add the corresponding coordinate plane

def main(args=None):
    while True:
        barometer_sensor_active_duty()
        time.sleep(4)
        # print("it worky")

if __name__ == '__main__':
    main()