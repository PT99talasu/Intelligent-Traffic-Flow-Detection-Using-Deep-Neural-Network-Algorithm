import cv2
import os
from glob import glob

# Open the video file
vidcap = cv2.VideoCapture('D:\\Sem3\\Project\\Traffic\\source code\\traffic2.mp4')

# Check if the video file was opened successfully
if not vidcap.isOpened():
    print("Error opening video stream or file")

count = 0
while True:
    # Read a frame from the video
    success, image = vidcap.read()

    # If no frames were read, break out of the loop
    if not success:
        break

    # Save specific frames to the "images" directory
    if count == 0 or count % 500 == 0:
        cv2.imwrite("D:\\Sem3\\Project\\Traffic\\source code\\images/frame%d.jpg" % count, image)

    print('Read a new frame: ', success)
    count += 1

# Release the video capture object
vidcap.release()