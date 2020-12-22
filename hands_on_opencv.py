# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 23:02:32 2020

@author: SAKET
This code is inspired by a tutorial, by Bharath K: https://towardsdatascience.com/opencv-complete-beginners-guide-to-master-the-basics-of-computer-vision-with-code-4a1cd0c687f9

"""

import cv2
import numpy as np

# Read The Image 
image=cv2.imread("Lenna.png")
# Frame Title with the image to be displayed 
cv2.imshow("Pic", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the shape of the image
print(image.shape)

# Save the image
cv2.imwrite("Lenna1.png", image)

# Resizing the image
resize=cv2.resize(image, (256,256))
cv2.imshow("Pic", image)
cv2.imshow("Resized Pic", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the color image to grayscale image
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Blur the image
blur=cv2.GaussianBlur(gray, (19
                             ,19), 0)
cv2.imshow("Blur Pic", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a line 
img=np.zeros((256,256,3))
img=cv2.line(img, (0,0), (255,255), (255,0,0), 10)
cv2.imshow("Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a rectangle
img=np.zeros((256,256,3))
img=cv2.rectangle(img, (124,124), (200,200), (0,255,0), 10)
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a circle
img=np.zeros((256,256,3))
img=cv2.circle(img, (128,128), 100, (0,0,255), 10)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Put a Text in the image
img=np.zeros((512,512,3))
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "Hello! What's up?", (150,150), font, 1, (0,255,255), 
            3, cv2.LINE_8)
cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a polygon
img=np.zeros((256,256,3))
pts = np.array([[25, 70], [25, 160],  
                [110, 200], [200, 160],  
                [200, 70], [110, 20]], 
               np.int32) 
print(pts)
pts=pts.reshape((-1,1,2))
print(pts.shape, pts)
cv2.polylines(img, [pts], True, (0,0,255), 10)
cv2.imshow("Polygon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Accessing the web cam
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow("capture",frame)
    key=cv2.waitKey(1)
    print(key)
    if(key==ord(' ')):
        break
cap.release()
cv2.destroyAllWindows()
    