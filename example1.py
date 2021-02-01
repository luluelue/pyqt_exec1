# coding=utf-8

'''
安装：
pip install PyQt5
pip install PyQt5-tools

qtdesigner设置：
E:\py_code\pyqt\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
$FileName$
$ProjectFileDir$

qtuic设置：
E:\py_code\pyqt\Scripts\python.exe  # 这个python地址必须是环境内的python地址
E:\py_code\pyqt\Scripts\pyuic5.exe $FileName$ -o $FileNameWithoutExtension$.py    # 配置pyuic的配置
$ProjectFileDir$
'''



# pyinstaller -F -i bb.ico example1.py -n pyqtexample --noconsole
# pip install pyqt5 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QMutex
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QToolTip, QMessageBox, QWidget, QApplication
from test1 import Ui_Form
import sys
import time


g_Lock1 = QMutex()  # 线程锁1

# 界面对象
class MyWidget1(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.m_Loding = None  # loding界面

    def initUI(self):
        self.setWindowIcon(QIcon('bb.ico'))  # 增加icon图标，如果没有图片可以没有这句
        self.m_ui = Ui_Form()
        self.m_ui.setupUi(self)
        self.m_ui.m_ButtonTrue.clicked.connect(self.button_true)
        self.m_ui.m_ButtonFalse.clicked.connect(self.button_false)
        self.m_ui.m_Button1.clicked.connect(self.button_1)
        self.m_ui.m_Button2.clicked.connect(self.button_2)
        self.m_ui.m_Button3.clicked.connect(self.button_3)
        self.m_ui.m_Button4.clicked.connect(self.button_4)
        self.show()

    # 确认按钮回调事件
    def button_true(self):
        print("确认按钮触发")
        widget = QtWidgets.QWidget()
        userName = self.m_ui.m_UserName.text()
        pwd = self.m_ui.m_Pwd.text()
        print("用户名：{}，，密码：{}".format(userName, pwd))
        reply = QMessageBox.about(widget, '关于', '这是一个提示框')
        widget.close()

    def button_false(self):
        print("确认按钮触发")
        widget = QtWidgets.QWidget()
        reply = QMessageBox.warning(widget, "警告框", "真的要取消吗",
                                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        widget.close()

    def button_1(self):
        print("确认按钮触发")

        # 使用多线程解决界面卡顿问题
        class thread_test(QThread):
            def __init__(self):
                super().__init__()
            def run(self):
                g_Lock1.lock()  # 加锁，防止执行多次
                for i in range(20):
                    print(i)
                    time.sleep(0.5)  # 休眠
                g_Lock1.unlock()
        t = thread_test()
        t.start()

        widget = QtWidgets.QWidget()
        reply = QMessageBox.question(widget, '询问框', '这是一个询问消息对话框，默认是No',
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        widget.close()

    def button_2(self):
        print("确认按钮触发")
        widget = QtWidgets.QWidget()
        reply = QMessageBox.critical(widget, "错误框", "这是一个提示",
                                     QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore, QMessageBox.Retry)
        widget.close()

    def button_3(self):
        print("确认按钮触发")
        widget = QtWidgets.QWidget()
        reply = QMessageBox.information(widget, "提示框", "这是一个提示", QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        widget.close()

    def button_4(self):
        print("确认按钮触发")
        widget = QtWidgets.QWidget()
        reply = QMessageBox.information(widget, "提示框", "这是一个提示")
        widget.close()

    def loding(self):
        self.m_Loding = QLabel()
        self.m_Loding.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 无边框
        self.m_Loding.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 背景透明
        # 打开gif文件
        movie = QtGui.QMovie("loding.gif")
        # 设置cacheMode为CacheAll时表示gif无限循环，注意此时loopCount()返回-1
        movie.setCacheMode(QtGui.QMovie.CacheAll)
        # 播放速度
        movie.setSpeed(100)
        self.m_Loding.setMovie(movie)
        # 开始播放，对应的是movie.start()
        movie.start()
        self.m_Loding.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyWidget1()
    ui.loding()
    sys.exit(app.exec_())




