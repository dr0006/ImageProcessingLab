# -*- coding: utf-8 -*-
"""
@File  : car_plate_location.py
@author: FxDr
@Time  : 2023/10/21 19:50
@Description:
"""
import cv2
import numpy as np

# 读取图像并将其转换为HSV颜色空间
# image = cv2.imread('./images/car3.png')
image = cv2.imread('./images/car4.png')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义蓝色车牌区域的颜色范围
lower_blue = np.array([90, 50, 50])  # 最低蓝色HSV值
upper_blue = np.array([130, 255, 255])  # 最高蓝色HSV值

# 创建一个蓝色掩码，以便只保留蓝色车牌区域
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# 进行形态学操作，如腐蚀和膨胀，以平滑和处理图像中的噪音
# 开运算闭运算。。
kernel = np.ones((5, 5), np.uint8)
blue_mask = cv2.erode(blue_mask, kernel, iterations=1)
blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)

# 查找蓝色车牌区域的轮廓
contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 遍历所有轮廓并找到可能的车牌区域，可以根据面积、形状等特征来筛选
possible_plates = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:  # 根据面积筛选可能的车牌区域
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h
        if 2.5 < aspect_ratio < 4.0:  # 根据宽高比筛选可能的车牌区域
            possible_plates.append((x, y, w, h))

# 在原始图像上绘制边框，表示找到的车牌区域
for (x, y, w, h) in possible_plates:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 显示带有车牌区域边框的图像
cv2.imshow('Blue License Plates', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
