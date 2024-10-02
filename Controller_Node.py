# Author: Anthony Chavez

import sys
import pygame
from pygame.locals import *

pygame.init() #initializes Pygame
pygame.joystick.init() #Initializes joystick module
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())] #Initializes an array of joysticks detected

for joystick in joysticks: #Recieves name of controller
    print(joystick.get_name())

# First float: Button press
# X: 0, A: 1, B: 2, Y: 3, LB: 4, RB: 5, LT: 6, RT: 7, BACK: 8, START: 9,
# Second float: JoystickAxis -1 to 1
# Third float: Dpad left -1, right 1
# Fourth float: Dpad up 1, down -1
data_array = [0, 0, 0, 0]       # [buttonPress, JoystickAxis, DpadLeftRight, DpadUpDown]

while True:

    for event in pygame.event.get(): #Accesses event class that reads controller interactions

        if event.type == JOYBUTTONDOWN:

            data_array[0] = float(event.button) #'button' is a part of the JOYBUTTONDOWN class

        if event.type == JOYBUTTONUP:
            data_array[0] = float(0)

        if event.type == JOYAXISMOTION:

            data_array[1] = float(event.value)         #'value' is a port of the JOYAXISMOTION class

        if event.type == JOYHATMOTION:

            data_array[2] = float(event.value[0])       #'value' is a port of the JOYHATMOTION class
            data_array[3] = float(event.value[1])

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        print(data_array) 
