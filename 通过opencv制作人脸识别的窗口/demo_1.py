import cv2

image = cv2.imread("test_1.png")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(image)
print(image_gray)

