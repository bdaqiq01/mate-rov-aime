"""
Example code of how to read and write vehicle parameters using pymavlink
"""

import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Returns a parameter value
def fetch_param(param_name):
    while True:
        master.mav.param_request_read_send(
            master.target_system, master.target_component,
            param_name.encode('utf-8'),
            -1
        )

        # Read ACK
        # IMPORTANT: The receiving component should acknowledge the new parameter value by sending a
        # param_value message to all communication partners.
        # This will also ensure that multiple GCS all have an up-to-date list of all parameters.
        # If the sending GCS did not receive a PARAM_VALUE message within its timeout time,
        # it should re-send the PARAM_SET message.
        message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()

        if (message['param_id'] == param_name):
            return {
                'param_id': param_name,
                'param_value': message['param_value']
            }
        else:
            # Try again
            pass

# Changes parameter to set value. See https://ardupilot.org/sub/docs/parameters.html for reference values
def set_param(param_name, param_value):
    master.mav.param_set_send(
        master.target_system, master.target_component,
        param_name.encode('utf-8'),
        float(param_value),
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32
    )

# Prints value of yaw -180 to 180 degrees with 0 representing north
def fetch_yaw():
    while True:
        msg = master.recv_match(type='ATTITUDE', blocking=True)
        yaw_rad = msg.yaw
        yaw_deg = yaw_rad * 180.0 / 3.14159
        return yaw_deg

# Sends RC values to a given RC channel
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.

# Disables all thrusters by setting them to neutral
def set_rc_neutral():
    for i in range(1,7):
        set_rc_channel_pwm(i, 1500)
    

# Rotates ROV given a pwm value (1100-1900) pwm>1500 for clockwise
def set_rc_rotate(pwm):
    set_rc_channel_pwm(1, -pwm)
    set_rc_channel_pwm(2, pwm)
    set_rc_channel_pwm(3, pwm)
    set_rc_channel_pwm(4, -pwm)

# Sets all thrusters to rc mode for custom control
def set_rc_mode():
    set_param('SERVO_1Function', 51)
    set_param('SERVO_2Function', 52)
    set_param('SERVO_3Function', 53)
    set_param('SERVO_4Function', 54)
    set_param('SERVO_5Function', 55)
    set_param('SERVO_6Function', 56)

# Sets all thrusters to servo mode for manual control
def set_servo_mode():
    set_param('SERVO_1Function', 33)
    set_param('SERVO_2Function', 34)
    set_param('SERVO_3Function', 35)
    set_param('SERVO_4Function', 36)
    set_param('SERVO_5Function', 37)
    set_param('SERVO_6Function', 38)


# SERVO_1Function 33-40 Motor, 51-66 RCIN
param = fetch_param('SERVO_1Function')
print('name: %s\tvalue: %d' % (param['param_id'], param['param_value']))

set_rc_mode()
param = fetch_param('SERVO_1Function')
print('name: %s\tvalue: %d' % (param['param_id'], param['param_value']))

set_rc_rotate(1600)
time.sleep(3)
set_rc_neutral()
