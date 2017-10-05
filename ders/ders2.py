import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("image.png")
print(img.shape)

img2 = np.zeros((256, 200, 3))
print(img2.shape)
for i in range(200):
    for j in range(256):
        img2[j,i] = img[i, j]
plt.subplot(2,3,1),plt.imshow(img2)
mpimg.imsave("image3.png", img2)