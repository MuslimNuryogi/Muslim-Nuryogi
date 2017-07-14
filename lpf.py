import cv2
import numpy as np
from matplotlib import pyplot as plt #digunakan untuk meplot histogram dan ditampilkan dalam jendela

img = cv2.imread('Muslim.jpg')#membaca file gambar yang akan dilakukan proses filter nantinya

blur = cv2.blur(img,(5,5))#perintah blurr ini saya gunakan untuk memfilter gambar agar di dapat hasil filter low..pada gambar.
 #menampilkan histogram dari hasil gambar
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('lpf')
plt.xticks([]), plt.yticks([])
plt.show()