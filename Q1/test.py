

import cv2
import os


def getyichang():
    #存放模板图片的地址
    #image1=cv2.imread('./images/dy.mp4/xjtlu.jpg')
    # 存放对比图片的地址
   #images_src_path = './images/'
    # 存放异常图片的地址
    #images_save_path = './yichang'
    # 返回images_src_path路径下包含的文件或文件夹名字的列表（所有图片的文件名），按字母顺序排序
    images = os.listdir(images_src_path)

    for each_image in images:
       # cv2.imread(images_src_path)
        # 获取每个图片的名称
        each_image_name, _ = each_image.split('.')
        # 创建目录，来保存图片帧
        print(os.path.exists(images_save_path))
        if os.path.exists(images_save_path + '/' + each_image_name):
            print("目录已存在")
        else:
            os.mkdir(images_save_path + '/' + each_image_name)
            print("目录创建完毕")


        # 获取保存异常图片的完整路径，每个异常图片存在以异常名为文件名的文件夹中
        each_image_save_full_path = os.path.join(images_save_path, each_image_name) + '/'
        # 获取每个图片的完整路径
        each_image_full_path = os.path.join(images_src_path, each_image)
        # 读取图片
        img2= cv2.imread(each_image_full_path)
        n = classify_hist_with_split(image1, img2)
        frame_count = 0
        success = True
        while (success==True):
            # 提取视频帧，success为是否成功获取视频帧（true/false），第二个返回值为返回的视频帧
            #success, frame = each_image.read()
            #if success == True:
                # 存储异常帧
                if (n<=0.95):
                    cv2.imwrite(each_image_save_full_path + "yichang" +"%06d.jpg" % frame_count,img2)
                frame_count = frame_count + 1


# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


if __name__=="__main__":
    image1 = cv2.imread('./images/dy.mp4/1.jpg')
    images_src_path = './images/dy.mp4'
    images_save_path = './yichang'
    getyichang()