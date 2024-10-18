import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def blend(image1,op1,image2,op2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    imgBlend = (img1 * op1) + (img2 * op2)
    imgBlend = np.clip(imgBlend,0,255)
    return imgBlend.astype(np.uint8)

img1 = img.imread("C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Tugas4_PCD_MirzaYusuf\\picture\\download.jpg")
img2 = img.imread("C:\\Users\\DELL\\Documents\\Mrzz\\Pengolahan citra\\Tugas4_PCD_MirzaYusuf\\picture\\images.jpg")

imgBlend = blend(img1,0.3,img2,0.7)

img1Hist,bins = np.histogram(img1.flatten(),bins=256,range=[0,256])
img2Hist,bins = np.histogram(img2.flatten(),bins=256,range=[0,256])
imgBlendHist,bins = np.histogram(imgBlend.flatten(),bins=256,range=[0,256])

plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,2)
plt.plot(img1Hist,color="blue")

plt.subplot(3,2,3)
plt.imshow(img2)

plt.subplot(3,2,4)
plt.plot(img2Hist,color="Red")

plt.subplot(3,2,5)
plt.imshow(imgBlend)

plt.subplot(3,2,6)
plt.plot(imgBlendHist,color = "black")

plt.tight_layout
plt.show()