from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys
from ui_functions import consulta_cnpj
from database import Data_base
import pandas as pd
import sqlite3

