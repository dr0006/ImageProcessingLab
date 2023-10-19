# -*- coding: utf-8 -*-
"""
@File  : 二值化.py
@author: FxDr
@Time  : 2023/10/18 19:26
@Description:  threshold()
"""
import cv2

img = cv2.imread("../../images/back.jpg")

# 缩放
img_resize = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# 灰度化图像
gray_img1 = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
# 二值化
_, binary_img1 = cv2.threshold(gray_img1, 120, 255, cv2.THRESH_BINARY)
#
_, binary_img2 = cv2.threshold(gray_img1, 120, 255, cv2.THRESH_BINARY_INV)
#
_, binary_img3 = cv2.threshold(gray_img1, 120, 255, cv2.THRESH_TRUNC)
#
_, binary_img4 = cv2.threshold(gray_img1, 120, 255, cv2.THRESH_TOZERO)
# 显示图像
cv2.imshow("binary_img1", binary_img1)
cv2.waitKey(0)
cv2.imshow("binary_img2", binary_img2)
cv2.waitKey(0)
cv2.imshow("binary_img3", binary_img3)
cv2.waitKey(0)
cv2.imshow("binary_img4", binary_img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
