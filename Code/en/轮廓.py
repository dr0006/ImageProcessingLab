# -*- coding: utf-8 -*-
"""
@File  : 轮廓.py
@author: FxDr
@Time  : 2023/10/21 19:08
@Description: OpenCV轮廓findContours和drawContours
    findContoursr()的第二个参数轮廓检索模式是处理可能包含的父子关系
    也就是说一个轮廓里面可能还包含着其他轮廓，有几个选项来进行设置
    RETR_LIST只提取所有的轮廓，而不去创建任何父子关系；
    RETR_EXTERNAL只返回最外边的轮廓，所有的子轮廓都会被忽略；
    RETR_CCOMP会返回所有的轮廓并将轮廓分为两级组织结构；
    RETR_TREE会返回所有轮廓，并且创建一个完整的组织结构列表，它甚至会告诉你谁是爷爷、爸爸、儿子、孙子等。

    findContours()的第三个参数可以有两个设置值，
    设置为CHAIN_APPROX_NONE，表示边界所有点都会被存储；
    设置为CHAIN_APPROX_SIMPLE 会压缩轮廓，将轮廓上的冗余点去掉，比如说四边形就会只存储4个角点。

    查找到轮廓以后，就可以用drawContours()方法把findContours()返回的轮廓列表绘制出来。

    函数drawContours()有5个参数。
    第一个参数是一张图像，可以是原图或者其他；
    第二个参数是轮廓，也可以说是findContours()找出来的点集，一个列表；
    第三个参数是对轮廓（第二个参数）的索引，当需要绘制独立轮廓时很有用，若要全部绘制可设为-1；
    接下来的第四个和第五个参数是轮廓的颜色和厚度。
"""
import cv2

img = cv2.imread("../../images/car.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 160, 200)
cv2.imshow("edge", edge)
cv2.waitKey(0)
# 返回值的第一个元素是轮廓，这个轮廓是一个列表，每个列表元素代表一个轮廓。
cons, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
draw_edge = cv2.drawContours(img, cons, -1, (255, 0, 255), 1)
cv2.imshow("edge", draw_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
