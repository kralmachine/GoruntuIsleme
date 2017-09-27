import matplotlib.pyplot as plt
from masking import createCircularMask

img = plt.imread("image.png")
h, w = img.shape[:2]
radius = h/4
mask = createCircularMask(h, w, radius=radius)
img[~mask] = 0
plt.imsave("image2.png", img, cmap="gray")
