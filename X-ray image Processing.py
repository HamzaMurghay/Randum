import cv2
import matplotlib.pyplot as plt

image = cv2.imread('../../Downloads/chest xray.jpeg', cv2.IMREAD_GRAYSCALE)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
enhanced = clahe.apply(image)

blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)

edges = cv2.Canny(blurred, 50, 120)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)), plt.title('Canny Edge Detection')
plt.tight_layout()
plt.show()
