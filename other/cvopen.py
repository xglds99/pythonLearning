# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/9/5 16:38
https://github.com/opencv/opencv/tree/master/data/haarcascades
"""
import cv2

# ������ͼƬ·��
imagepath="2.jpg"

image = cv2.imread(imagepath)#��ȡͼƬ
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#ͼ��ת��Ϊ�Ҷ�ͼ��

face_cascade = cv2.CascadeClassifier(r'./forntface.xml')#����ʹ������ʶ����

faces = face_cascade.detectMultiScale(gray)#���ͼ���е��������

#Ϊÿ����������һ����ɫ����
for x, y, width, height in faces:
	# �����color�� �� �� �죬��rgb�෴��thickness���ÿ��
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

# ��������Ǳ�����ͼ��
cv2.imwrite("beauty_detected.jpg", image)
