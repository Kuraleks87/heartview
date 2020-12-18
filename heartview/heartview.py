import cv2
import numpy as np

def convert(my_name):
    """
    Parameters
    ----------
    my_name (str): Имя человека
    
        Описание функции

    Returns
    -------
    None.

    """
    print(f"Тест {my_name}")


convert('alexander')

img = cv2.imread('cat.jpg')

print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape:" +str(img.shape))

blue, green, red = cv2.split(img)

cv2.imwrite('blue.jpg',blue)
cv2.imwrite('red.jpg',red)
cv2.imwrite('green.jpg',green)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('black.jpg',gray_image)
print(gray_image)

blur = cv2.blur(gray_image,(5,5))
cv2.imwrite('black_blur.jpg',blur)

k = np.array([[-1,-1,-1],
              [-1,9,-1],
              [-1,-1,-1]])


new_img = cv2.filter2D(gray_image,-1, k)
cv2.imwrite('new_img.jpg',new_img)