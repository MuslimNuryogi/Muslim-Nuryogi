import numpy as np
import cv2

mus = cv2.VideoCapture(0) #perintah untuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada notebook.
print(mus.isOpened())


while(True): #perintah untuk looping imshow (looping menampilkan objek melalui webcam), sehingga webcam akan mengambil objek gambar secara realtime.
    ret, frame = mus.read() #perintah untuk mengambil objek gambar dengan format berwarna atau BGR.
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 25) #perintah untuk meningkatkan nilai kecerahan objek gambar.
    cv2.imshow('brightness',bright) #perintah untuk menampilkan gambar yang telah diubah nilai kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('c'): #perintah untuk menghentikan program dengan menekan tombol c pada keyboard notebook.
        break

mus.realease()
cv2.destroyAllwindows()
