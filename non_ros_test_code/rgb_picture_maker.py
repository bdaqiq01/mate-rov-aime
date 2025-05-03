import depthai as dai
import cv2
import time
import keyboard
import os

# Create pipeline
pipeline = dai.Pipeline()

# Create a ColorCamera node
camRgb = pipeline.create(dai.node.ColorCamera)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_12_MP)  # 4056x3040
camRgb.setStillSize(4056, 3040)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

# Create control input to trigger still capture
controlIn = pipeline.create(dai.node.XLinkIn)
controlIn.setStreamName("control")
controlIn.out.link(camRgb.inputControl)

# Create output for still image
xoutStill = pipeline.create(dai.node.XLinkOut)
xoutStill.setStreamName("still")
camRgb.still.link(xoutStill.input)

#Output Folder
outputFolder = "unstitchedImages/"


# Start device
with dai.Device(pipeline) as device:
    stillQueue = device.getOutputQueue(name="still", maxSize=1, blocking=True)
    controlQueue = device.getInputQueue(name="control")

    print("Press SPACE to capture a 12MP RGB still image, or ESC to exit.")

    while True:
        key = cv2.waitKey(1)
        if keyboard.is_pressed('esc'):  # ESC to exit
            break
        elif keyboard.is_pressed(' '):  # SPACE to take photo
            ctrl = dai.CameraControl()
            ctrl.setCaptureStill(True)
            controlQueue.send(ctrl)

            print("Capturing...")
            imgFrame = stillQueue.get()
            frame = imgFrame.getCvFrame()

            filename = outputFolder + f"rgb_img_to_stitch_{int(time.time())}.jpg"
            os.path.join(outputFolder, filename)
            cv2.imwrite(filename, frame)
            print(f"Saved 12MP RGB image: {filename}")

    cv2.destroyAllWindows()

