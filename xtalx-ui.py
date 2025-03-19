from PyQt5 import QtCore, QtGui, QtWidgets
import glotlib
import numpy as np
import math
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from OpenGL import GL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QTabWidget::tabWidget {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabWidget::tab {\n"
"    background-color: #000000;  /* Tab background color */\n"
"    color: white;               /* Tab text color */\n"
"    padding: 10px;              /* Padding for the tab */\n"
"}\n"
"\n"
"QTabWidget::tab:selected {\n"
"    background-color: #2ecc71;  /* Selected tab background color */\n"
"    color: white;               /* Selected tab text color */\n"
"}\n"
"\n"
"QTabWidget::tab:hover {\n"
"    background-color: #2980b9;  /* Tab hover background color */\n"
"}\n"
"\n"
"QTabWidget::tab_2 {\n"
"    background-color: #000000;  /* Tab background color */\n"
"    color: white;               /* Tab text color */\n"
"    padding: 10px;              /* Padding for the tab */\n"
"}\n"
"\n"
"QTabWidget::tab_2:selected {\n"
"    background-color: #2ecc71;  /* Selected tab background color */\n"
"    color: white;               /* Selected tab text color */\n"
"}\n"
"\n"
"QTabWidget::tab_2:hover {\n"
"    background-color: #2980b9;  /* Tab hover background color */\n"
"}\n"
"\n"
"QTabWidget::tab_3 {\n"
"    background-color: #000000;  /* Tab background color */\n"
"    color: white;               /* Tab text color */\n"
"    padding: 10px;              /* Padding for the tab */\n"
"}\n"
"\n"
"QTabWidget::tab_3:selected {\n"
"    background-color: #2ecc71;  /* Selected tab background color */\n"
"    color: white;               /* Selected tab text color */\n"
"}\n"
"\n"
"QTabWidget::tab_3:hover {\n"
"    background-color: #2980b9;  /* Tab hover background color */\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 900, 825))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.plots = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.plots.setFont(font)
        self.plots.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plots.setAcceptDrops(False)
        self.plots.setObjectName("plots")
        self.glotlibWidget = glotlibWidget(self.plots)
        self.glotlibWidget.setGeometry(QtCore.QRect(0, 35, 900, 700))
        self.glotlibWidget.setObjectName("glotlibWidget")
        self.saveButton = QtWidgets.QPushButton(self.plots)
        self.saveButton.setGeometry(QtCore.QRect(725, 748, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.saveButton.setStyleSheet("")
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSave")
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QtCore.QSize(20, 20))
        self.saveButton.setObjectName("saveButton")
        self.serialNum = QtWidgets.QLabel(self.plots)
        self.serialNum.setGeometry(QtCore.QRect(10, 6, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.serialNum.setFont(font)
        self.serialNum.setObjectName("serialNum")
        self.serialPlace = QtWidgets.QLabel(self.plots)
        self.serialPlace.setGeometry(QtCore.QRect(120, 6, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.serialPlace.setFont(font)
        self.serialPlace.setObjectName("serialPlace")
        self.tabWidget.addTab(self.plots, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.tabWidget.addTab(self.about, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.tabWidget.addTab(self.settings, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "xtalx"))
        self.saveButton.setText(_translate("MainWindow", "Save as CSV File"))
        self.serialNum.setText(_translate("MainWindow", "Serial Number:"))
        self.serialPlace.setText(_translate("MainWindow", "Place Holder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plots), _translate("MainWindow", "Plots"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "About"))


NVERTICES = 500

BOUNDS = [312, 313]
COLORS = [
    (0.8, 0.2, 0, 1),
    (0.8, 0, 0.2, 1),
]
AMP_RATES = [3.5, 0.35]

class glotlibWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(glotlibWidget, self).__init__(parent)
        fmt = QSurfaceFormat()
        fmt.setVersion(3, 3)
        fmt.setProfile(QSurfaceFormat.CoreProfile)
        QSurfaceFormat.setDefaultFormat(fmt)
        self.setFormat(fmt)

        
    def initializeGL(self):
        self.makeCurrent()
        GL.glClearColor(1, 1, 1, 0)
        print(GL.glGetString(GL.GL_VERSION))
        print(self.width, self.height)

        glotlib.programs.load()
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

    def paintGL(self):
        # Mandatory Field 
        self.width = 900
        self.height = 700
        self.makeCurrent()
        glotlib.main.draw_contexts(0)

        Xi = np.arange(NVERTICES) * 2 * math.pi / (NVERTICES - 1)
        Xs = [ar * Xi for ar in AMP_RATES]


        w = glotlib.Context(self.width,self.height,name="name",msaa=2)

        # Draw a circle in the top plot.
        p = w.add_plot(311, limits=(-1, -1, 1, 1), aspect=glotlib.ASPECT_SQUARE)
        T = np.linspace(0, 2 * math.pi, num=NVERTICES, endpoint=False)
        p.add_hline(0, color=(0.5, 0.75, 0.5, 1))
        p.add_hline(1, color=(0.5, 0.75, 0.5, 1))
        p.add_hline(-1, color=(0.5, 0.75, 0.5, 1))
        p.add_vline(0, color=(0.5, 0.75, 0.5, 1))
        p.add_vline(1, color=(0.5, 0.75, 0.5, 1))
        p.add_vline(-1, color=(0.5, 0.75, 0.5, 1))
        p.add_lines(X=np.cos(T), Y=np.sin(T), color=(0, 0.8, 0.2, 1), width=1,
                    point_width=3)

        # Draw sine waves in the next two plots.
        for bounds, color, X in zip(BOUNDS, COLORS, Xs):
            p = w.add_plot(bounds, limits=(0, -1, 2 * math.pi, 1))
            p.add_lines(X=Xi, Y=np.sin(X), color=color, width=1, point_width=3)

        

    def resizeGL(self, w, h):
        GL.glViewport(0,0,w,h)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
