import cv2
from matplotlib import pyplot as plt
image = cv2.imread('red_eyes.jpg',0)
image = cv2.medianBlur(image,5)
ret,threshold1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
threshold2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
threshold3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [image, threshold1, threshold2, threshold3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()