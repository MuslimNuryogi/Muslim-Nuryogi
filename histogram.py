import cv2
import numpy as np
from matplotlib import pyplot as plt #digunakan untuk meplot histogram dan ditampilkan dalam jendela

img = cv2.imread('Muslim.jpg',0)#membaca file gambar yang akan dilakukan proses filter nantinya
cv2.imshow('image',img)
#menampilkan histogram dari hasil gambar
plt.hist(img.ravel(),256,[0,256])
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()