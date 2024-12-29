import json
import os

from module.detect_settings import Detect_Settings_Window
from module.fruit_settings import Fruit_Settings_Window


class Settings:
    def __init__(self):
        # 模型参数设置
        self.cam_source = '0'       # 摄像头源，可选择电脑摄像头(0,1,2,...)
        self.max_fps = 100          # 每秒最多检测帧数
        self.min_conf = 0.5         # 最小检测可信度
        self.use_gpu = ''           # 启用GPU加速，允许的取值为''(自动),'0'(启用GPU0),'cpu'('始终使用CPU')

        # 水果信息设置
        self.unit_count = ['元/斤', '元/公斤（千克）', '元/个']                    # 计量单位
        self.fruits_list = ['苹果', '香蕉', '番石榴', '柠檬', '橙子', '石榴']        # 水果名
        self.fruits_price = {fruit: 5.0 for fruit in self.fruits_list}          # 水果单价
        self.fruits_unit = {fruit: 2 for fruit in self.fruits_list}             # 水果单价计量单位
        self.fruits_discount = {fruit: 1.0 for fruit in self.fruits_list}       # 水果折扣价格，无折扣为1.0

        # 如果有，读入上次保存的设置
        if os.path.exists('settings.json'):
            self.load_settings()

        # 记录
        self.fruits_attr_dict = {attr: getattr(self, attr) for attr in dir(self)
                                 if attr.startswith("fruits")}
        self.detect_attr_dict = {attr: getattr(self, attr) for attr in dir(self)
                                 if attr in ['cam_source', 'max_fps', 'min_conf', 'use_gpu']}

        self.fruit_settings_window = Fruit_Settings_Window(self.fruits_attr_dict)
        self.detect_settings_window = Detect_Settings_Window(self.detect_attr_dict)

    def show_detect_settings_window(self):
        try:
            self.detect_settings_window.show_detect_settings_window()
        except Exception as e:
            print(e)

    def show_fruit_settings_window(self):
        try:
            self.fruit_settings_window.show_fruit_settings_window()
        except Exception as e:
            print(e)

    def update_fruit_settings(self):
        self.fruits_price = {fruit: float(self.fruit_settings_window.fruit_price_text[i].toPlainText())
                             for i, fruit in enumerate(self.fruits_list)}
        self.fruits_unit = {fruit: self.fruit_settings_window.button_groups[i].checkedId()
                            for i, fruit in enumerate(self.fruits_list)}
        self.fruits_discount = {fruit: self.fruit_settings_window.discount_boxes[i].value()
                                for i, fruit in enumerate(self.fruits_list)}
        self.fruits_attr_dict = {attr: getattr(self, attr) for attr in dir(self)
                                 if attr.startswith("fruits")}

    def update_detect_settings(self):
        det_window = self.detect_settings_window
        self.cam_source = det_window.source_text.toPlainText()
        self.max_fps = int(det_window.max_fps_box.value())
        self.min_conf = det_window.conf_box.value()
        self.use_gpu = det_window.device_type[det_window.device_group.checkedId()]
        self.detect_attr_dict = {attr: getattr(self, attr) for attr in dir(self)
                                 if attr in ['cam_source', 'max_fps', 'min_conf', 'use_gpu']}
        print(self.detect_attr_dict)

    def save_settings(self):
        """保存设置"""
        det_settings = {
            'cam_source': self.cam_source,
            'max_fps': self.max_fps,
            'min_conf': self.min_conf,
            'use_gpu': self.use_gpu + 'g'
        }
        settings = [
            det_settings,
            self.fruits_price,
            self.fruits_unit,
            self.fruits_discount
        ]
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)

    def load_settings(self):
        """加载设置"""
        with open('settings.json', 'r', encoding='utf-8') as f:
            settings = json.load(f)

            # 传入参数时，将类的同名变量设置为该键对应的值
            detect_opts = settings[0]
            for opt_name in detect_opts.keys():
                if opt_name == 'use_gpu':
                    setattr(self, opt_name, detect_opts[opt_name][:-1])
                else:
                    setattr(self, opt_name, detect_opts[opt_name])

            self.fruits_price = settings[1]
            self.fruits_unit = settings[2]
            self.fruits_discount = settings[3]
