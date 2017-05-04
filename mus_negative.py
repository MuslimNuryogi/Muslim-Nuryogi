import numpy as np
import cv2

mus = cv2.VideoCapture(0) #perintah untuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada notebook.
print(mus.isOpened())

while(True): #perintahuntuk looping imshow (looping menampilkan objek melalui webcam), sehingga webcam akan mengambil objek gambar secara realtime.
    ret, frame = mus.read() #perintah untuk mengambil objek gambar dengan format berwarna atau BGR.
    grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #perintah untuk mengubah objek gambar yang awalnya berwarna (BGR) menjadi grayscale sebelum diubah menjadi gambar negatif.
    cv2.imshow('negatif', 255-grey) #perintah untuk mengubah obyek gambar dari skala keabuan menjadi gambar dengan skala negatif. 
    if cv2.waitKey(1) & 0xFF == ord('c'): #perintah  untuk menghentikan program dengan menekan tombol c pada keyboard notebook.
        break

mus.realease()
cv2.destroyAllwindows()