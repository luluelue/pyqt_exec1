# coding=utf-8


'''
安装：
pip install PyQt5
pip install PyQt5-tools

qtdesigner设置：
G:\py_project\pyqt_exec1\venv\Lib\site-packages\PySide2\designer.exe
$FileName$
$ProjectFileDir$

qtuic设置：
E:\py_code\pyqt\Scripts\python.exe  # 这个python地址必须是环境内的python地址
E:\py_code\pyqt\Scripts\pyuic5.exe $FileName$ -o $FileNameWithoutExtension$.py    # 配置pyuic的配置
$ProjectFileDir$
'''

# pyinstaller -F -i bb.ico example1.py -n pyqtexample --noconsole
# pip install PySide2 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow, QPlainTextEdit, QPushButton, QLabel


class StatisticUI():
    def __init__(self):
        app = QApplication([])

        self.window = QMainWindow()
        window = self.window
        window.resize(500, 400)
        window.move(500, 500)
        window.setWindowTitle("pyside2测试")

        textEdit = QPlainTextEdit(window)
        textEdit.setPlaceholderText("请输入内容")
        textEdit.move(10, 25)
        textEdit.resize(300, 300)

        button = QPushButton("统计", window)
        button.move(380, 80)
        button.clicked.connect(lambda: self.button1CB(window, textEdit))
        # button.clicked.connect(self.loding)

        window.show()
        app.exec_()

    # 统计按钮的回调函数
    def button1CB(self, window, textEdit):
        QMessageBox.information(window, "统计结果", textEdit.toPlainText())

    def loding(self):
        self.m_Loding = QLabel(self.window)
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


if __name__ == '__main__':
    StatisticUI()
