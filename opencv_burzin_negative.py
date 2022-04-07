# Jose Bendana 04/06/22
# Import the package
import cv2

# Load Image from directory

img = cv2.imread('/Users/josebendana/Desktop/Spring 2022/ME 369/Lightning Talk /Burzin final.png',1 )

# Make new image by inverting BGR values
img_neg = 255 - img


# Save updated negative image to directory
cv2.imwrite('buz.png',img)

# This image is the cropped using and placed into google slides with animation

# "https://half-6.github.io/lf-freehand-cropper/"

