# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Doorv2.ui'
#
# Created: Sun Jan 07 20:03:53 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cv2 as cv
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

    "总的ui界面 包含各个选项按钮和摄像头的预览"
class Ui_Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Ui_Dialog):
        Ui_Dialog.setObjectName(_fromUtf8("Ui_Dialog"))
        Ui_Dialog.setWindowModality(QtCore.Qt.NonModal)
        Ui_Dialog.setEnabled(True)
        Ui_Dialog.resize(800, 700)
        Ui_Dialog.setMinimumSize(QtCore.QSize(750, 640))
        Ui_Dialog.setMaximumSize(QtCore.QSize(800, 700))
        Ui_Dialog.setMouseTracking(False)
        Ui_Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Ui_Dialog.setAcceptDrops(False)
        Ui_Dialog.setAutoFillBackground(False)
        Ui_Dialog.setSizeGripEnabled(True)
        self.lcdNumber = QtGui.QLCDNumber(Ui_Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(470, 530, 221, 81))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setNumDigits(8)
        self.photo = QtGui.QLabel(Ui_Dialog)
        self.photo.setGeometry(QtCore.QRect(50, 40, 640, 480))
        self.photo.setMinimumSize(QtCore.QSize(640, 480))
        self.photo.setMaximumSize(QtCore.QSize(640, 480))
        self.photo.setText(_fromUtf8(""))
        self.photo.setObjectName(_fromUtf8("photo"))
        self.widget = QtGui.QWidget(Ui_Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 530, 421, 83))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.take_photo = QtGui.QPushButton(self.widget)
        self.take_photo.setEnabled(False)
        self.take_photo.setObjectName(_fromUtf8("take_photo"))
        self.gridLayout.addWidget(self.take_photo, 0, 1, 1, 1)
        self.preview = QtGui.QPushButton(self.widget)
        self.preview.setObjectName(_fromUtf8("preview"))
        self.gridLayout.addWidget(self.preview, 0, 0, 1, 1)
        self.up_load = QtGui.QPushButton(self.widget)
        self.up_load.setEnabled(False)
        self.up_load.setObjectName(_fromUtf8("up_load"))
        self.gridLayout.addWidget(self.up_load, 0, 2, 1, 1)
        self.add = QtGui.QPushButton(self.widget)
        self.add.setEnabled(False)
        self.add.setObjectName(_fromUtf8("add"))
        self.gridLayout.addWidget(self.add, 1, 0, 1, 1)
        self.identify = QtGui.QPushButton(self.widget)
        self.identify.setEnabled(False)
        self.identify.setObjectName(_fromUtf8("identify"))
        self.gridLayout.addWidget(self.identify, 1, 1, 1, 1)
        self.check = QtGui.QPushButton(self.widget)
        self.check.setEnabled(True)
        self.check.setObjectName(_fromUtf8("check"))
        self.gridLayout.addWidget(self.check, 1, 2, 1, 1)
        self.quit = QtGui.QPushButton(self.widget)
        self.quit.setObjectName(_fromUtf8("quit"))
        self.gridLayout.addWidget(self.quit, 2, 0, 1, 3)
        self.retranslateUi(Ui_Dialog)
        QtCore.QObject.connect(self.quit, QtCore.SIGNAL(_fromUtf8("clicked()")), Ui_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Ui_Dialog)
        self.face_ui.setModal(False)
        self.face_add.setModal(False)
    def retranslateUi(self, Ui_Dialog):
        Ui_Dialog.setWindowTitle(_translate("Ui_Dialog", "Door", None))
        self.take_photo.setText(_translate("Ui_Dialog", "拍照", None))
        self.preview.setText(_translate("Ui_Dialog", "预览", None))
        self.up_load.setText(_translate("Ui_Dialog", "上传", None))
        self.add.setText(_translate("Ui_Dialog", "添加", None))
        self.identify.setText(_translate("Ui_Dialog", "识别", None))
        self.quit.setText(_translate("Ui_Dialog", "关闭", None))
        self.check.setText(_translate("Ui_Dialog","查看",None))
    def __init__(self):
        super(Ui_Ui_Dialog, self).__init__()
        self.face_ui = Ui_face_feature()
        self.face_add = Ui_Add_Dialog()
        self.face_identify = Ui_identify()
        self.face_check = Ui_checkDialog()
        self.setupUi(self)
        self.retranslateUi(self)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._showtime)
        self._timer.start()
        self._showtime()
    def _showtime(self):
        self._timer = QtCore.QTime.currentTime()
        self._text = self._timer.toString("hh:mm:ss")
        self.lcdNumber.display(self._text)
    "弹出面部属性的对话框 包含一个messagebox对话框，通过在主程序中发送消息进行调用"
    def pop_up_msg(self,*result):
        if result[0]:
            button_ok = QtGui.QMessageBox.information(self,_translate("", "提示", None), _translate("", "上传成功", None))
            if button_ok == QtGui.QMessageBox.Ok:
                self.face_ui.age_2.setText(_translate("face_feature", str(int(result[0]['result'][0]['age'])), None))
                self.face_ui.beauty_2.setText(_translate("face_feature", str(int(result[0]['result'][0]['beauty'])), None))
                face_expression = {0:'不笑',1:'微笑',2:'大笑'}
                self.face_ui.expression_2.setText(_translate("face_feature",
                                                             face_expression[result[0]['result'][0]['expression']], None))
                face_glasses = {0:'不带眼镜',1:'普通眼镜',2:'墨  镜'}
                self.face_ui.glasses_2.setText(_translate("face_feature",
                                                          face_glasses[result[0]['result'][0]['glasses']],None))
                face_gender = {'male':'男','female':'女'}
                self.face_ui.gender_2.setText(_translate("face_feature",
                                                         face_gender[result[0]['result'][0]['gender']],None))
                face_shape = {'square':'方形脸','triangle':'三角形脸','oval':'椭圆形脸','heart':'心形脸','round':'圆形脸'}
                face_shape_recv = sorted(result[0]['result'][0]['faceshape'],
                                         key = lambda e:e['probability'],reverse= True)
                self.face_ui.faceshape_2.setText(_translate("face_feature",
                                                             face_shape[face_shape_recv[0]['type']],None))
                Frame_image = cv.imread(result[1])
                cropImg = Frame_image[result[0]['result'][0]['location']['top']:
                                      result[0]['result'][0]['location']['top'] + result[0]['result'][0]['location']['height'],
                          result[0]['result'][0]['location']['left']:
                          result[0]['result'][0]['location']['width'] + result[0]['result'][0]['location']['left']]
                cropImgRGB = cv.cvtColor(cropImg,cv.COLOR_BGR2RGB)
                Q_img = QtGui.QImage(cropImgRGB.data,cropImgRGB.shape[1],cropImgRGB.shape[0],QtGui.QImage.Format_RGB888)
                self.face_ui.photo.setPixmap(QtGui.QPixmap.fromImage(Q_img))
                self.face_ui.exec_()
        else:
            button_fail = QtGui.QMessageBox(QtGui.QMessageBox.Information,_translate("", "提示", None),
                                            _translate("", "上传失败", None))
            button_fail.setButtonText(QtGui.QMessageBox.Ok,_translate("", "确定", None))
            button_fail.exec_()
    "获取接收到的 人脸识别的结果，并将结果进行整理"
    def identify_msg(self,*result):
        name_str = result[0][0]['uid'].split('_')
        show_name = name_str[0]
        show_group = name_str[1]
        self.face_identify.name_show.setText(_fromUtf8(show_name))
        self.face_identify.group_show.setText(_fromUtf8(show_group))
        self.face_identify.exec_()
    "人脸识别失败进行弹出对话框"
    def identify_fail(self):
        button_fail = QtGui.QMessageBox(QtGui.QMessageBox.Information, _translate("", "提示", None),
                                        _translate("", "无此成员", None))
        button_fail.setButtonText(QtGui.QMessageBox.Ok, _translate("", "确定", None))
        button_fail.exec_()
    "添加人脸对话框"
    def face_add_show(self):
        self.face_add.exec_()
    "人脸查看，用于查看账号下所有的人脸存储结果"
    def face_check_show(self,*result):
        self.face_check.checktableWidget.setRowCount(result[0]['result_num'])
        num = 0
        for info in result[0]['result']:
            name_str = info['uid'].split('_')
            show_name = name_str[0]
            show_group = name_str[1]
            item = QtGui.QTableWidgetItem(str(num))
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            self.face_check.checktableWidget.setItem(num,0,item)
            item = QtGui.QTableWidgetItem(show_name)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            self.face_check.checktableWidget.setItem(num,1,item)
            item = QtGui.QTableWidgetItem(show_group)
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            self.face_check.checktableWidget.setItem(num,2,item)
            item = QtGui.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.face_check.checktableWidget.setItem(num,3,item)
            num = num + 1
        QtCore.QObject.connect(self.face_check.checktableWidget,QtCore.SIGNAL(_fromUtf8("cellChanged(int,int)")),self.face_check.checkboxstate)
        self.face_check.exec_()
        "这个应该没用到"
