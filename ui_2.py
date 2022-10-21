import PyQt5
import sys, os
import downloadFinal

from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QListWidget, QListWidgetItem, QPushButton, QFileDialog, \
    QGridLayout, QWidget, QTableWidget, QFrame, QHeaderView, QTableWidgetItem, QAbstractItemView, QScrollArea, \
    QVBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QUrl, QPropertyAnimation, QTimer

import similarity_algorithm
from similarity_algorithm import walk_dir

# Set scroll label to review check report
class ScrollLabel(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.label = QLabel(content)

        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.label.setWordWrap(True)

        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)

# Set the box of file list
class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(350, 500)
        self.folderPath = ''
        self.fileList = []
        self.label = QLabel('Upload or Drag a repository to check for plagiarism')
    # Set drag and drop event
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():

                if url.isLocalFile():
                    self.folderPath = str(url.toLocalFile())
                    for link in walk_dir(str(url.toLocalFile()))[0]:
                        if link != '.DS_Store':
                            links.append(link)
                            self.fileList.append(link)

            self.addItems(links)
            self.setAcceptDrops(False)

        else:
            event.ignore()

# the window of check report
class CheckPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.resize(900, 600)
        self.label = ScrollLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

# Set main page
class AppDemo(QWidget):
    # submitClicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.path = ''
        self.fileList = []
        self.layout = QGridLayout()
        self.bottom = QGridLayout()
        self.windowIndex = 0
        self.result = ()
        self.selectedFile = ''

        self.resize(700, 500)
        self.lstView = ListboxWidget(self)
        self.checkPage = CheckPage()
        self.layout.addWidget(self.lstView, 1, 0)
        self.btn = QPushButton('Upload', self)
        # self.btn.setStyleSheet("background-color: #349209;")
        # self.btn.setGeometry(400, 400, 150, 50)
        self.bottom.addWidget(self.btn, 0, 0)
        self.btn.clicked.connect(self.clicker)
        #
        self.btnCheck = QPushButton('Check', self)
        # self.btnCheck.setGeometry(400, 300, 150, 50)
        self.bottom.addWidget(self.btnCheck, 0, 1)
        self.btnCheck.clicked.connect(self.checkClick)

        self.btnCancel = QPushButton('Cancel', self)
        # self.btnCreate.setGeometry(400, 200, 150, 50)
        self.bottom.addWidget(self.btnCancel, 0, 2)
        self.btnCancel.clicked.connect(self.createWidget)

        self.layout.addLayout(self.bottom, 2, 0)
        self.setLayout(self.layout)

        # alert label
        self.label = QLabel(self)
        self.label.setText('Repo already uploaded')
        self.label.setAutoFillBackground(True)
        # set background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(141, 91, 153))
        self.label.setPalette(palette)
        # set opacity
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0)
        self.label.setGraphicsEffect(self.opacity)

        # self.draw()
    # label appear
    def draw(self):
        self.layout.addWidget(self.label, 0, 0)
        self.opacity.i = 1
        print(self.opacity.i)

        def timeout():  # set timeout, change opacity

            self.opacity.setOpacity(self.opacity.i / 100)
            self.label.setGraphicsEffect(self.opacity)
            # self.label.setGeometry(50, 50, 200, 200)
            self.opacity.i += 1
            if self.opacity.i >= 100:
                self.timer.stop()  # timer stop
                self.timer.deleteLater()


        self.timer = QTimer()
        self.timer.setInterval(10)  # Set time interval(ms)
        self.timer.timeout.connect(timeout)  # timeout slot
        self.timer.start()

    # label disappear
    def disappear(self):
        self.timer_1.stop()
        self.timer_1.deleteLater()
        # self.opacity.i = 1
        print('disappear')

        def remove():
            self.opacity.setOpacity(self.opacity.i / 100)
            self.label.setGraphicsEffect(self.opacity)
            # self.label.setGeometry(50, 50, 200, 200)
            # print('in')
            self.opacity.i = self.opacity.i - 1
            # print(self.opacity.i)
            if self.opacity.i == 0:
                self.timer_2.stop()  # timer stop
                self.timer_2.deleteLater()
                self.label.deleteLater()
                print(self.opacity.i)
                self.label = QLabel(self)
                self.label.setText('Repo already loaded')
                self.label.setAutoFillBackground(True)

                palette = QPalette()
                palette.setColor(QPalette.Window, QColor(141, 91, 153))
                self.label.setPalette(palette)

                self.opacity = QGraphicsOpacityEffect()
                self.opacity.setOpacity(0)
                self.label.setGraphicsEffect(self.opacity)

        self.timer_2 = QTimer()
        self.timer_2.setInterval(10)  # Set time interval(ms)
        self.timer_2.timeout.connect(remove)  # timeout slot
        self.timer_2.start()


    # label in and out
    def in_out(self):

        self.draw()
        self.timer_1 = QTimer()
        self.timer_1.setInterval(1200)
        self.timer_1.start()
        self.timer_1.timeout.connect(self.disappear)






    # upload file
    def clicker(self):
        fname = QFileDialog.getExistingDirectory(self, "Upload Folder")
        if self.lstView.folderPath == '' and self.path == '' and fname:
            self.path = fname
            print(fname)
            for i in walk_dir(fname)[0]:
                if i != '.DS_Store':
                    self.fileList.append(i)
            self.lstView.addItems(self.fileList)

            self.lstView.setAcceptDrops(False)
        else:
            self.in_out()
    # call plagiarism check algorithm
    def checkClick(self):
        if self.path == '':
            self.path = self.lstView.folderPath
            self.fileList = self.lstView.fileList
        if self.path != '':
            if self.fileList[0].endswith(".py"):
                result = similarity_algorithm.check_python(self.path + '/')
            elif self.fileList[0].endswith(".java"):
                print(2)
                result = similarity_algorithm.check_java(self.path + '/')
                print(1)
            elif self.fileList[0].endswith(".php"):
                result = similarity_algorithm.check_PHP(self.path + '/')
            elif self.fileList[0].endswith(".txt"):
                result = similarity_algorithm.check_sql(self.path + '/')
            elif self.fileList[0].endswith(".cpp"):
                result = similarity_algorithm.check_cpp(self.path + '/')
            self.result = result
            # print(result)
            # print(self.layout.itemAt(0))
            # self.layout.itemAt(self.windowIndex).widget().deleteLater()
            self.lstView.deleteLater()

            self.tableWidget = QTableWidget(len(self.fileList), 2)
            self.tableWidget.setFrameShape(QFrame.NoFrame)
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            self.tableWidget.setHorizontalHeaderLabels(['File Name', 'Similarity Rate'])

            counter = 0
            for i in result[0].keys():
                item = QTableWidgetItem(i)
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(counter, 0, item)
                # tableWidget.setItem(counter, 0, QTableWidgetItem(i))
                percentage = round(float(result[0][i]), 4)
                percentage = round(percentage * 100, 2)
                item_1 = QTableWidgetItem(str(percentage) + '%')
                if percentage < 30:
                    item_1.setForeground(QBrush(QColor(0, 255, 0)))
                elif percentage < 50:
                    item_1.setForeground(QBrush(QColor(255, 69, 0)))
                else:
                    item_1.setForeground(QBrush(QColor(255, 0, 0)))

                item_1.setTextAlignment(Qt.AlignCenter)

                self.tableWidget.setItem(counter, 1, QTableWidgetItem(item_1))
                counter = counter + 1
            # tableWidget.setStyleSheet('color:green;')
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)
            self.layout.addWidget(self.tableWidget, 0, 0)

            self.btn.setText('Download Report')
            self.btnCheck.setText('Check Report')
            self.btnCheck.clicked.disconnect()
            self.btnCheck.clicked.connect(self.checkReport)
    # click report
    def on_selectionChanged(self, selected, deselected):

        for i in selected.indexes():
            # print(i.row(), i.column())
            self.selectedFile = self.fileList[i.row()]
    # a new window to review report
    def checkReport(self):
        l = downloadFinal.download.trans(self.path, self.fileList, self.selectedFile, self.result
                                         )
        # print(l)
        # self.submitClicked.emit(l)
        w = self.checkPage
        text = ''
        for t in l[0]:
            text = text + t
        print(text)
        w.label.setText(text)
        w.show()
    # clean up
    def createWidget(self):
        try:
            item_list = list(range(self.layout.count()))
            for i in item_list:
                item = self.layout.itemAt(i)
                if item.widget() is not None:
                    self.layout.itemAt(i).widget().deleteLater()
                    if i == 0:
                        self.windowIndex = 0
                    else:
                        self.windowIndex = 1

            self.lstView = ListboxWidget(self)
            self.layout.addWidget(self.lstView, 1, 0)
            self.path = ''
            self.fileList = []

            self.btn.setText('Upload')
            self.btnCheck.setText('Check')
            self.btnCheck.disconnect()
            self.btnCheck.clicked.connect(self.checkClick)





        except:
            print(self.layout.itemAt(2))


app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())
