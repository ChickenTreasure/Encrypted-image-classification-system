import cv2
import matplotlib.pyplot as plt
import numpy as np

# 读取两张图片
img1 = cv2.imread('../dataset/train_AES/encrypted0_0.png', cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取图片
img2 = cv2.imread('../dataset/train_AES/encrypted0_1.png', cv2.IMREAD_GRAYSCALE)

# 计算两张图片的直方图
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

# 归一化直方图以便更好地比较
hist1 = hist1.ravel() / hist1.max()
hist2 = hist2.ravel() / hist2.max()

# 绘制直方图
plt.figure(figsize=(12, 6))

# 绘制第一张图片的直方图
plt.subplot(1, 2, 1)
plt.plot(hist1, color='r')
plt.title('Number 0')
plt.xlabel('Pixel Value')
plt.ylabel('Normalized Frequency')

# 绘制第二张图片的直方图
plt.subplot(1, 2, 2)
plt.plot(hist2, color='b')
plt.title('Number 0(png_2)')
plt.xlabel('Pixel Value')
plt.ylabel('Normalized Frequency')

# 显示直方图
plt.tight_layout()
plt.show()

# 计算直方图交集并展示结果（可选）
intersection = np.minimum(hist1, hist2)
difference = np.sum(np.abs(hist1 - hist2))
similarity = np.sum(intersection) / np.sum(hist1 + hist2 - intersection)

print(f"Histogram Difference: {difference}")
print(f"Histogram Similarity: {similarity}")