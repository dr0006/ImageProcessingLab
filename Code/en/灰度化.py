# -*- coding: utf-8 -*-
"""
@File  : 灰度化.py
@author: FxDr
@Time  : 2023/10/18 19:18
@Description:
"""
import cv2

img = cv2.imread("../../images/back.jpg")
# 缩放
img_resize = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# 灰度化
gray_img = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
# 显示
cv2.imshow("gray_img", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
