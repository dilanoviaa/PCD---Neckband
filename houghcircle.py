# import the necessary packages
import cv2
import os, os.path
import numpy as np
import glob
# debug info OpenCV version
print("OpenCV version: " + cv2.__version__)

# image path and valid extensions
imageDir = "E:\pcd_sapi\\test1"  # specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]  # specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

# create a list all files in directory and
# append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

# loop through image_path_list to open each image
for imagePath in image_path_list:
    img = cv2.imread(imagePath, 0)

    # img = cv2.medianBlur(img, 5)
    gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=290, param2=55, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    cropSize = (100, 100)
    for i in circles[0, :]:
        cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(gray, (i[0], i[1]), 2, (0, 0, 255), 3)
        cropCoords = (
        max(0, i[1] - cropSize[0] // 2), min(img.shape[0], i[1] + cropSize[0] // 2), max(0, i[0] - cropSize[1] // 2),
        min(img.shape[1], i[0] + cropSize[1] // 2))
        crop = gray[cropCoords[0]:cropCoords[1], cropCoords[2]:cropCoords[3]]

    # display the image on screen with imshow()
    # after checking that it loaded
    print(crop)
    # if crop is not None:
    #     cv2.imshow(imagePath, crop)
    # elif crop is None:
    #     print("Error loading: " + imagePath)
        # end this loop iteration and move on to next image
        # continue
cv2.waitKey(0)
cv2.destroyAllWindows()

    # wait time in milliseconds
    # this is required to show the image
    # 0 = wait indefinitely
    # exit when escape key is pressed
    # key = cv2.waitKey(0)
    # if key == 27:  # escape
    #     break

# close any open windows
# cv2.destroyAllWindows()