class MessageBoxDlg(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MessageBoxDlg, self).__init__(parent)
        self.setWindowTitle("Messagebox")
        self.label = QtGui.QLabel("About Qt MessageBox")
        questionButton = QtGui.QPushButton("Question")
        informationButton = QtGui.QPushButton("Information")
        warningButton = QtGui.QPushButton("Warning")
        criticalButton = QtGui.QPushButton("Critical")
        aboutButton = QtGui.QPushButton("About")
        aboutqtButton = QtGui.QPushButton("About Qt")
        customButton = QtGui.QPushButton("Custom")

        gridLayout = QtGui.QGridLayout(self)
        gridLayout.addWidget(self.label, 0, 0, 1, 2)
        gridLayout.addWidget(questionButton, 1, 0)
        gridLayout.addWidget(informationButton, 1, 1)
        gridLayout.addWidget(warningButton, 2, 0)
        gridLayout.addWidget(criticalButton, 2, 1)
        gridLayout.addWidget(aboutButton, 3, 0)
        gridLayout.addWidget(aboutqtButton, 3, 1)
        gridLayout.addWidget(customButton, 4, 0)
        self.connect(questionButton, QtCore.SIGNAL("clicked()"), self.slotQuestion)
        self.connect(informationButton, QtCore.SIGNAL("clicked()"), self.slotInformation)
        self.connect(warningButton, QtCore.SIGNAL("clicked()"), self.slotWarning)
        self.connect(criticalButton, QtCore.SIGNAL("clicked()"), self.slotCritical)
        self.connect(aboutButton, QtCore.SIGNAL("clicked()"), self.slotAbout)
        self.connect(aboutqtButton, QtCore.SIGNAL("clicked()"), self.slotAboutQt)
        self.connect(customButton, QtCore.SIGNAL("clicked()"), self.slotCustom)
    def slotQuestion(self):
        button = QtGui.QMessageBox.question(self, "Question",
                                      self.tr("end"),
                                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                                            QtGui.QMessageBox.Ok)
        if button == QtGui.QMessageBox.Ok:
            self.label.setText("Question button/Ok")
        elif button == QtGui.QMessageBox.Cancel:
            self.label.setText("Question button/Cancel")
        else:
            return

    def slotInformation(self):
        QtGui.QMessageBox.information(self, "Information",
                                self.tr("input"))
        self.label.setText("Information MessageBox")

    def slotWarning(self):
        button = QtGui.QMessageBox.warning(self, "Warning",
                                     self.tr("save or not"),
                                           QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel,
                                           QtGui.QMessageBox.Save)
        if button == QtGui.QMessageBox.Save:
            self.label.setText("Warning button/Save")
        elif button == QtGui.QMessageBox.Discard:
            self.label.setText("Warning button/Discard")
        elif button == QtGui.QMessageBox.Cancel:
            self.label.setText("Warning button/Cancel")
        else:
            return

    def slotCritical(self):
        QtGui.QMessageBox.critical(self, "Critical",
                             self.tr("error"))
        self.label.setText("Critical MessageBox")

    def slotAbout(self):
        QtGui.QMessageBox.about(self, "About", self.tr("about"))
        self.label.setText("About MessageBox")

    def slotAboutQt(self):
        QtGui.QMessageBox.aboutQt(self, "About Qt")
        self.label.setText("About Qt MessageBox")

    def slotCustom(self):
        customMsgBox = QtGui.QMessageBox(self)
        customMsgBox.setWindowTitle("Custom message box")
        lockButton = customMsgBox.addButton(self.tr("local"),
                                            QtGui.QMessageBox.ActionRole)
        unlockButton = customMsgBox.addButton(self.tr("release"),
                                              QtGui.QMessageBox.ActionRole)
        cancelButton = customMsgBox.addButton("cancel", QtGui.QMessageBox.ActionRole)

        customMsgBox.setText(self.tr("diy"))
        customMsgBox.exec_()

        button = customMsgBox.clickedButton()
        if button == lockButton:
            self.label.setText("Custom MessageBox/Lock")
        elif button == unlockButton:
            self.label.setText("Custom MessageBox/Unlock")
        elif button == cancelButton:
            self.label.setText("Custom MessageBox/Cancel")
