import cv2
import numpy as np
from matplotlib import pyplot as plt #digunakan untuk meplot histogram dan ditampilkan dalam jendela
 
img = cv2.imread('Muslim.jpg')#membaca file gambar yang akan dilakukan proses filter nantinya.
 
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)#filter2D saya gunakan sebagai filter hightpass untuk gambar.
  #menampilkan histogram dari hasil gambar
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('hpf')
plt.xticks([]), plt.yticks([])
plt.show()