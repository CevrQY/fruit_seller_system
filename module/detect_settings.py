import torch
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup


class Ui_Dialog(object):
    def setupUi(self, Dialog, detect_opt, device=0):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 457)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.max_fps_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.max_fps_box.setGeometry(QtCore.QRect(250, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.max_fps_box.setFont(font)
        self.max_fps_box.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.max_fps_box.setDecimals(0)
        self.max_fps_box.setMinimum(10.0)
        self.max_fps_box.setMaximum(500.0)
        self.max_fps_box.setObjectName("doubleSpinBox")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.conf_slider = QtWidgets.QSlider(Dialog)
        self.conf_slider.setGeometry(QtCore.QRect(40, 200, 601, 31))
        self.conf_slider.setMinimum(30)
        self.conf_slider.setMaximum(95)
        self.conf_slider.setSingleStep(1)
        self.conf_slider.setValue(int(detect_opt['min_conf'] * 100))
        self.conf_slider.setOrientation(QtCore.Qt.Horizontal)
        self.conf_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.conf_slider.setTickInterval(5)
        self.conf_slider.setObjectName("horizontalSlider")
        self.conf_slider.valueChanged.connect(self.change_spinbox)

        self.conf_box = QtWidgets.QDoubleSpinBox(Dialog)
        self.conf_box.setGeometry(QtCore.QRect(690, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.conf_box.setFont(font)
        self.conf_box.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.conf_box.setDecimals(2)
        self.conf_box.setMinimum(0.3)
        self.conf_box.setMaximum(0.95)
        self.conf_box.setSingleStep(0.01)
        self.conf_box.setValue(detect_opt['min_conf'])
        self.conf_box.setObjectName("doubleSpinBox_2")
        self.conf_box.editingFinished.connect(self.change_slider)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 160, 641, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(170, 20, 561, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 141, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(180, 290, 491, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        if not torch.cuda.is_available():
            self.radioButton_2.setDisabled(True)

        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 370, 281, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")

        self.device_type = ['', '0', 'cpu']
        self.device_group = QButtonGroup(self)
        self.device_group.addButton(self.radioButton, 0)
        self.device_group.addButton(self.radioButton_2, 1)
        self.device_group.addButton(self.radioButton_3, 2)
        button = self.device_group.button(device)
        button.setChecked(True)

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 230, 671, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.source_text = QtWidgets.QPlainTextEdit(Dialog)
        self.source_text.setGeometry(QtCore.QRect(30, 60, 751, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.source_text.setFont(font)
        self.source_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.source_text.setObjectName("plainTextEdit")

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.apply_button = QtWidgets.QPushButton(Dialog)
        self.apply_button.setGeometry(QtCore.QRect(580, 410, 91, 31))
        self.apply_button.setFont(font)
        self.apply_button.setObjectName("pushButton")

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(690, 410, 91, 31))
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.cancel_button.clicked.connect(self.close_window)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "水果检测设置"))
        self.label.setText(_translate("Dialog", "摄像头信号源"))
        self.label_2.setText(_translate("Dialog", "检测速度（次/秒）"))
        self.label_3.setText(_translate("Dialog", "最小置信度"))
        self.label_4.setText(_translate("Dialog", "（判断画面中有水果的可能性，过小可能导致误判，过大可能导致漏判）"))
        self.label_5.setText(_translate("Dialog", "（0,1,2,...为电脑摄像头，默认为0，可输入网络摄像头地址）"))
        self.label_6.setText(_translate("Dialog", "GPU加速检测"))
        self.radioButton.setText(_translate("Dialog", "自动（默认选项，可用GPU检测时优先启用）"))
        self.radioButton_2.setText(_translate("Dialog", "始终启用"))
        self.radioButton_3.setText(_translate("Dialog", "始终禁用（仅使用CPU）"))
        self.label_7.setText(_translate("Dialog",
                                        "0.30      0.40      0.50      0.60      0.70      0.80      0.90  0.95"))
        self.apply_button.setText(_translate("Dialog", "应用"))
        self.cancel_button.setText(_translate("Dialog", "取消"))

    def close_window(self):
        self.close()

    def change_slider(self):
        self.conf_slider.setValue(int(self.conf_box.value() * 100))

    def change_spinbox(self):
        self.conf_box.setValue(self.conf_slider.value() / 100.0)


class Detect_Settings_Window(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, detect_opt):
        super().__init__()
        device = ['', '0', 'cpu'].index(detect_opt['use_gpu'])
        device = device if 0 <= device <= 2 else 0
        self.setupUi(self, detect_opt, device)
        self.source_text.setPlainText(detect_opt['cam_source'])
        self.max_fps_box.setValue(detect_opt['max_fps'])

    def show_detect_settings_window(self):
        self.show()
        self.exec_()
