import time
import RPi.GPIO as GPIO

# Setup the GPIO mode and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pins for each ESC (adjust according to your wiring)
esc_pins = [17, 18, 27, 22, 23, 24, 25, 12]  # Example GPIO pin numbers for 8 ESCs

# Set up each GPIO pin as an output
for pin in esc_pins:
    GPIO.setup(pin, GPIO.OUT)

# Create a PWM object for each ESC with a 50Hz frequency (standard for ESCs)
esc_pwms = [GPIO.PWM(pin, 50) for pin in esc_pins]

# Start PWM with a neutral signal (stop signal for ESCs)
for pwm in esc_pwms:
    pwm.start(7.5)  # 7.5% duty cycle corresponds to neutral position (no movement)

def set_thruster_speed(thruster_channel, speed):
    """
    Set the speed of a thruster.
    :param thruster_channel: Channel number (0-7) for the thruster.
    :param speed: Speed value (-1.0 to 1.0).
    """
    # Ensure the speed is within the valid range
    speed = max(-1.0, min(1.0, speed))
    
    # Convert speed to a duty cycle percentage
    duty_cycle = 7.5 + (2.5 * speed)  # 7.5 is neutral, +2.5 is full forward, -2.5 is full reverse

    # Set the duty cycle for the specific thruster
    esc_pwms[thruster_channel].ChangeDutyCycle(duty_cycle)

def test_thruster(thruster_channel):
    """
    Test a single thruster by ramping the speed up and down.
    :param thruster_channel: Channel number (0-7) for the thruster.
    """
    print(f"Testing thruster {thruster_channel} individually")

    # Gradually increase speed from 0 to full forward
    for speed in range(0, 11):
        set_thruster_speed(thruster_channel, speed / 10.0)
        time.sleep(1)  # Hold the speed for 1 second

    # Gradually decrease speed back to neutral
    for speed in range(10, -1, -1):
        set_thruster_speed(thruster_channel, speed / 10.0)
        time.sleep(1)

    # Gradually increase speed from 0 to full reverse
    for speed in range(0, -11, -1):
        set_thruster_speed(thruster_channel, speed / 10.0)
        time.sleep(1)

    # Gradually decrease speed back to neutral
    for speed in range(-10, 1):
        set_thruster_speed(thruster_channel, speed / 10.0)
        time.sleep(1)

    # Stop the thruster
    set_thruster_speed(thruster_channel, 0)
    print(f"Thruster {thruster_channel} individual test complete.\n")

def test_all_thrusters_together():
    """
    Test all thrusters together by ramping the speed up and down.
    """
    print("Testing all thrusters together")

    # Gradually increase speed from 0 to full forward for all thrusters
    for speed in range(0, 11):
        for i in range(8):
            set_thruster_speed(i, speed / 10.0)
        time.sleep(1)  # Hold the speed for 1 second

    # Gradually decrease speed back to neutral for all thrusters
    for speed in range(10, -1, -1):
        for i in range(8):
            set_thruster_speed(i, speed / 10.0)
        time.sleep(1)

    # Gradually increase speed from 0 to full reverse for all thrusters
    for speed in range(0, -11, -1):
        for i in range(8):
            set_thruster_speed(i, speed / 10.0)
        time.sleep(1)

    # Gradually decrease speed back to neutral for all thrusters
    for speed in range(-10, 1):
        for i in range(8):
            set_thruster_speed(i, speed / 10.0)
        time.sleep(1)

    # Stop all thrusters
    for i in range(8):
        set_thruster_speed(i, 0)
    print("All thrusters combined test complete.\n")

def main():
    # Test each thruster individually
    for i in range(8):
        test_thruster(i)
        time.sleep(2)  # Small delay between tests

    # Test all thrusters together
    test_all_thrusters_together()

    # Clean up the GPIO settings
    for pwm in esc_pwms:
        pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
