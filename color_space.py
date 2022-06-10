import cv2
import matplotlib.pyplot as plt

# baca gambar
fish = cv2.imread('koi.jpg')
# convert BGR ke RGB
fish = cv2.cvtColor(fish, cv2.COLOR_BGR2RGB)
# convert RGK ke HSV
hsv_fish = cv2.cvtColor(fish, cv2.COLOR_RGB2HSV)

# deklarasi batas bawah (orange cerah)
light_orange = (1,190,200)
# deklarasi batas atas (dark orange)
dark_orange = (18, 255, 255)

# tresholding
mask = cv2.inRange(hsv_fish, light_orange, dark_orange)
# impose gambar asli dengan mask
result = cv2.bitwise_and(fish, fish, mask=mask)

# ploting
plt.subplot(2, 2, 1)
plt.imshow(fish)
plt.subplot(2, 2, 2)
plt.imshow(hsv_fish)
plt.subplot(2, 2, 3)
plt.imshow(mask)
plt.subplot(2, 2, 4)
plt.imshow(result)
plt.show()