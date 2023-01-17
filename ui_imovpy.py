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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 774)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.frame_aside.setStyleSheet(u"background-color: rgb(52,39,0);")
        self.frame_aside.setFrameShape(QFrame.StyledPanel)
        self.frame_aside.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_aside)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menu_aside_main = QFrame(self.frame_aside)
        self.menu_aside_main.setObjectName(u"menu_aside_main")
        self.menu_aside_main.setStyleSheet(u"background-color: #55430C;")
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
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.btn_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.btn_consultar.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.frame_main.setMaximumSize(QSize(1500, 600))
        self.frame_main.setStyleSheet(u"background-color: rgb(52,39,0);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_header = QFrame(self.frame_main)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 50))
        self.frame_header.setMaximumSize(QSize(16777215, 50))
        self.frame_header.setStyleSheet(u"background-color: #55430C;")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_toggle_button = QPushButton(self.frame_header)
        self.btn_toggle_button.setObjectName(u"btn_toggle_button")
        self.btn_toggle_button.setMinimumSize(QSize(50, 30))
        self.btn_toggle_button.setMaximumSize(QSize(50, 30))
        self.btn_toggle_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_toggle_button)

        self.frame_title = QLabel(self.frame_header)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setMaximumSize(QSize(16777215, 30))
        self.frame_title.setMargin(10)

        self.horizontalLayout_5.addWidget(self.frame_title)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_main_content = QFrame(self.frame_main)
        self.frame_main_content.setObjectName(u"frame_main_content")
        sizePolicy.setHeightForWidth(self.frame_main_content.sizePolicy().hasHeightForWidth())
        self.frame_main_content.setSizePolicy(sizePolicy)
        self.frame_main_content.setStyleSheet(u"background-color: #55430C;")
        self.frame_main_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_main_content)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabWidget = QTabWidget(self.frame_main_content)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #342700;\n"
