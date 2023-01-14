# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imovpy.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QToolBox, QVBoxLayout, QWidget, QtSvg)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1202, 826)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_page_content = QFrame(self.centralwidget)
        self.frame_page_content.setObjectName(u"frame_page_content")
        self.frame_page_content.setMinimumSize(QSize(1000, 630))
        self.frame_page_content.setMaximumSize(QSize(1110, 630))
        self.frame_page_content.setStyleSheet(u"background-color: rgba(52,39,0,100);\n"
"border-radius: 5px;")
        self.frame_page_content.setFrameShape(QFrame.StyledPanel)
        self.frame_page_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_page_content)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_aside = QFrame(self.frame_page_content)
        self.frame_aside.setObjectName(u"frame_aside")
        self.frame_aside.setMinimumSize(QSize(200, 600))
        self.frame_aside.setMaximumSize(QSize(200, 600))
        self.frame_aside.setStyleSheet(u"background-color: rgba(52,39,0,100);")
        self.frame_aside.setFrameShape(QFrame.StyledPanel)
        self.frame_aside.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_aside)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menu_aside_main = QFrame(self.frame_aside)
        self.menu_aside_main.setObjectName(u"menu_aside_main")
        self.menu_aside_main.setFrameShape(QFrame.StyledPanel)
        self.menu_aside_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.menu_aside_main)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu_aside_content = QToolBox(self.menu_aside_main)
        self.menu_aside_content.setObjectName(u"menu_aside_content")
        self.menu_aside_content.setMaximumSize(QSize(152, 16777215))
        self.menu_aside_content.setStyleSheet(u"QFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgba(52,39,0,0);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	background-color: #786324;\n"
"}\n"
"\n"
"QToolBox::tab:hover{\n"
"	background-color: #c49300;\n"
"	border-radius: 5px;\n"
"}")
        self.page_1_menu = QWidget()
        self.page_1_menu.setObjectName(u"page_1_menu")
        self.page_1_menu.setGeometry(QRect(0, 0, 152, 484))
        self.verticalLayout_3 = QVBoxLayout(self.page_1_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_home = QPushButton(self.page_1_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setMaximumSize(QSize(16777215, 30))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_cadastro = QPushButton(self.page_1_menu)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(0, 30))
        self.btn_cadastro.setMaximumSize(QSize(16777215, 30))
        self.btn_cadastro.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_cadastro)

        self.btn_consultar = QPushButton(self.page_1_menu)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setMinimumSize(QSize(0, 30))
        self.btn_consultar.setMaximumSize(QSize(16777215, 30))
        self.btn_consultar.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_consultar)

        self.btn_contato = QPushButton(self.page_1_menu)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 30))
        self.btn_contato.setMaximumSize(QSize(16777215, 30))
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_contato)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.menu_aside_content.addItem(self.page_1_menu, u"Menu")
        self.page_2_menu = QWidget()
        self.page_2_menu.setObjectName(u"page_2_menu")
        self.page_2_menu.setGeometry(QRect(0, 0, 152, 484))
        self.horizontalLayout_4 = QHBoxLayout(self.page_2_menu)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_page_2 = QLabel(self.page_2_menu)
        self.label_page_2.setObjectName(u"label_page_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_page_2.sizePolicy().hasHeightForWidth())
        self.label_page_2.setSizePolicy(sizePolicy)
        self.label_page_2.setMaximumSize(QSize(152, 16777215))
        font = QFont()
        font.setPointSize(15)
        self.label_page_2.setFont(font)
        self.label_page_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_page_2.setWordWrap(True)
        self.label_page_2.setMargin(10)
        self.label_page_2.setIndent(0)

        self.horizontalLayout_4.addWidget(self.label_page_2)

        self.menu_aside_content.addItem(self.page_2_menu, u"Info")

        self.horizontalLayout_3.addWidget(self.menu_aside_content)


        self.verticalLayout_2.addWidget(self.menu_aside_main)


        self.horizontalLayout_2.addWidget(self.frame_aside)

        self.frame_main = QFrame(self.frame_page_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setMinimumSize(QSize(800, 600))
        self.frame_main.setMaximumSize(QSize(900, 600))
        self.frame_main.setStyleSheet(u"background-color: rgba(52,39,0,100);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frame_main)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_toggle_button = QPushButton(self.frame)
        self.btn_toggle_button.setObjectName(u"btn_toggle_button")
        self.btn_toggle_button.setMinimumSize(QSize(50, 30))
        self.btn_toggle_button.setMaximumSize(QSize(50, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_toggle_button)

        self.frame_title = QLabel(self.frame)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setMaximumSize(QSize(16777215, 30))
        self.frame_title.setMargin(10)

        self.horizontalLayout_5.addWidget(self.frame_title)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_main)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setSizeIncrement(QSize(0, 0))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_main)


        self.horizontalLayout.addWidget(self.frame_page_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menu_aside_content.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.menu_aside_content.setItemText(self.menu_aside_content.indexOf(self.page_1_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_page_2.setText(QCoreApplication.translate("MainWindow", u"Programa criado para mat\u00e9ria de P\u00f3s Gradua\u00e7\u00e3o em linguagem Python, da Unicesumar.", None))
        self.menu_aside_content.setItemText(self.menu_aside_content.indexOf(self.page_2_menu), QCoreApplication.translate("MainWindow", u"Info", None))
        self.btn_toggle_button.setText("")
        self.frame_title.setText(QCoreApplication.translate("MainWindow", u"ImovPy - Cadastro de im\u00f3veis", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Created by Galli, Marcelo L. \u24c7", None))
    # retranslateUi

