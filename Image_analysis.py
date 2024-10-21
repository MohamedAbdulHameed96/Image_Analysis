
# import cv2
import matplotlib.pyplot as plt
%matplotlib inline

img_path = 'pandas.jpg'
# Load color image 
bgr_img = cv2.imread(img_path)
# Convert to grayscale
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
# Normalize, rescale entries to lie in [0,1]
gray_img = gray_img.astype("float32")/255
# Plot image
plt.imshow(gray_img, cmap='gray')
plt.show()

 
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

img_path = 'pandas.jpg'

 
bgr_img = cv2.imread(img_path)

 
print(bgr_img.shape)

 
print(bgr_img.size)

 
print(bgr_img.dtype)

 
plt.imshow(bgr_img)

 
crop = bgr_img[0:500,200:800]

 
plt.imshow(crop)

 
gray_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

 
plt.imshow(gray_img)

 
print(gray_img)

 
# Normalize, rescale entries to lie in [0,1]
gray_img = gray_img.astype("float32")/255

 
# Plot image
plt.imshow(gray_img, cmap='gray')
plt.show()

 



