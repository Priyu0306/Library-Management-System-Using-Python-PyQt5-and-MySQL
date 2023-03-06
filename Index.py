from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType

ui, _ = loadUiType('library ms.ui')


class MainApp(QMainWindow, ui):
    def int(self):
        QMainWindow.init(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

    def Handel_UI_Changes(self):
        self.Hiding_Themes()

    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_14.clicked.connect(self.Hiding_Themes)

        self. 
    def Show_Themes(self):
        self.groupBox.show()

    def Hiding_Themes(self):
        self.groupBox.hide()

    def Open_Day_To_Day_Tab(self):
        pass

    ###########################
    #####opening tabs##########
    def Open_Books_Tab(self):
        pass

    def Open_Users_Tab(self):
        pass

    def Open_Settings_Tab(self):
        pass

        def main():
            app = QApplication(sys.argv)
            window = MainApp()
            window.show()
            app.exec_()

            if _name_ == '_main_':
                main()