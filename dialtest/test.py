# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

StyleSheet = """
/*这里是通用设置，所有按钮都有效，不过后面的可以覆盖这个*/
QPushButton {
    border: none; /*去掉边框*/
}
/*
QPushButton#xxx
或者
#xx
都表示通过设置的objectName来指定
*/
QPushButton#pushButton {
    background-color: #f44336; /*背景颜色*/
}
#pushButton:hover {
    background-color: #e57373; /*鼠标悬停时背景颜色*/
}
/*注意pressed一定要放在hover的后面，否则没有效果*/
#pushButton:pressed {
    background-color: #ffcdd2; /*鼠标按下不放时背景颜色*/
}
#pushButton_2 {
    background-color: #4caf50;
    border-radius: 5px; /*圆角*/
}
#pushButton_2:hover {
    background-color: #81c784;
}
#pushButton_2:pressed {
    background-color: #c8e6c9;
}
#pushButton_3 {
    background-color: #2196f3;
    /*限制最小最大尺寸*/
    min-width: 96px;
    max-width: 96px;
    min-height: 96px;
    max-height: 96px;
    border-radius: 48px; /*圆形*/
}
#pushButton_3:hover {
    background-color: #64b5f6;
}
#pushButton_3:pressed {
    background-color: #bbdefb;
}
#pushButton_4 {
    max-height: 48px;
    border-top-right-radius: 20px; /*右上角圆角*/
    border-bottom-left-radius: 20px; /*左下角圆角*/
    background-color: #ff9800;
}
#pushButton_4:hover {
    background-color: #ffb74d;
}
#pushButton_4:pressed {
    background-color: #ffe0b2;
}
/*根据文字内容来区分按钮,同理还可以根据其它属性来区分*/
#pushButton_5 {
    color: white; /*文字颜色*/
    background-color: #9c27b0;
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 478, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 48))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 48))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 48))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 48))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 478, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        # Qt Designer 设计器自动生成相关事件代码(信号/槽)
        # self.pushButton.clicked.connect(self.plainTextEdit.zoomIn)
        # self.pushButton_2.clicked.connect(self.plainTextEdit.zoomIn)
        # self.pushButton_3.clicked.connect(self.plainTextEdit.zoomIn)
        # self.pushButton_4.clicked.connect(self.plainTextEdit.zoomIn)
        # self.pushButton_5.clicked.connect(self.plainTextEdit.zoomIn)
        # 自定义函数进行相关(信号/槽)事件绑定
        self.pushButton.clicked.connect(self.onClicked)
        self.pushButton_2.clicked.connect(self.onPressed)
        self.pushButton_3.clicked.connect(self.onReleased)
        self.pushButton_4.clicked.connect(self.onToggled)
        self.pushButton_5.clicked.connect(self.onToggled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    # 自定义按钮点击触发事件
    def onClicked(self):
        self.plainTextEdit.appendPlainText(
            '按钮{0}被点击'.format(self.pushButton.objectName()))

    def onPressed(self):
        self.plainTextEdit.appendPlainText(
            '按钮{0}被按下'.format(self.pushButton_2.objectName()))

    def onReleased(self):
        self.plainTextEdit.appendPlainText(
            '按钮{0}被释放'.format(self.pushButton_3.objectName()))

    def onToggled(self, checked):
        self.plainTextEdit.appendPlainText(
            '按钮{0}被选中：{1}'.format(self.pushButton_4.objectName(), checked))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())