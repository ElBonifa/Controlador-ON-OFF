
import os
import sys
from PyQt5 import QtCore, QtWidgets
#import pandas as pd
import json
import time
import random
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport

ODataFrame = [{"Tiempo": 1, "Variable": 4, "Respuesta": 11}, {"Tiempo": 2, "Variable": 7, "Respuesta": 1}]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ####------------Valores de set point y histeresis---------------

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(30, 400, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setValue(10)
        self.doubleSpinBox.setMinimum(-20)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(160, 400, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setSingleStep(0.5)
        self.doubleSpinBox_2.setMinimum(-20)
        self.doubleSpinBox_2.setMaximum(0)
        self.doubleSpinBox_2.setValue(0)

        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(285, 400, 62, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setSingleStep(0.5)
        self.doubleSpinBox_3.setValue(1)
        valor1 = self.doubleSpinBox.value()
        valor2 = self.doubleSpinBox_2.value()
        valor3 = self.doubleSpinBox_3.value()
        print(valor1, valor2, valor3)
        print(type(valor3))
        #####------------------Termina Spines---------------------

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 480, 200, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.Graficart)



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 480, 200, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Setpoint)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 90, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##### -----------------Barra de menu de archivos con Iconos-------------------
        self.barraguar = QtWidgets.QPushButton(self.centralwidget)
        rMyIcon = QtGui.QPixmap('./Adwaita/32x32/legacy/document-save-as.png');
        self.barraguar.setIcon(QtGui.QIcon(rMyIcon))
        self.barraguar.setGeometry(QtCore.QRect(44,0,44,44))
        self.barraguar.clicked.connect(self.SaveProject)

        self.barrabrir = QtWidgets.QPushButton(self.centralwidget)
        rMyIcon1 = QtGui.QPixmap('./Adwaita/22x22/legacy/document-open.png');
        self.barrabrir.setIcon(QtGui.QIcon(rMyIcon1))
        self.barrabrir.setGeometry(QtCore.QRect(0, 0, 44, 44))
        self.barrabrir.clicked.connect(self.Barraabrir)

        #'./Adwaita/32x32/legacy/preferences-system-network.png'
        self.barraexpor = QtWidgets.QPushButton(self.centralwidget)
        rMyIcon2 = QtGui.QPixmap('./Adwaita/22x22/legacy/document-pdf.png')
        self.barraexpor.setIcon(QtGui.QIcon(rMyIcon2))
        self.barraexpor.setGeometry(QtCore.QRect(88, 0, 44, 44))
        self.barraexpor.clicked.connect(self.Exporproject)

        ######----------------Botonnes de servidor--------------------
        self.pushButtoninternetS = QtWidgets.QPushButton(self.centralwidget)
        rMyIcon3 = QtGui.QPixmap('./Adwaita/22x22/legacy/network-transmit')
        self.pushButtoninternetS.setIcon(QtGui.QIcon(rMyIcon3))
        self.pushButtoninternetS.setGeometry(QtCore.QRect(176, 0, 44, 44))
        self.pushButtoninternetS.clicked.connect(self.Client)
        self.pushButtoninternetS.clicked.connect(self.Graficart)

        self.pushButtoninternetC = QtWidgets.QPushButton(self.centralwidget)
        rMyIcon4 = QtGui.QPixmap('./Adwaita/22x22/legacy/network-wired')
        self.pushButtoninternetC.setIcon(QtGui.QIcon(rMyIcon4))
        self.pushButtoninternetC.setGeometry(QtCore.QRect(132, 0, 44, 44))
        self.pushButtoninternetC.clicked.connect(self.Server)

        #self.Setpoint(valor1,valor2,valor3)
        #self.pushButton.clicked.connect(self)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 350, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("          Set-point")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(135, 350, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(255, 350, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2.setPlaceholderText("      Valor manimo")
        self.lineEdit_3.setPlaceholderText("      Valor maximo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Control ON OFF"))
        self.pushButton.setText(_translate("MainWindow", "Iniciar controlador"))
        self.pushButton_2.setText(_translate("MainWindow", "Fijar valores de consigna/Rangos"))

    def Barraabrir(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName()
        if fileName != "":
            print(fileName)
            print(type(fileName))

            ODataFrame = fileName
            with open(ODataFrame) as file:
                type(file)
                letraslist = []
                for letras in fileName:
                    letraslist.append(letras)
                lestraliststr = str(letraslist[-4]) + str(letraslist[-3]) + str(letraslist[-2]) + str(letraslist[-1])
                print(lestraliststr)
                if "json" == lestraliststr:
                    data = json.load(file)
                    print(data)
                    return data

    def SaveProject(self):
        option = QFileDialog.Options()
        file = QFileDialog.getSaveFileName(caption= 'ODataFrame.json',options = option)
        print(file[0])
        file2 = file[0]
        archivo = open(str(file2), "w")
        archivo.write(str(ODataFrame))

        archivo.close()
    def Exporproject(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName()
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"

    def Server(self):
        import mdbus_server as server
        print("Ejecuto server")
        return server

    def Client(self):
        import mdbus_client as client
        print("Ejecuto client")

        return client
    def Graficart(self):
        import graficatm as grafica
        return grafica
    def Graf(self):
        grafica = 0
        print(grafica)
    def Setpoint(self):
        valor1 = self.doubleSpinBox.value()
        valor2 = self.doubleSpinBox_2.value()
        valor3 = self.doubleSpinBox_3.value()
        self.Setpoint2(valor1,valor2,valor3)
    def Setpoint2(self,Set_point, Valorminimo, Valormaximo):
        with open('Setpoint2.json', 'w') as file:
            list = [(Set_point, Set_point, Set_point)]
            json.dump(list, file)

        with open('valorminimo.json', 'w') as file2:
            list = [(Set_point+Valorminimo, Set_point+Valorminimo, Set_point+Valorminimo)]
            json.dump(list, file2)
        with open('valormaximo.json', 'w') as file3:
            list = [(Set_point+Valormaximo, Set_point+Valormaximo, Set_point+Valormaximo)]
            json.dump(list, file3)
        print(Set_point)
        print(Valorminimo)
        print(Valormaximo)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
