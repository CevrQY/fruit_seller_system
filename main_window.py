from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QAbstractItemView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1620, 970)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.topay_button = QtWidgets.QPushButton(self.centralwidget)
        self.topay_button.setGeometry(QtCore.QRect(980, 740, 601, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.topay_button.setFont(font)
        self.topay_button.setObjectName("pushButton")

        self.drawback_button = QtWidgets.QPushButton(self.centralwidget)
        self.drawback_button.setGeometry(QtCore.QRect(980, 800, 295, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.drawback_button.setFont(font)
        self.drawback_button.setObjectName("pushButton_2")

        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(1285, 800, 295, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("pushButton_2")

        self.payment_button = QtWidgets.QPushButton(self.centralwidget)
        self.payment_button.setGeometry(QtCore.QRect(980, 860, 601, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.payment_button.setFont(font)
        self.payment_button.setObjectName("pushButton_3")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 930, 901))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        self.paylist_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.paylist_label.setFont(font)
        self.paylist_label.setObjectName("label_5")
        self.verticalLayout.addWidget(self.paylist_label)

        self.purchaseTable = QtWidgets.QTableWidget(10, 8)
        self.purchaseTable.setObjectName("tableWidget")
        self.purchaseTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalLayout.addWidget(self.purchaseTable)

        self.total_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.total_label.setFont(font)
        self.total_label.setObjectName("label")
        self.verticalLayout.addWidget(self.total_label)

        self.discount_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.discount_label.setFont(font)
        self.discount_label.setObjectName("label_7")
        self.verticalLayout.addWidget(self.discount_label)

        self.payment_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.payment_label.setFont(font)
        self.payment_label.setObjectName("label_6")
        self.verticalLayout.addWidget(self.payment_label)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(980, 10, 601, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.class_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.class_label.setFont(font)
        self.class_label.setObjectName("label_3")

        self.verticalLayout_3.addWidget(self.class_label)
        self.freshness_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.freshness_label.setFont(font)
        self.freshness_label.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.freshness_label)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(980, 120, 601, 601))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.camera_area = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.camera_area.setFont(font)
        self.camera_area.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.camera_area)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1463, 26))
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.detect_settings = QtWidgets.QAction(MainWindow)
        self.fruit_settings = QtWidgets.QAction(MainWindow)
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.fruit_settings = QtWidgets.QAction(MainWindow)
        self.action = QtWidgets.QAction(MainWindow)
        self.action_4 = QtWidgets.QAction(MainWindow)

        self.menu.addAction(self.detect_settings)
        self.menu.addAction(self.fruit_settings)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_action)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "水果质量检测与自动贩卖系统"))
        self.paylist_label.setText(_translate("MainWindow", "当前待付商品列表："))

        self.class_label.setText(_translate("MainWindow", "检测水果种类："))
        self.freshness_label.setText(_translate("MainWindow", "是否新鲜："))
        self.camera_area.setText(_translate("MainWindow", "正在打开摄像头……"))
        self.topay_button.setText(_translate("MainWindow", "添加到待付列表"))
        self.drawback_button.setText(_translate("MainWindow", "撤回上一步操作"))
        self.reset_button.setText(_translate("MainWindow", "付款信息重置"))
        self.payment_button.setText(_translate("MainWindow", "结账"))

        self.menu.setTitle(_translate("MainWindow", "系统菜单"))
        self.detect_settings.setText(_translate("MainWindow", "水果检测设置"))
        self.fruit_settings.setText(_translate("MainWindow", "商品信息设置"))
        self.exit_action.setText(_translate("MainWindow", "退出系统"))

        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.fruit_settings.setText(_translate("MainWindow", "水果定价设置"))
        self.action.setText(_translate("MainWindow", "教程"))
        self.action_4.setText(_translate("MainWindow", "关于"))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)


class TestWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = TestWindow()
    window.show()
    app.exec_()