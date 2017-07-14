import cv2
import numpy as np
from matplotlib import pyplot as plt #digunakan untuk meplot histogram dan ditampilkan dalam jendela
 
img = cv2.imread('Muslim.jpg',0) #membaca file gambar yang akan dilakukan proses filter nantinya
 
hist,bins = np.histogram(img.flatten(),256,[0,256])# melakukan proses histogram equalition guna meningkatkan kecerahan gambar
 
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

cv2.imshow('image',img2)#menampilkan hasil gambar dari proses equalition.
#menampilkan histogram dari hasil gambar
plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()