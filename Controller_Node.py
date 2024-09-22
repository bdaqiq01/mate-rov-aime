# Author: Anthony Chavez

import sys
import pygame
from pygame.locals import *

pygame.init() #initializes Pygame
pygame.joystick.init() #Initializes joystick module
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())] #Initializes an array of joysticks detected

for joystick in joysticks: #Recieves name of controller
    print(joystick.get_name())

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
