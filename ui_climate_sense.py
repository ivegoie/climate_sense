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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setMinimumSize(QSize(650, 500))
        MainWindow.setMaximumSize(QSize(650, 500))
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout_2 = QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.entry_frame = QFrame(self.central_widget)
        self.entry_frame.setObjectName(u"entry_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_frame.sizePolicy().hasHeightForWidth())
        self.entry_frame.setSizePolicy(sizePolicy)
        self.entry_frame.setStyleSheet(u"border: none;")
        self.entry_frame.setFrameShape(QFrame.StyledPanel)
        self.entry_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.entry_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.entry_label = QLabel(self.entry_frame)
        self.entry_label.setObjectName(u"entry_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entry_label.sizePolicy().hasHeightForWidth())
        self.entry_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        self.entry_label.setFont(font)
        self.entry_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.entry_label)

        self.entry_layout = QHBoxLayout()
        self.entry_layout.setObjectName(u"entry_layout")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.entry_layout.addItem(self.horizontalSpacer)

        self.city_entry = QLineEdit(self.entry_frame)
        self.city_entry.setObjectName(u"city_entry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.city_entry.sizePolicy().hasHeightForWidth())
        self.city_entry.setSizePolicy(sizePolicy2)
        self.city_entry.setMaximumSize(QSize(300, 40))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(15)
        self.city_entry.setFont(font1)
        self.city_entry.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid white;\n"
"padding-left: 10px;\n"
"height: 40px;\n"
"background: transparent;")
        self.city_entry.setAlignment(Qt.AlignCenter)

        self.entry_layout.addWidget(self.city_entry)

        self.submit_button = QPushButton(self.entry_frame)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setFont(font1)
        self.submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_button.setStyleSheet(u"background: transparent;\n"
"border: 1px solid white;\n"
"height: 40px;\n"
"border-radius: 15px;")

        self.entry_layout.addWidget(self.submit_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.entry_layout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.entry_layout)


        self.verticalLayout_2.addWidget(self.entry_frame)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.city_name.sizePolicy().hasHeightForWidth())
        self.city_name.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(38)
        font2.setBold(False)
        self.city_name.setFont(font2)
        self.city_name.setStyleSheet(u"")
        self.city_name.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.city_name)

        self.weather_icon = QLabel(self.weather_frame)
        self.weather_icon.setObjectName(u"weather_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.weather_icon.sizePolicy().hasHeightForWidth())
        self.weather_icon.setSizePolicy(sizePolicy4)
        self.weather_icon.setStyleSheet(u"")
        self.weather_icon.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.weather_icon)

        self.current_temperature = QHBoxLayout()
        self.current_temperature.setObjectName(u"current_temperature")
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.current_temperature.addItem(self.horizontalSpacer_3)

        self.feels_like = QLabel(self.weather_frame)
        self.feels_like.setObjectName(u"feels_like")
        self.feels_like.setFont(font1)
        self.feels_like.setStyleSheet(u"")
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
        sizePolicy3.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(13)
        self.description.setFont(font3)
        self.description.setStyleSheet(u"padding: 10px 0px;")
        self.description.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.description)


        self.verticalLayout_3.addLayout(self.info_layout)


        self.verticalLayout_2.addWidget(self.weather_frame)

        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 650, 21))
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_help = QMenu(self.menu_bar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_quit)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Climate Sense", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.entry_label.setText(QCoreApplication.translate("MainWindow", u"Search for your location", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.city_name.setText(QCoreApplication.translate("MainWindow", u"city_name", None))
        self.weather_icon.setText(QCoreApplication.translate("MainWindow", u"weather_icon", None))
        self.feels_like.setText(QCoreApplication.translate("MainWindow", u"feels_like", None))
        self.temperature.setText(QCoreApplication.translate("MainWindow", u"temperature_celsius", None))
        self.sunrise.setText(QCoreApplication.translate("MainWindow", u"sunrise", None))
        self.sunset.setText(QCoreApplication.translate("MainWindow", u"sunset", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

