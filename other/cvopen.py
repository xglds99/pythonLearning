# coding=gbk
"""
作者：川川
@时间  : 2021/9/5 16:38
https://github.com/opencv/opencv/tree/master/data/haarcascades
"""
import cv2

# 待检测的图片路径
imagepath="2.jpg"

image = cv2.imread(imagepath)#读取图片
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#图像转换为灰度图：

face_cascade = cv2.CascadeClassifier(r'./forntface.xml')#加载使用人脸识别器

faces = face_cascade.detectMultiScale(gray)#检测图像中的所有面孔

#为每个人脸绘制一个蓝色矩形
for x, y, width, height in faces:
	# 这里的color是 蓝 黄 红，与rgb相反，thickness设置宽度
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

# 最后，让我们保存新图像
cv2.imwrite("beauty_detected.jpg", image)
