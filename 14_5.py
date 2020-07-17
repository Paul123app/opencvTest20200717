import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('test_carNumber.jpg')
rows, cols, ch = img.shape

# 设置标记点和目标点
markpoint = [[228, 173], [311, 172], [233, 210], [315, 208]]
dstpoint = [[0, 0], [780, 0], [0, 352], [780, 352]]

# 强调标记点
for i in markpoint:
    cv2.circle(img, tuple(i), 5, (0, 255, 0), -1)

# 转换点的格式
pts1 = np.float32(markpoint)
pts2 = np.float32(dstpoint)

# 生成透视矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)

# 转换
dst = cv2.warpPerspective(img, M, (780, 352))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
