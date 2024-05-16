import cv2
import numpy as np


def apply_kernel_on_image(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    output = np.zeros_like(image)

    for y in range(image_height - kernel_height + 1):
        for x in range(image_width - kernel_width + 1):
            output[y, x] = (
                kernel * image[y:y+kernel_height, x:x+kernel_width]).sum()

    return output


image = cv2.imread('assets/image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.array([
    [-1, -1, 0],
    [-1, 0, 1],
    [0, 1, 1]
]) / 9

cv2.imshow("test", apply_kernel_on_image(image, kernel))
cv2.waitKey()
