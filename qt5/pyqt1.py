#coding=utf-8
from PyQt5 import QtCore, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys

class Qlabel1():
    def __init__(self):
        _translate = QtCore.QCoreApplication.translate

        app = QApplication([])
        label = QLabel('Hello World!')
        label.resize(300,300)
        label.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 无边框
        label.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 背景透明

        self.m_Label1 = QLabel()
        self.m_Label1.setGeometry(QtCore.QRect(200, 350, 241, 131))
        font = QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.m_Label1.setFont(font)
        self.m_Label1.setTextFormat(QtCore.Qt.PlainText)
        self.m_Label1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.m_Label1.setObjectName("m_Label1")
        self.m_Label1.setText(_translate("Form", "TextLabel"))

        label.show()
        self.m_Label1.show()

        app.exec_()


class QLabelExample(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lb1 = QLabel('学点编程吧，我爱你~！', self)
        self.lb2 = QLabel('我内容很少哦...', self)
        self.lb3 = QLabel('我内容很少哦...', self)
        self.lb3.setWordWrap(True)

        self.bt1 = QPushButton('输入内容1', self)
        self.bt2 = QPushButton('输入内容2', self)

        self.ra1 = QRadioButton('左边', self)
        self.ra2 = QRadioButton('中间', self)
        self.ra3 = QRadioButton('右边', self)

        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.ra1, 1)
        self.bg1.addButton(self.ra2, 2)
        self.bg1.addButton(self.ra3, 3)

        self.show()

        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)

    def rbclicked(self):
        if self.bg1.checkedId() == 1:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        elif self.bg1.checkedId() == 2:
            self.lb1.setAlignment(Qt.AlignCenter)
        elif self.bg1.checkedId() == 3:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '内容1', '请输入内容1：')
            if ok:
                self.lb2.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '内容2', '请输入内容2：')
            if ok:
                self.lb3.setText(str(text))


if __name__ == '__main__':
    # Qlabel1()
    app = QApplication(sys.argv)
    widgets = QLabelExample()
    sys.exit(app.exec_())
