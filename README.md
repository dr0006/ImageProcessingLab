# ImageProcessingLab

图像处理课程的学习，主要用到OpenCV处理图像

---

## 目录

1. [OpenCV的安装](#安装)
2. [熟悉和了解](#熟悉和了解)
3. [绘图功能](#绘图)
4. [基操](#基操)
5. [运算](#运算)

## OpenCV

目录

### 安装

```bash
pip3 install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
#Successfully installed numpy-1.24.4 opencv-python-4.8.1.78
```

---

### 熟悉和了解

`Code:` [ipynb](./Code/熟悉和了解.ipynb)

- 主要是图片的读取等操作，还有写入和摄像头调用及显示
- 视频文件的读取以及显示
- 里面写了一个等比例缩放的函数，因为有些图片太大不好显示

---

### 绘图

`Code:` [ipynb](./Code/绘图功能.ipynb)

- 举个简单的应用，比如说车牌识别，当你识别出结果后你就可以绘制到图片上
- cv.line()，cv.circle()，cv.rectangle()，cv.ellipse()，cv.putText()等
- 当你试图用putText绘制中文，出来的都是？？？？？
- 绘制中文 [ChineseText.py](./Code/ChineseText.py)

![img_1](./md/img_1.png)

### 基操

`Code` [ipynb](./Code/基操.ipynb)

- 访问像素值并修改它们
- 访问图像属性
- 设置感兴趣区域(ROI)
- 分割合并

![img_1](./md/img.png)

### 运算

`Code`[ipynb](./Code/运算.ipynb)

- 学习图像的几种算术运算，例如加法，减法，按位运算等