"面部属性对话框"
class Ui_face_feature(QtGui.QDialog):
    def setupUi(self, face_feature):
        face_feature.setObjectName(_fromUtf8("face_feature"))
        face_feature.resize(421, 332)
        self.photo = QtGui.QLabel(face_feature)
        self.photo.setGeometry(QtCore.QRect(30, 40, 201, 211))
        self.photo.setObjectName(_fromUtf8("photo"))
        self.quit = QtGui.QPushButton(face_feature)
        self.quit.setGeometry(QtCore.QRect(270, 260, 111, 21))
        self.quit.setObjectName(_fromUtf8("quit"))
        self.widget = QtGui.QWidget(face_feature)
        self.widget.setGeometry(QtCore.QRect(270, 30, 111, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gender = QtGui.QLabel(self.widget)
        self.gender.setObjectName(_fromUtf8("gender"))
        self.gridLayout.addWidget(self.gender, 0, 0, 1, 1)
        self.beauty = QtGui.QLabel(self.widget)
        self.beauty.setObjectName(_fromUtf8("beauty"))
        self.gridLayout.addWidget(self.beauty, 2, 0, 1, 1)
        self.age = QtGui.QLabel(self.widget)
        self.age.setObjectName(_fromUtf8("age"))
        self.gridLayout.addWidget(self.age, 1, 0, 1, 1)
        self.gender_2 = QtGui.QLabel(self.widget)
        self.gender_2.setObjectName(_fromUtf8("gender_2"))
        self.gridLayout.addWidget(self.gender_2, 0, 1, 1, 1)
        self.faceshape_2 = QtGui.QLabel(self.widget)
        self.faceshape_2.setObjectName(_fromUtf8("faceshape_2"))
        self.gridLayout.addWidget(self.faceshape_2, 5, 1, 1, 1)
        self.beauty_2 = QtGui.QLabel(self.widget)
        self.beauty_2.setObjectName(_fromUtf8("beauty_2"))
        self.gridLayout.addWidget(self.beauty_2, 2, 1, 1, 1)
        self.glasses = QtGui.QLabel(self.widget)
        self.glasses.setObjectName(_fromUtf8("glasses"))
        self.gridLayout.addWidget(self.glasses, 4, 0, 1, 1)
        self.expression_2 = QtGui.QLabel(self.widget)
        self.expression_2.setObjectName(_fromUtf8("expression_2"))
        self.gridLayout.addWidget(self.expression_2, 3, 1, 1, 1)
        self.expression = QtGui.QLabel(self.widget)
        self.expression.setObjectName(_fromUtf8("expression"))
        self.gridLayout.addWidget(self.expression, 3, 0, 1, 1)
        self.age_2 = QtGui.QLabel(self.widget)
        self.age_2.setObjectName(_fromUtf8("age_2"))
        self.gridLayout.addWidget(self.age_2, 1, 1, 1, 1)
        self.faceshape = QtGui.QLabel(self.widget)
        self.faceshape.setObjectName(_fromUtf8("faceshape"))
        self.gridLayout.addWidget(self.faceshape, 5, 0, 1, 1)
        self.glasses_2 = QtGui.QLabel(self.widget)
        self.glasses_2.setObjectName(_fromUtf8("glasses_2"))
        self.gridLayout.addWidget(self.glasses_2, 4, 1, 1, 1)

        self.retranslateUi(face_feature)
        QtCore.QObject.connect(self.quit, QtCore.SIGNAL(_fromUtf8("clicked()")), face_feature.close)
        QtCore.QMetaObject.connectSlotsByName(face_feature)

    def retranslateUi(self, face_feature):
        face_feature.setWindowTitle(_translate("face_feature", "面部属性", None))
        self.photo.setText(_translate("face_feature", "", None))
        self.quit.setText(_translate("face_feature", "退出", None))
        self.gender.setText(_translate("face_feature", "性别：", None))
        self.beauty.setText(_translate("face_feature", "颜值：", None))
        self.age.setText(_translate("face_feature", "年龄：", None))
        self.gender_2.setText(_translate("face_feature", "", None))
        self.faceshape_2.setText(_translate("face_feature", "", None))
        self.beauty_2.setText(_translate("face_feature", "", None))
        self.glasses.setText(_translate("face_feature", "眼镜：", None))
        self.expression_2.setText(_translate("face_feature", "", None))
        self.expression.setText(_translate("face_feature", "表情：", None))
        self.age_2.setText(_translate("face_feature", "", None))
        self.faceshape.setText(_translate("face_feature", "脸型：", None))
        self.glasses_2.setText(_translate("face_feature", "", None))
    def __init__(self):
        #QtGui.QDialog.__init__()
        super(Ui_face_feature, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
"添加人脸对话框"
class Ui_Add_Dialog(QtGui.QDialog):
    def setupUi(self, Add_Dialog):
        Add_Dialog.setObjectName(_fromUtf8("Add_Dialog"))
        Add_Dialog.resize(314, 232)
        Add_Dialog.setMinimumSize(QtCore.QSize(314, 232))
        Add_Dialog.setMaximumSize(QtCore.QSize(314, 232))
        self.cancel = QtGui.QPushButton(Add_Dialog)
        self.cancel.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.ok = QtGui.QPushButton(Add_Dialog)
        self.ok.setEnabled(False)
        self.ok.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.ok.setDefault(False)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.layoutWidget = QtGui.QWidget(Add_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(72, 62, 177, 48))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.name = QtGui.QLabel(self.layoutWidget)
        self.name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name.setTextFormat(QtCore.Qt.AutoText)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName(_fromUtf8("name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.name)
        self.name_edit = QtGui.QLineEdit(self.layoutWidget)
        self.name_edit.setObjectName(_fromUtf8("name_edit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.name_edit)
        self.group = QtGui.QLabel(self.layoutWidget)
        self.group.setAlignment(QtCore.Qt.AlignCenter)
        self.group.setObjectName(_fromUtf8("group"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.group)
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)

        self.retranslateUi(Add_Dialog)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Add_Dialog.close)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Add_Dialog.quit)
        QtCore.QObject.connect(self.ok,QtCore.SIGNAL("clicked()"),Add_Dialog.close)
        QtCore.QObject.connect(self.name_edit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self._enable_ok)
        QtCore.QObject.connect(self.comboBox,QtCore.SIGNAL(_fromUtf8("activated(QString)")),self._enable_ok)
        QtCore.QMetaObject.connectSlotsByName(Add_Dialog)

    def retranslateUi(self, Add_Dialog):
        Add_Dialog.setWindowTitle(_translate("Add_Dialog", "添加", None))
        self.cancel.setText(_translate("Add_Dialog", "取消", None))
        self.ok.setText(_translate("Add_Dialog", "确定", None))
        self.name.setText(_translate("Add_Dialog", "姓名：", None))
        self.group.setText(_translate("Add_Dialog", "组别：", None))
        self.comboBox.setItemText(0, _translate("Add_Dialog", "Door201", None))
        self.comboBox.setItemText(1, _translate("Add_Dialog", "Door202", None))
        self.comboBox.setItemText(2, _translate("Add_Dialog", "Door203", None))
        self.comboBox.setItemText(3, _translate("Add_Dialog", "Door204", None))
    "使能确认按钮 槽函数"
    def _enable_ok(self):
        self.name_edit_text = str(self.name_edit.text()+'_'+self.comboBox.currentText())
        if self.name_edit_text :
            self.ok.setEnabled(True)
        else:
            self.ok.setEnabled(False)
    def __init__(self):
        super(Ui_Add_Dialog,self).__init__()
        self.setupUi(self)
    def show_msg(self):
        QtGui.QMessageBox.information(self,self.trUtf8("提示"),self.trUtf8("添加成功"))
    def quit(self):
        QtGui.QMessageBox.information(self,self.trUtf8("提示"),self.trUtf8("用户取消"))
"人脸识别对话框"
class Ui_identify(QtGui.QDialog):
    def setupUi(self, identify):
        identify.setObjectName(_fromUtf8("identify"))
        identify.resize(360, 200)
        identify.setMinimumSize(QtCore.QSize(360, 200))
        identify.setMaximumSize(QtCore.QSize(360, 200))
        self.pushButton = QtGui.QPushButton(identify)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("ok"))
        self.photo_show = QtGui.QLabel(identify)
        self.photo_show.setGeometry(QtCore.QRect(10, 40, 128, 96))
        self.photo_show.setObjectName(_fromUtf8("photo_show"))
        self.widget = QtGui.QWidget(identify)
        self.widget.setGeometry(QtCore.QRect(150, 50, 131, 36))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.name = QtGui.QLabel(self.widget)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName(_fromUtf8("name"))
        self.verticalLayout_2.addWidget(self.name)
        self.group = QtGui.QLabel(self.widget)
        self.group.setAlignment(QtCore.Qt.AlignCenter)
        self.group.setObjectName(_fromUtf8("group"))
        self.verticalLayout_2.addWidget(self.group)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.name_show = QtGui.QLabel(self.widget)
        self.name_show.setText(_fromUtf8(""))
        self.name_show.setAlignment(QtCore.Qt.AlignCenter)
        self.name_show.setObjectName(_fromUtf8("name_show"))
        self.verticalLayout_3.addWidget(self.name_show)
        self.group_show = QtGui.QLabel(self.widget)
        self.group_show.setText(_fromUtf8(""))
        self.group_show.setAlignment(QtCore.Qt.AlignCenter)
        self.group_show.setObjectName(_fromUtf8("group_show"))
        self.verticalLayout_3.addWidget(self.group_show)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.setModal(False)
        self.retranslateUi(identify)
        self.photo_show.setText(_fromUtf8(""))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), identify.close)
        QtCore.QMetaObject.connectSlotsByName(identify)

    def retranslateUi(self, identify):
        identify.setWindowTitle(_translate("identify", "识别结果", None))
        self.pushButton.setText(_translate("identify", "确认", None))
        self.photo_show.setText(_translate("identify", "TextLabel", None))
        self.name.setText(_translate("identify", "姓名：", None))
        self.group.setText(_translate("identify", "组别：", None))
    def __init__(self):
        super(Ui_identify,self).__init__()
        self.setupUi(self)
"查看人脸存储结果的对话框"
class Ui_checkDialog(QtGui.QDialog):
    def setupUi(self, checkDialog):
        checkDialog.setObjectName(_fromUtf8("checkDialog"))
        checkDialog.resize(400, 340)
        checkDialog.setMinimumSize(QtCore.QSize(400, 340))
        checkDialog.setMaximumSize(QtCore.QSize(500, 400))
        self.layoutWidget = QtGui.QWidget(checkDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 301, 241))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checktableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.checktableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checktableWidget.setFrameShape(QtGui.QFrame.Panel)
        self.checktableWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.checktableWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.checktableWidget.setShowGrid(True)
        self.checktableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.checktableWidget.setObjectName(_fromUtf8("checktableWidget"))
        self.checktableWidget.setColumnCount(4)
        self.checktableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.checktableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.checktableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.checktableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.checktableWidget.setHorizontalHeaderItem(3, item)
        self.checktableWidget.horizontalHeader().setVisible(True)
        self.checktableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.checktableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.checktableWidget.verticalHeader().setVisible(False)
        self.checktableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.checktableWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deleteButton = QtGui.QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.quitButton = QtGui.QPushButton(self.layoutWidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout.addWidget(self.quitButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(checkDialog)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), checkDialog.close)
        QtCore.QMetaObject.connectSlotsByName(checkDialog)

    def retranslateUi(self, checkDialog):
        checkDialog.setWindowTitle(_translate("checkDialog", "查看", None))
        item = self.checktableWidget.horizontalHeaderItem(0)
        item.setText(_translate("checkDialog", "序号", None))
        item = self.checktableWidget.horizontalHeaderItem(1)
        item.setText(_translate("checkDialog", "姓名", None))
        item = self.checktableWidget.horizontalHeaderItem(2)
        item.setText(_translate("checkDialog", "组别", None))
        item = self.checktableWidget.horizontalHeaderItem(3)
        item.setText(_translate("checkDialog", "删除", None))
        self.deleteButton.setText(_translate("checkDialog", "删除", None))
        self.quitButton.setText(_translate("checkDialog", "退出", None))
    def __init__(self):
        super(Ui_checkDialog,self).__init__()
        self.setupUi(self)
        self.checkedrow = {}
    def checkboxstate(self,checked_row,checked_col):
        if self.checktableWidget.item(checked_row,checked_col).checkState() == QtCore.Qt.Checked:
            self.checkedrow[checked_row] = True
        else:
            self.checkedrow[checked_row] = False





if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    face_idd = Ui_checkDialog()
    face_idd.checktableWidget.setRowCount(4)
    item = QtGui.QTableWidgetItem()
    item.setCheckState(QtCore.Qt.Unchecked)
    face_idd.checktableWidget.setItem(1, 3, item)
    face_idd.exec_()
    app.exec_()
