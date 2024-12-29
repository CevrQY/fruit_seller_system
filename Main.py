import sys
import cv2

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem

import main_window
from fruit import Fruit
from module.camera import Camera
from settings import Settings


class Controller(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    """程序主要功能"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.camera = None

        # 导入保存的系统设置
        self.settings = Settings()
        self.detect_settings.triggered.connect(self.settings.show_detect_settings_window)
        self.fruit_settings.triggered.connect(self.settings.show_fruit_settings_window)

        # 初始化水果、摄像头信息
        self.fruits = {fruit: None for fruit in self.settings.fruits_list}
        self.init_or_reset_fruit_info()

        # 建立按钮按键触发映射
        self.topay_button.clicked.connect(self.add_purchase_info)
        self.drawback_button.clicked.connect(self.draw_back)
        self.reset_button.clicked.connect(self.reset_purchase_info)
        self.payment_button.clicked.connect(self.payment_steps)
        self.exit_action.triggered.connect(self.exit)

        # 水果设置窗口按钮触发映射
        fruit_settings_window = self.settings.fruit_settings_window
        fruit_settings_window.apply_button.clicked.connect(self.apply_fruit_settings)

        # 模型检测设置窗口按钮触发映射
        detect_settings_window = self.settings.detect_settings_window
        detect_settings_window.apply_button.clicked.connect(self.apply_detect_settings)

        if self.camera is None:
            self.camera = Camera(self.settings.detect_attr_dict)

        # 付费信息
        self.info_head = ['水果名称', '新鲜程度（优/劣）', '单价', '单位', '重量', '数量', '折扣', '总价']
        self.info_dtypes = [str, str, float, str, float, int, float, float]
        self.purchase_info = pd.DataFrame({self.info_head[i]: [0] for i in range(len(self.info_head))})  # 存储付费信息
        self.purchase_stack = []  # 购买信息栈，提供撤回步骤
        self.reset_purchase_info()

        # 运行摄像头，使检测画面投射到窗口
        self.show()
        self.camera.run_camera(window=self, stop_event=self.camera.stop_event)

    def init_or_reset_fruit_info(self):
        # 初始化水果对象
        self.fruits = {fruit: Fruit(fruit,
                                    self.settings.fruits_price[fruit],
                                    self.settings.fruits_unit[fruit],
                                    self.settings.fruits_discount[fruit])
                       for fruit in self.settings.fruits_list}

    def apply_fruit_settings(self):
        self.reset_purchase_info()
        self.settings.update_fruit_settings()
        self.init_or_reset_fruit_info()
        self.settings.fruit_settings_window.close_window()

    def apply_detect_settings(self):
        self.settings.update_detect_settings()
        self.settings.detect_settings_window.close_window()
        self.camera.refresh_camera(self, self.settings.detect_attr_dict)

    def display_image(self, image):
        """显示摄像头图像"""
        try:
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换图像通道
            x = img.shape[1]
            y = img.shape[0]
            self.zoomscale = min(810 / x, 810 / y)          # 图片放缩尺度
            frame = QImage(img, x, y, x * 3, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.camera_area.setPixmap(pix)
        except Exception as e:
            print(e)

    def info_empty(self):
        """检测购买信息是否为空"""
        return list(self.purchase_info.loc[0]) == ['0', '0', 0.0, '0', 0.0, 0, 0.0, 0.0]

    def reset_purchase_info(self):
        """重置购买信息"""
        self.purchase_stack.clear()
        self.purchaseTable.clear()
        self.purchaseTable.setHorizontalHeaderLabels(self.info_head)
        self.purchase_info = pd.DataFrame({self.info_head[i]: [0] for i in range(len(self.info_head))})
        for i in range(len(self.info_head)):
            self.purchase_info[self.info_head[i]] = self.purchase_info[self.info_head[i]].astype(self.info_dtypes[i])

        self.total_label.setText("合计：0.00")
        self.discount_label.setText("优惠：-0.00")
        self.payment_label.setText("应付：0.00")

        self.init_or_reset_fruit_info()

    def add_purchase_info(self):
        """添加水果信息"""
        try:
            # 获取检测信息
            cls = self.settings.fruits_list[self.camera.detect_class]
            good_num, bad_num = self.camera.detect_count

            # 修改已检测水果数量
            fruit_count = good_num + bad_num
            self.fruits[cls].count['good'] += good_num
            self.fruits[cls].count['bad'] += bad_num
            weight = self.get_weight(self.settings.fruits_unit[cls])
            actual_payment, discount = self.fruits[cls].get_price(weight=weight, count=fruit_count)

            # 添加到购买信息栈
            self.purchase_stack.append([self.purchase_info.copy(), (cls, good_num, bad_num)])

            if True in list(self.purchase_info['水果名称'].str.contains(cls)):
                self.purchase_info.loc[self.purchase_info['水果名称'] == cls, '新鲜程度（优/劣）'] = (
                    '{}优，{}劣'.format(self.fruits[cls].count['good'], self.fruits[cls].count['bad']))
                self.purchase_info.loc[self.purchase_info['水果名称'] == cls, '重量'] += weight
                self.purchase_info.loc[self.purchase_info['水果名称'] == cls, '数量'] += fruit_count
                self.purchase_info.loc[self.purchase_info['水果名称'] == cls, '折扣'] += discount * -1.0
                self.purchase_info.loc[self.purchase_info['水果名称'] == cls, '总价'] += actual_payment
            else:
                new_row = pd.Series({'水果名称': cls,
                                     '新鲜程度（优/劣）': '{}优，{}劣'.format(self.fruits[cls].count['good'],
                                                                           self.fruits[cls].count['bad']),
                                     '单价': self.settings.fruits_price[cls],
                                     '单位': self.settings.unit_count[self.settings.fruits_unit[cls]],
                                     '重量': self.get_weight(self.settings.fruits_unit[cls]),
                                     '数量': fruit_count,
                                     '折扣': discount * -1.0,
                                     '总价': actual_payment})
                if self.info_empty():
                    self.purchase_info.loc[0] = new_row
                else:
                    self.purchase_info = pd.concat([self.purchase_info, new_row.to_frame().T], ignore_index=True)
            self.update_purchase_info()
        except Exception as e:
            print(e)

    def draw_back(self):
        """撤回上一步操作"""
        if len(self.purchase_stack) > 0:
            last_step = self.purchase_stack.pop()
            self.purchase_info = last_step[0]
            cls, good_num, bad_num = last_step[1]
            self.fruits[cls].count['good'] -= good_num
            self.fruits[cls].count['bad'] -= bad_num
            self.update_purchase_info()

    def update_purchase_info(self):
        """更新购买信息表"""
        self.purchaseTable.clear()
        self.purchaseTable.setHorizontalHeaderLabels(self.info_head)
        if not self.info_empty():
            for i in range(len(self.purchase_info)):
                for j in range(len(self.purchase_info.columns)):
                    col_name = self.purchase_info.columns[j]
                    item = self.purchase_info.loc[i, col_name]
                    if isinstance(item, float):
                        item = str(round(item, 2))
                    item = QTableWidgetItem(str(item))
                    self.purchaseTable.setItem(i, j, item)

        self.discount_label.setText('优惠：{:.2f}'.format(self.purchase_info['折扣'].sum()))
        self.payment_label.setText('应付：{:.2f}'.format(self.purchase_info['总价'].sum()))
        self.total_label.setText(
            '合计：{:.2f}'.format(self.purchase_info['折扣'].sum() * -1.0 + self.purchase_info['总价'].sum()))

    def get_weight(self, unit=0) -> float:
        """
        连接到摄像头，获取水果重量，或直接获取电子秤重量(需要补充)
        unit: 水果单位, 合法输入值：0 - 元/斤, 1 - 元/公斤（千克）
        """
        return 0.0

    def payment_steps(self):
        """支付步骤(待补充，可接入微信、支付宝等第三方支付接口)"""
        self.reset_purchase_info()  # 支付成功后，重置待付商品信息

    def exit(self):
        """退出系统操作"""
        self.camera.camera_open = False
        self.settings.save_settings()
        sys.exit(0)

    def closeEvent(self, event):
        """关闭窗口时执行"""
        self.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Controller()
    app.exec_()