"}\n"
"QTabBar::tab{\n"
"	background-color: rgb(87, 65, 0);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"	background-color: rgb(120, 99, 36);\n"
"}\n"
"\n"
"\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_Home = QWidget()
        self.tab_Home.setObjectName(u"tab_Home")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_Home)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_image = QLabel(self.tab_Home)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setStyleSheet(u"image: url(:/icons/Icons/logo2.png);")

        self.horizontalLayout_7.addWidget(self.label_image)

        self.tabWidget.addTab(self.tab_Home, "")
        self.tab_Cadastro = QWidget()
        self.tab_Cadastro.setObjectName(u"tab_Cadastro")
        self.tab_Cadastro.setStyleSheet(u"QComboBox{\n"
"	background-color: #786324;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: #786324;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	background-color: #786324;\n"
"}")
        self.comboBox_status = QComboBox(self.tab_Cadastro)
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.setObjectName(u"comboBox_status")
        self.comboBox_status.setGeometry(QRect(10, 210, 161, 21))
        self.comboBox_caracteristica = QComboBox(self.tab_Cadastro)
        self.comboBox_caracteristica.addItem("")
        self.comboBox_caracteristica.addItem("")
        self.comboBox_caracteristica.addItem("")
        self.comboBox_caracteristica.addItem("")
        self.comboBox_caracteristica.addItem("")
        self.comboBox_caracteristica.setObjectName(u"comboBox_caracteristica")
        self.comboBox_caracteristica.setGeometry(QRect(10, 250, 161, 21))
        self.comboBox_opcao = QComboBox(self.tab_Cadastro)
        self.comboBox_opcao.addItem("")
        self.comboBox_opcao.addItem("")
        self.comboBox_opcao.setObjectName(u"comboBox_opcao")
        self.comboBox_opcao.setGeometry(QRect(10, 290, 161, 21))
        self.textEdit_descricao = QTextEdit(self.tab_Cadastro)
        self.textEdit_descricao.setObjectName(u"textEdit_descricao")
        self.textEdit_descricao.setGeometry(QRect(190, 170, 621, 181))
        self.comboBox_tipo = QComboBox(self.tab_Cadastro)
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.setObjectName(u"comboBox_tipo")
        self.comboBox_tipo.setGeometry(QRect(10, 170, 161, 21))
        self.lineEdit_valor = QLineEdit(self.tab_Cadastro)
        self.lineEdit_valor.setObjectName(u"lineEdit_valor")
        self.lineEdit_valor.setGeometry(QRect(10, 330, 161, 21))
        self.lineEdit_valor.setAlignment(Qt.AlignCenter)
        self.lineEdit_cpf_cnpj = QLineEdit(self.tab_Cadastro)
        self.lineEdit_cpf_cnpj.setObjectName(u"lineEdit_cpf_cnpj")
        self.lineEdit_cpf_cnpj.setGeometry(QRect(290, 10, 161, 21))
        self.lineEdit_cpf_cnpj.setAlignment(Qt.AlignCenter)
        self.lineEdit_nome = QLineEdit(self.tab_Cadastro)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(470, 10, 341, 21))
        self.lineEdit_nome.setAlignment(Qt.AlignCenter)
        self.lineEdit_id = QLineEdit(self.tab_Cadastro)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(10, 10, 81, 21))
        self.lineEdit_id.setAlignment(Qt.AlignCenter)
        self.lineEdit_logradouro = QLineEdit(self.tab_Cadastro)
        self.lineEdit_logradouro.setObjectName(u"lineEdit_logradouro")
        self.lineEdit_logradouro.setGeometry(QRect(10, 50, 441, 21))
        self.lineEdit_logradouro.setAlignment(Qt.AlignCenter)
        self.comboBox_persona = QComboBox(self.tab_Cadastro)
        self.comboBox_persona.addItem("")
        self.comboBox_persona.addItem("")
        self.comboBox_persona.setObjectName(u"comboBox_persona")
        self.comboBox_persona.setGeometry(QRect(110, 10, 161, 21))
        self.lineEdit_numero = QLineEdit(self.tab_Cadastro)
        self.lineEdit_numero.setObjectName(u"lineEdit_numero")
        self.lineEdit_numero.setGeometry(QRect(470, 50, 161, 21))
        self.lineEdit_numero.setAlignment(Qt.AlignCenter)
        self.lineEdit_complemento = QLineEdit(self.tab_Cadastro)
        self.lineEdit_complemento.setObjectName(u"lineEdit_complemento")
        self.lineEdit_complemento.setGeometry(QRect(650, 50, 161, 21))
        self.lineEdit_complemento.setAlignment(Qt.AlignCenter)
        self.lineEdit_cidade = QLineEdit(self.tab_Cadastro)
        self.lineEdit_cidade.setObjectName(u"lineEdit_cidade")
        self.lineEdit_cidade.setGeometry(QRect(370, 90, 341, 21))
        self.lineEdit_cidade.setAlignment(Qt.AlignCenter)
        self.lineEdit_bairro = QLineEdit(self.tab_Cadastro)
        self.lineEdit_bairro.setObjectName(u"lineEdit_bairro")
        self.lineEdit_bairro.setGeometry(QRect(10, 90, 341, 21))
        self.lineEdit_bairro.setAlignment(Qt.AlignCenter)
        self.lineEdit_uf = QLineEdit(self.tab_Cadastro)
        self.lineEdit_uf.setObjectName(u"lineEdit_uf")
        self.lineEdit_uf.setGeometry(QRect(730, 90, 81, 21))
        self.lineEdit_uf.setAlignment(Qt.AlignCenter)
        self.lineEdit_cep = QLineEdit(self.tab_Cadastro)
        self.lineEdit_cep.setObjectName(u"lineEdit_cep")
        self.lineEdit_cep.setGeometry(QRect(10, 130, 161, 21))
        self.lineEdit_cep.setAlignment(Qt.AlignCenter)
        self.lineEdit_telefone = QLineEdit(self.tab_Cadastro)
        self.lineEdit_telefone.setObjectName(u"lineEdit_telefone")
        self.lineEdit_telefone.setGeometry(QRect(190, 130, 161, 21))
        self.lineEdit_telefone.setAlignment(Qt.AlignCenter)
        self.lineEdit_celular = QLineEdit(self.tab_Cadastro)
        self.lineEdit_celular.setObjectName(u"lineEdit_celular")
        self.lineEdit_celular.setGeometry(QRect(370, 130, 161, 21))
        self.lineEdit_celular.setAlignment(Qt.AlignCenter)
        self.lineEdit_email = QLineEdit(self.tab_Cadastro)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(550, 130, 261, 21))
        self.lineEdit_email.setAlignment(Qt.AlignCenter)
        self.frame_btn_cadastro = QFrame(self.tab_Cadastro)
        self.frame_btn_cadastro.setObjectName(u"frame_btn_cadastro")
        self.frame_btn_cadastro.setGeometry(QRect(10, 360, 801, 40))
        self.frame_btn_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_cadastro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btn_cadastro)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_cadastrar = QPushButton(self.frame_btn_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(200, 25))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_limpar = QPushButton(self.frame_btn_cadastro)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setMaximumSize(QSize(200, 25))
        self.btn_limpar.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_limpar)

        self.tabWidget.addTab(self.tab_Cadastro, "")
        self.tab_Consultar = QWidget()
        self.tab_Consultar.setObjectName(u"tab_Consultar")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_Consultar)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_main_consulta = QFrame(self.tab_Consultar)
        self.frame_main_consulta.setObjectName(u"frame_main_consulta")
        self.frame_main_consulta.setMaximumSize(QSize(636, 16777215))
        self.frame_main_consulta.setFrameShape(QFrame.StyledPanel)
        self.frame_main_consulta.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_main_consulta)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_main_consulta)
        if (self.tableWidget.columnCount() < 20):
            self.tableWidget.setColumnCount(20)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_6.addWidget(self.tableWidget)


        self.horizontalLayout_8.addWidget(self.frame_main_consulta)

        self.frame_consulta_menu = QFrame(self.tab_Consultar)
        self.frame_consulta_menu.setObjectName(u"frame_consulta_menu")
        self.frame_consulta_menu.setMaximumSize(QSize(130, 16777215))
        self.frame_consulta_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_consulta_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_consulta_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_gerar_excel = QPushButton(self.frame_consulta_menu)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(0, 30))
        self.btn_gerar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_gerar_excel)

        self.btn_alterar = QPushButton(self.frame_consulta_menu)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_consulta_menu)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton {\n"
"	background-color: #786324;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #c49300;\n"
"	border-radius: 5px\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.frame_consulta_menu)

        self.tabWidget.addTab(self.tab_Consultar, "")
        self.tab_Contato = QWidget()
        self.tab_Contato.setObjectName(u"tab_Contato")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_Contato)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_contato = QLabel(self.tab_Contato)
        self.label_contato.setObjectName(u"label_contato")
        self.label_contato.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_contato.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_contato)

        self.tabWidget.addTab(self.tab_Contato, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame_main_content)

        self.frame_footer = QFrame(self.frame_main)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 50))
        self.frame_footer.setMaximumSize(QSize(16777215, 50))
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_footer = QLabel(self.frame_footer)
        self.label_footer.setObjectName(u"label_footer")
        self.label_footer.setMinimumSize(QSize(0, 30))
        self.label_footer.setMaximumSize(QSize(16777215, 30))
        self.label_footer.setSizeIncrement(QSize(0, 0))
        self.label_footer.setStyleSheet(u"background-color: #55430C;")
        self.label_footer.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_footer)


        self.verticalLayout.addWidget(self.frame_footer)


        self.horizontalLayout_2.addWidget(self.frame_main)


        self.gridLayout.addWidget(self.frame_page_content, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menu_aside_content.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.menu_aside_content.setItemText(self.menu_aside_content.indexOf(self.page_1_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_page_2.setText(QCoreApplication.translate("MainWindow", u"Programa criado para mat\u00e9ria de P\u00f3s Gradua\u00e7\u00e3o em linguagem Python, da Unicesumar.", None))
        self.menu_aside_content.setItemText(self.menu_aside_content.indexOf(self.page_2_menu), QCoreApplication.translate("MainWindow", u"Info", None))
        self.btn_toggle_button.setText("")
        self.frame_title.setText(QCoreApplication.translate("MainWindow", u"ImovPy - Cadastro de im\u00f3veis", None))
        self.label_image.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.comboBox_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.comboBox_status.setItemText(1, QCoreApplication.translate("MainWindow", u"Dispon\u00edvel", None))
        self.comboBox_status.setItemText(2, QCoreApplication.translate("MainWindow", u"Locado", None))
        self.comboBox_status.setItemText(3, QCoreApplication.translate("MainWindow", u"Vendido", None))
        self.comboBox_status.setItemText(4, QCoreApplication.translate("MainWindow", u"\u00c0 Liberar", None))

        self.comboBox_caracteristica.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.comboBox_caracteristica.setItemText(1, QCoreApplication.translate("MainWindow", u"Apartamento", None))
        self.comboBox_caracteristica.setItemText(2, QCoreApplication.translate("MainWindow", u"Casa", None))
        self.comboBox_caracteristica.setItemText(3, QCoreApplication.translate("MainWindow", u"Terreno", None))
        self.comboBox_caracteristica.setItemText(4, QCoreApplication.translate("MainWindow", u"Rural", None))

        self.comboBox_opcao.setItemText(0, QCoreApplication.translate("MainWindow", u"Vis\u00edvel", None))
        self.comboBox_opcao.setItemText(1, QCoreApplication.translate("MainWindow", u"Oculto", None))

        self.comboBox_tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.comboBox_tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Venda", None))
        self.comboBox_tipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Loca\u00e7\u00e3o", None))
        self.comboBox_tipo.setItemText(3, QCoreApplication.translate("MainWindow", u"Venda/Loca\u00e7\u00e3o", None))

        self.lineEdit_valor.setText("")
        self.lineEdit_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.lineEdit_cpf_cnpj.setText("")
        self.lineEdit_cpf_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None))
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME/RAZ\u00c3O SOCIAL", None))
        self.lineEdit_id.setText("")
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lineEdit_logradouro.setText("")
        self.lineEdit_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.comboBox_persona.setItemText(0, QCoreApplication.translate("MainWindow", u"Jur\u00eddica", None))
        self.comboBox_persona.setItemText(1, QCoreApplication.translate("MainWindow", u"F\u00edsica", None))

        self.lineEdit_numero.setText("")
        self.lineEdit_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.lineEdit_complemento.setText("")
        self.lineEdit_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.lineEdit_cidade.setText("")
        self.lineEdit_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.lineEdit_bairro.setText("")
        self.lineEdit_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.lineEdit_uf.setText("")
        self.lineEdit_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.lineEdit_cep.setText("")
        self.lineEdit_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_telefone.setText("")
        self.lineEdit_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.lineEdit_celular.setText("")
        self.lineEdit_celular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CELULAR", None))
        self.lineEdit_email.setText("")
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PERSONA", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NOME/RAZ\u00c3O", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"CELULAR", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TIPO", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"CARACTER\u00cdSTICAS", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"VISIBILIDADE", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"VALOR", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None));
        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Consultar), QCoreApplication.translate("MainWindow", u"Consulta", None))
        self.label_contato.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Icons/whatsapp.png\"/><span style=\" font-size:24pt; vertical-align:super;\">(44)98862-0946</span></p><p align=\"center\"><img src=\":/icons/Icons/linkedin.png\"/><span style=\" font-size:24pt; vertical-align:super;\">https://www.linkedin.com/in/marcelo-l-galli-488671101/</span></p><p align=\"center\"><img src=\":/icons/Icons/github.png\"/><span style=\" font-size:24pt; vertical-align:super;\">https://github.com/MarceloGalliDev</span></p><p align=\"center\"><img src=\":/icons/Icons/instagram.png\"/><span style=\" font-size:24pt; vertical-align:super;\">https://www.instagram.com/marcelogalli/</span></p><p align=\"center\"><img src=\":/icons/Icons/google+.png\"/><span style=\" font-size:24pt; vertical-align:super;\">marcelolemesgalli2@gmail.com</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Contato), QCoreApplication.translate("MainWindow", u"Contato", None))
        self.label_footer.setText(QCoreApplication.translate("MainWindow", u"Created by Galli, Marcelo L. \u24c7", None))
    # retranslateUi

