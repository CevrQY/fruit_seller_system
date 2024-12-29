import random
import pytest
import torch
from PyQt5 import QtWidgets

import detect
from Main import Main_Function


def generate_detections():
    """生成一些随机的检测数据"""
    fruits_list = ['苹果', '香蕉', '番石榴', '柠檬', '橙子', '石榴']  # 六种水果类型
    # 随机的检测结果
    x, y, w, h, conf = [random.uniform(0, 1) for i in range(5)]  # 随意指定检测目标的出现位置
    cls = random.randint(0, 5)              # 检测目标水果类型
    target_num = random.randint(1, 10)      # 检测目标水果数量
    freshness = [random.choice([0, 1]) for i in range(target_num)]  # 随意指定新鲜度
    detection = [torch.tensor([[x, y, w, h, conf, cls * 2 + freshness[i]] for i in range(target_num)],
                              device=torch.device('cuda:0'))]  # 生成输入数据
    expected = ("检测水果种类：{}".format(fruits_list[cls]),
                "检测水果新鲜度：优质{}，劣质{}".format(freshness.count(0), freshness.count(1)))  # 预期结果
    return detection, expected


@pytest.mark.parametrize("detection, expected", [generate_detections() for i in range(50)])
def test_01(detection, expected):
    """随机检测目标"""
    app = QtWidgets.QApplication([])
    window = Main_Function()
    detect.show_detection_result(window, detection)
    assert window.class_label.text() == expected[0]
    assert window.freshness_label.text() == expected[1]


def test_02():
    """无检测目标"""
    app = QtWidgets.QApplication([])
    window = Main_Function()
    detection, expected = [torch.tensor([], device=torch.device('cuda:0'))], ("检测水果种类：未检测到水果", "检测水果新鲜度：无")
    detect.show_detection_result(window, detection)
    assert window.class_label.text() == expected[0]
    assert window.freshness_label.text() == expected[1]


if __name__ == "__main__":
    pytest.main()
