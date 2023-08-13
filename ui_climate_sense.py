# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'climate_sense.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 700)
        MainWindow.setMinimumSize(QSize(650, 600))
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout_2 = QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.city_entry_layout = QHBoxLayout()
        self.city_entry_layout.setObjectName(u"city_entry_layout")
        self.city_entry = QLineEdit(self.central_widget)
        self.city_entry.setObjectName(u"city_entry")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_entry.sizePolicy().hasHeightForWidth())
        self.city_entry.setSizePolicy(sizePolicy)
        self.city_entry.setMaximumSize(QSize(300, 40))
        self.city_entry.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 10px;\n"
"height: 40px;\n"
"")
        self.city_entry.setAlignment(Qt.AlignCenter)

        self.city_entry_layout.addWidget(self.city_entry)


        self.verticalLayout_2.addLayout(self.city_entry_layout)

        self.weather_info_layout = QVBoxLayout()
        self.weather_info_layout.setObjectName(u"weather_info_layout")
        self.city_name = QLabel(self.central_widget)
        self.city_name.setObjectName(u"city_name")
        self.city_name.setAlignment(Qt.AlignCenter)

        self.weather_info_layout.addWidget(self.city_name)

        self.weather_icon = QLabel(self.central_widget)
        self.weather_icon.setObjectName(u"weather_icon")
        self.weather_icon.setAlignment(Qt.AlignCenter)

        self.weather_info_layout.addWidget(self.weather_icon)

        self.temperature_celsius = QLabel(self.central_widget)
        self.temperature_celsius.setObjectName(u"temperature_celsius")
        self.temperature_celsius.setAlignment(Qt.AlignCenter)

        self.weather_info_layout.addWidget(self.temperature_celsius)

        self.min_max_temp_layout = QHBoxLayout()
        self.min_max_temp_layout.setObjectName(u"min_max_temp_layout")
        self.left_spacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.min_max_temp_layout.addItem(self.left_spacer)

        self.min_temperature = QLabel(self.central_widget)
        self.min_temperature.setObjectName(u"min_temperature")
        self.min_temperature.setStyleSheet(u"")
        self.min_temperature.setAlignment(Qt.AlignCenter)

        self.min_max_temp_layout.addWidget(self.min_temperature)

        self.max_temperature = QLabel(self.central_widget)
        self.max_temperature.setObjectName(u"max_temperature")
        self.max_temperature.setAlignment(Qt.AlignCenter)

        self.min_max_temp_layout.addWidget(self.max_temperature)

        self.right_spacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.min_max_temp_layout.addItem(self.right_spacer)


        self.weather_info_layout.addLayout(self.min_max_temp_layout)

        self.description = QLabel(self.central_widget)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignCenter)

        self.weather_info_layout.addWidget(self.description)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.weather_info_layout.addItem(self.verticalSpacer)

        self.line = QFrame(self.central_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.weather_info_layout.addWidget(self.line)


        self.verticalLayout_2.addLayout(self.weather_info_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.day_1 = QVBoxLayout()
        self.day_1.setObjectName(u"day_1")
        self.date = QLabel(self.central_widget)
        self.date.setObjectName(u"date")
        self.date.setAlignment(Qt.AlignCenter)

        self.day_1.addWidget(self.date)

        self.icon = QLabel(self.central_widget)
        self.icon.setObjectName(u"icon")
        self.icon.setAlignment(Qt.AlignCenter)

        self.day_1.addWidget(self.icon)

        self.min_max_temperature = QLabel(self.central_widget)
        self.min_max_temperature.setObjectName(u"min_max_temperature")
        self.min_max_temperature.setAlignment(Qt.AlignCenter)

        self.day_1.addWidget(self.min_max_temperature)


        self.horizontalLayout.addLayout(self.day_1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.central_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.central_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.central_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.central_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_7 = QLabel(self.central_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.central_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.central_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_10 = QLabel(self.central_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_9 = QLabel(self.central_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_9)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.central_widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_11)

        self.label_13 = QLabel(self.central_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.label_12 = QLabel(self.central_widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_12)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.loading_layout = QVBoxLayout()
        self.loading_layout.setObjectName(u"loading_layout")
        self.label = QLabel(self.central_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.loading_layout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.loading_layout)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Climate Sense - Weather Application", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.city_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Unesite zeljenu lokaciju", None))
        self.city_name.setText(QCoreApplication.translate("MainWindow", u"city_name", None))
        self.weather_icon.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.temperature_celsius.setText(QCoreApplication.translate("MainWindow", u"temperature_celsius", None))
        self.min_temperature.setText(QCoreApplication.translate("MainWindow", u"min_temperature", None))
        self.max_temperature.setText(QCoreApplication.translate("MainWindow", u"max_temperature", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.icon.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.min_max_temperature.setText(QCoreApplication.translate("MainWindow", u"min_max", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"min_max", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"min_max", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"min_max", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"min_max", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Loading........", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

