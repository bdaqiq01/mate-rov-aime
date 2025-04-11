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

param = fetch_param('SURFACE_DEPTH')

print('name: %s\tvalue: %d' % (param['param_id'], param['param_value']))