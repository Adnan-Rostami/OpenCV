# Import packages
import cv2
import numpy
import matplotlib.pyplot as plt

# Reading a image
firstpic = cv2.imread('Pictures/Cat.jpg')
secondpics = cv2.cvtColor(firstpic, cv2.COLOR_BGR2RGB)

# Showing the image in computer view (BGR)
plt.imshow(firstpic)
plt.title('Cat in computer view (BGR)')
plt.show()

# Showing the image in human view (RGB)
plt.imshow(secondpics)
plt.title('Cat in human view (RGB)')
plt.show()

image = cv2.rectangle(firstpic, (800,3200), (3200,400), color=(255,255,255), thickness= 15)
finalImage =  cv2.putText(img =image,
                     text = "Cat",
                     org =  (220,500),
                     fontFace=cv2.FONT_HERSHEY_COMPLEX,
                     fontScale = 10,
                     thickness =15,
                     color = (255,255,255) )

plt.imshow(cv2.cvtColor(finalImage, cv2.COLOR_BGR2RGB))
plt.title('Cat')
plt.show()

# Svae the file
cv2.imwrite("output.jpg",finalImage)
