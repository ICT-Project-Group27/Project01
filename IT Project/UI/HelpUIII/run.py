# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Help


class pages_window(Help.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(pages_window, self).__init__()
        self.setupUi(self)
        # 设置信号与槽
        # 点击左侧按钮页面1切换到第一个页面
        self.pushButton.clicked.connect(self.display_page1)
        # 点击左侧按钮页面2切换到第二个页面
        self.pushButton_2.clicked.connect(self.display_page2)
        # 点击左侧按钮页面3切换到第三个页面
        self.pushButton_3.clicked.connect(self.display_page3)
        # 点击左侧按钮页面4切换到第四个页面
        self.pushButton_4.clicked.connect(self.display_page4)

        self.stackedWidget.setCurrentIndex(0)


    def display_page1(self):
       self.stackedWidget.setCurrentIndex(3)

    def display_page2(self):
       self.stackedWidget.setCurrentIndex(0)

    def display_page3(self):
       self.stackedWidget.setCurrentIndex(1)

    def display_page4(self):
       self.stackedWidget.setCurrentIndex(2)


if __name__ == "__main__":
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        # 为main_window类和login_window类创建对象
        main_window = pages_window()
        # 显示窗口
        main_window.show()
        # 关闭程序，释放资源
        sys.exit(app.exec_())