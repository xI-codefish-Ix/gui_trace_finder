# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.picspace = QLabel(self.centralwidget)
        self.picspace.setObjectName(u"picspace")
        self.picspace.setGeometry(QRect(90, 4, 600, 500)) #401, 331
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 470, 353, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_for_speed = QLineEdit(self.widget)
        self.line_for_speed.setObjectName(u"line_for_speed")

        self.horizontalLayout.addWidget(self.line_for_speed)

        self.line_for_angle = QLineEdit(self.widget)
        self.line_for_angle.setObjectName(u"line_for_angle")

        self.horizontalLayout.addWidget(self.line_for_angle)

        self.ok_button = QPushButton(self.widget)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout.addWidget(self.ok_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.picspace.setText("")
        self.line_for_speed.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.line_for_angle.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0443\u0433\u043e\u043b", None))
        self.ok_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a", None))
    # retranslateUi

