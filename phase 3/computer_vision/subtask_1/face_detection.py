import cv2
import matplotlib.pyplot as plt  
image = cv2.imread("noisy_face.jpg")  #read the image
print(image is None)  #check if the image was loaded successfully
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #convert the image to grayscale
print(gray is None)  #check if the image was converted to grayscale
# average filter
average = cv2.blur(gray, (5, 5))  #apply smoothing to the image using average filter
# median filter
median = cv2.medianBlur(gray, 5)  #apply smoothing to the image using median filter
# gaussian filter
gaussian = cv2.GaussianBlur(gray, (5, 5), 0)  #apply smoothing to the image using gaussian filter
# canny edge detection
average_edges = cv2.Canny(average, 100, 200)  #detect edges in the image after applying the average filter
median_edges = cv2.Canny(median, 100, 200)  #detect edges in the image after applying the median filter
gaussian_edges = cv2.Canny(gaussian, 100, 200)  #detect edges in the image after applying the gaussian filter
# create a figure to display all images
plt.figure(figsize=(15, 8))
plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 4, 2)
plt.imshow(average, cmap="gray")
plt.title("Average Filter")
plt.axis("off")

plt.subplot(2, 4, 3)
plt.imshow(median, cmap="gray")
plt.title("Median Filter")
plt.axis("off")

plt.subplot(2, 4, 4)
plt.imshow(gaussian, cmap="gray")
plt.title("Gaussian Filter")
plt.axis("off")

plt.subplot(2, 4, 5)
plt.imshow(average_edges, cmap="gray")
plt.title("Average Edges")
plt.axis("off")

plt.subplot(2, 4, 6)
plt.imshow(median_edges, cmap="gray")
plt.title("Median Edges")
plt.axis("off")

plt.subplot(2, 4, 7)
plt.imshow(gaussian_edges, cmap="gray")
plt.title("Gaussian Edges")
plt.axis("off")

plt.tight_layout()
plt.show()