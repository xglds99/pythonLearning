import torch
import cv2
from torchvision import transforms
import numpy as np
from resnet18 import get_net
import torch as d2l


DEVICE = d2l.try_gpu()  # 使用GPU计算
PARAMS_PATH = 'face_SGD_224_resnet18-3.params'  # 网络参数


def face_detect(img_file, device=DEVICE):
    gpu()
    net = get_net()
    net.load_state_dict(torch.load(PARAMS_PATH))
    net.to(device)
    scales = []  # 缩放变换比例
    factor = 0.79
    img = cv2.imread(img_file)
    largest = min(2, 4000 / max(img.shape[0:2]))
    scale = largest
    mind = largest * min(img.shape[0:2])
    while mind >= 224:
        scales.append(scale)
        scale *= factor
        mind *= factor

    total_box = []
    for scale in scales:
        scale_img = cv2.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))
        for box_img, box_pos in box_move(scale_img):
            box_img = trans_form(box_img)
            box_img = box_img.to(device)
            prob = torch.softmax(net(box_img), dim=1)[0][0].data
            if prob > 0.92:
                x0, y0, x1, y1 = box_pos
                x0 = int(x0 / scale)
                y0 = int(y0 / scale)
                x1 = int(x1 / scale)
                y1 = int(y1 / scale)
                total_box.append([x0, y0, x1, y1, prob])
    total_box = nms(total_box)
    for box in total_box:
        x0, y0, x1, y1, prob = box
        cv2.rectangle(img, (x0, y0), (x1, y1), (0, 255, 0), 2)
        cv2.putText(img, str(prob.item()), (x0, y0), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imwrite('detect.png', img)
    return 0


def box_move(img, row_stride=16, col_stride=16):
    """窗口滑动"""
    h, w = img.shape[0:2]
    cellsize = 224
    row = int((w - cellsize) / row_stride) + 1
    col = int((h - cellsize) / col_stride) + 1
    for i in range(col):
        for j in range(row):
            box_pos = (j*row_stride, i*col_stride, j*row_stride+cellsize, i*col_stride+cellsize)
            box_img = img[i*col_stride:i*col_stride+cellsize, j*row_stride:j*row_stride+cellsize]
            yield box_img, box_pos


def trans_form(img):
    transform = transforms.Compose([transforms.ToPILImage(),
                                    transforms.Resize((224, 224)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
                                    ])
    img = transform(img)
    img = img.unsqueeze(0)
    return img


def nms(bounding_boxes, Nt=0.70):
    """非极大值抑制"""
    if len(bounding_boxes) == 0:
        return []
    bboxes = np.array(bounding_boxes)
    # 计算 n 个候选框的面积大小
    x1 = bboxes[:, 0]
    y1 = bboxes[:, 1]
    x2 = bboxes[:, 2]
    y2 = bboxes[:, 3]
    scores = bboxes[:, 4]
    areas = (x2 - x1) * (y2 - y1)
    # 对置信度进行排序, 获取排序后的下标序号, argsort 默认从小到大排序
    order = np.argsort(scores)
    picked_boxes = []  # 返回值
    while order.size > 0:
        # 将当前置信度最大的框加入返回值列表中
        index = order[-1]
        picked_boxes.append(bounding_boxes[index])
        # 获取当前置信度最大的候选框与其他任意候选框的相交面积
        x11 = np.maximum(x1[index], x1[order[:-1]])
        y11 = np.maximum(y1[index], y1[order[:-1]])
        x22 = np.minimum(x2[index], x2[order[:-1]])
        y22 = np.minimum(y2[index], y2[order[:-1]])
        w = np.maximum(0.0, x22 - x11)
        h = np.maximum(0.0, y22 - y11)
        intersection = w * h
        # 利用相交的面积和两个框自身的面积计算框的交并比, 将交并比大于阈值的框删除
        ious = intersection / np.minimum(areas[index], areas[order[:-1]])
        left = np.where(ious < Nt)
        order = order[left]
    return picked_boxes


def gpu():
    """GPU预热"""
    x = torch.randn(size=(100, 100), device=DEVICE)
    for i in range(10):
        torch.mm(x, x)


if __name__ == '__main__':
    face_detect('wx.jpg')
