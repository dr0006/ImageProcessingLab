# -*- coding: utf-8 -*-
"""
@File  : show_pic_resize.py
@author: FxDr
@Time  : 2023/10/04 19:03
@Description:
"""
import cv2


# 等比例缩放显示
def show_frame(frame):
    # 获取图像的宽度和高度
    height, width = frame.shape[:2]

    # 设置希望的缩放宽度
    desired_width = 400

    # 计算缩放比例，确保等比例缩放
    scale_factor = desired_width / width

    # 计算缩放后的新高度
    desired_height = int(height * scale_factor)

    # 缩放图像
    resized_image = cv2.resize(frame, (desired_width, desired_height))
    return resized_image