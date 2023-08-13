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
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 600)
        MainWindow.setMinimumSize(QSize(650, 600))
        MainWindow.setMaximumSize(QSize(667, 600))
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
        self.frame = QFrame(self.central_widget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.city_entry = QLineEdit(self.frame)
        self.city_entry.setObjectName(u"city_entry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.city_entry.sizePolicy().hasHeightForWidth())
        self.city_entry.setSizePolicy(sizePolicy2)
        self.city_entry.setMaximumSize(QSize(300, 40))
        self.city_entry.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid white;\n"
"padding-left: 10px;\n"
"height: 40px;\n"
"")
        self.city_entry.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.city_entry)

        self.submit_button = QPushButton(self.frame)
        self.submit_button.setObjectName(u"submit_button")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(15)
        self.submit_button.setFont(font1)
        self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_button.setStyleSheet(u"background: transparent;\n"
"border: 1px solid white;\n"
"height: 40px;\n"
"border-radius: 15px;")

        self.horizontalLayout.addWidget(self.submit_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.weather_frame = QFrame(self.central_widget)
        self.weather_frame.setObjectName(u"weather_frame")
        self.weather_frame.setStyleSheet(u"border: none;")
        self.weather_frame.setFrameShape(QFrame.StyledPanel)
        self.weather_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.weather_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.info_layout = QVBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.city_name = QLabel(self.weather_frame)
        self.city_name.setObjectName(u"city_name")
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(30)
        font2.setBold(False)
        self.city_name.setFont(font2)
        self.city_name.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.city_name)

        self.weather_icon = QLabel(self.weather_frame)
        self.weather_icon.setObjectName(u"weather_icon")
        self.weather_icon.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.weather_icon)

        self.current_temperature = QHBoxLayout()
        self.current_temperature.setObjectName(u"current_temperature")
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.current_temperature.addItem(self.horizontalSpacer_3)

        self.feels_like = QLabel(self.weather_frame)
        self.feels_like.setObjectName(u"feels_like")
        self.feels_like.setFont(font1)
        self.feels_like.setAlignment(Qt.AlignCenter)

        self.current_temperature.addWidget(self.feels_like)

        self.temperature = QLabel(self.weather_frame)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setFont(font1)
        self.temperature.setAlignment(Qt.AlignCenter)

        self.current_temperature.addWidget(self.temperature)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.current_temperature.addItem(self.horizontalSpacer_4)


        self.info_layout.addLayout(self.current_temperature)

        self.min_max_temp_layout = QHBoxLayout()
        self.min_max_temp_layout.setObjectName(u"min_max_temp_layout")
        self.left_spacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.min_max_temp_layout.addItem(self.left_spacer)

        self.sunrise = QLabel(self.weather_frame)
        self.sunrise.setObjectName(u"sunrise")
        self.sunrise.setFont(font1)
        self.sunrise.setStyleSheet(u"")
        self.sunrise.setAlignment(Qt.AlignCenter)

        self.min_max_temp_layout.addWidget(self.sunrise)

        self.sunset = QLabel(self.weather_frame)
        self.sunset.setObjectName(u"sunset")
        self.sunset.setFont(font1)
        self.sunset.setAlignment(Qt.AlignCenter)

        self.min_max_temp_layout.addWidget(self.sunset)

        self.right_spacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.min_max_temp_layout.addItem(self.right_spacer)


        self.info_layout.addLayout(self.min_max_temp_layout)

        self.description = QLabel(self.weather_frame)
        self.description.setObjectName(u"description")
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(13)
        self.description.setFont(font3)
        self.description.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.description)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.info_layout.addItem(self.verticalSpacer)

        self.line = QFrame(self.weather_frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"Line {\n"
"	border-top: 1px solid gray;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.info_layout.addWidget(self.line)

        self.days_layout = QHBoxLayout()
        self.days_layout.setObjectName(u"days_layout")
        self.day_frame = QFrame(self.weather_frame)
        self.day_frame.setObjectName(u"day_frame")
        self.day_frame.setStyleSheet(u"margin-top: 5px;\n"
"margin-bottom: 5px;")
        self.day_frame.setFrameShape(QFrame.StyledPanel)
        self.day_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.day_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.date = QLabel(self.day_frame)
        self.date.setObjectName(u"date")
        self.date.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.date)

        self.icon = QLabel(self.day_frame)
        self.icon.setObjectName(u"icon")
        self.icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.icon)

        self.min_max_temperature = QLabel(self.day_frame)
        self.min_max_temperature.setObjectName(u"min_max_temperature")
        self.min_max_temperature.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.min_max_temperature)


        self.days_layout.addWidget(self.day_frame, 0, Qt.AlignVCenter)


        self.info_layout.addLayout(self.days_layout)


        self.verticalLayout_3.addLayout(self.info_layout)

        self.loading_frame = QFrame(self.weather_frame)
        self.loading_frame.setObjectName(u"loading_frame")
        self.loading_frame.setStyleSheet(u"border: none;")
        self.loading_frame.setFrameShape(QFrame.StyledPanel)
        self.loading_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.loading_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loading_label = QLabel(self.loading_frame)
        self.loading_label.setObjectName(u"loading_label")
        font4 = QFont()
        font4.setPointSize(20)
        self.loading_label.setFont(font4)
        self.loading_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.loading_label)


        self.verticalLayout_3.addWidget(self.loading_frame)


        self.verticalLayout_2.addWidget(self.weather_frame)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Climate Sense", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter your location", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.city_name.setText(QCoreApplication.translate("MainWindow", u"city_name", None))
        self.weather_icon.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.feels_like.setText(QCoreApplication.translate("MainWindow", u"feels_like", None))
        self.temperature.setText(QCoreApplication.translate("MainWindow", u"temperature_celsius", None))
        self.sunrise.setText(QCoreApplication.translate("MainWindow", u"sunrise", None))
        self.sunset.setText(QCoreApplication.translate("MainWindow", u"sunset", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.icon.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.min_max_temperature.setText(QCoreApplication.translate("MainWindow", u"min_max", None))
        self.loading_label.setText(QCoreApplication.translate("MainWindow", u"Loading........", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

