from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyperclip



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 490)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 180, 241, 31))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 210, 241, 31))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 60, 231, 31))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(110, 60, 61, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:gen())
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 391, 41))
        self.pushButton.setStyleSheet("background-color: rgb(224, 255, 251);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(224, 255, 251, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: copy())
        self.pushButton_2.setGeometry(QtCore.QRect(20, 340, 181, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(224, 255, 251);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(224, 255, 251, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:save())
        self.pushButton_3.setGeometry(QtCore.QRect(230, 340, 181, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(224, 255, 251);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(224, 255, 251, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 390, 411, 91))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 411, 91))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setScaledContents(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 381, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


# creating variables for password 
        self.alphalower="abcdefghijklmnopqrstuvwxyz"
        self.alphaupper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.number="0123456789"
        self.char="!”#$%&'()*+,-./:;<=>?@[]^_`{|}~"
        self.choice=""
        self.passw=""


        # function for genarating password
        def gen():
            self.label_4.setText("")
            self.choice=""
            self.passw=""

            if self.checkBox.isChecked()==True:
                self.choice +=self.alphalower
            if self.checkBox_2.isChecked()==True:
                self.choice +=self.number
            if self.checkBox_3.isChecked()==True:
                self.choice +=self.alphaupper
            if self.checkBox_4.isChecked()==True:
                self.choice +=self.char

            try:
                for i in range(self.spinBox.value()):
                    self.passw+=random.choice(list(self.choice))
                self.label_4.setText(self.passw)

            except:
                self.label_4.setText("choose a checkbox please !!!!")



        # function for copying password
        def copy():
            pyperclip.copy(self.passw)

        
        # function for saving password
        def save():
            with open("password.txt","w") as p:
                p.write(self.passw)



                
        # connect slider and spinbox
        self.horizontalSlider.valueChanged.connect(lambda:sliderValueChange())
        self.spinBox.valueChanged.connect(lambda:spinboxValueChange())

        def sliderValueChange():
            # connect slider
            self.spinBox.setValue(self.horizontalSlider.value())


            # change security label 
            if  5<self.horizontalSlider.value()<11 :
                self.label.setText("security : NORMAL")
                self.label.setStyleSheet("background-color: white;font: bold 16px")
            if  6>self.horizontalSlider.value() :
                    self.label.setText("security : WEAK ")
                    self.label.setStyleSheet("background-color: red ;font: bold 16px")
            if  self.horizontalSlider.value()>10 :
                    self.label.setText("security : STRONG ")
                    self.label.setStyleSheet("background-color: green; font: bold 16px")

        

        def spinboxValueChange():
            # connect slider
            self.horizontalSlider.setValue(self.spinBox.value())


            # change security label 
            if  5<self.spinBox.value()<11 :
                self.label.setText("security : NORMAL")
                self.label.setStyleSheet("background-color: white ;font: bold 16px")
            if  6>self.spinBox.value() :
                    self.label.setText("security : WEAK ")
                    self.label.setStyleSheet("background-color: red ;font: bold 16px")
            if  self.spinBox.value()>10 :
                    self.label.setText("security : STRONG ")
                    self.label.setStyleSheet("background-color: green ; font: bold 16px")






        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.checkBox.setText(_translate("MainWindow", "alphabet (lower case)"))
        self.checkBox_2.setText(_translate("MainWindow", "number"))
        self.checkBox_3.setText(_translate("MainWindow", "alphabet (upper case)"))
        self.checkBox_4.setText(_translate("MainWindow", "character"))
        self.label_2.setText(_translate("MainWindow", "lenght : "))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.pushButton_2.setText(_translate("MainWindow", "copy"))
        self.pushButton_3.setText(_translate("MainWindow", "save to file"))
        self.label_3.setText(_translate("MainWindow", "create your password"))
        self.label_4.setText(_translate("MainWindow", "your password : "))
        self.label.setText(_translate("MainWindow", "security : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
