import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/basira/Documents/AIME/MATE-ROV-AIME-/ros2_ws/install/underwater_rover'
