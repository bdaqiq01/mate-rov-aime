import keyboard
import panorama_maker as pm
import pano_viewer

on = True
while on:
    ## When "a" is pressed the robot will start spinning and take photos every 18 degrees
    if keyboard.is_pressed('a'):
        print('The robot is turning and taking photos')
    ## When "p" is pressed the panorama code will run and create a panorama from the photos taken previously
    if keyboard.is_pressed('p'):
        print("panorama stitching has started")
        pm.main()
        print("panorama has been created!!")
    ## When "v" is pressed this will display the panorama in a 360 panorama viewer
    if keyboard.is_pressed('v'):
        print("panorama viewer is on")
        pano_viewer.main()
    ##When "0" is pressed this program ends
    if keyboard.is_pressed('0'):
        print("exiting program")
        on = False