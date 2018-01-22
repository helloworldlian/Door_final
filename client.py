# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:46:20 2018
function 客户端主程序
@author: Mr.lian
"""
from preview import *
from Doorv2 import *
from face import *
import sys
import time
import threading
import os
class my_client(QtGui.QDialog):
    def __init__(self):
        super(my_client,self).__init__()
        self.ui = Ui_Ui_Dialog()
        self.per = Preview()
        self.face = Face_id()
        QtCore.QObject.connect(self.ui.preview, QtCore.SIGNAL("clicked()"), self._cam_preview)
        QtCore.QObject.connect(self.ui.take_photo,QtCore.SIGNAL("clicked()"),self._cam_takephoto)
        QtCore.QObject.connect(self.ui.up_load,QtCore.SIGNAL("clicked()"),self._face_detect)
        QtCore.QObject.connect(self.ui.quit, QtCore.SIGNAL("clicked()"), self._exit)
        QtCore.QObject.connect(self,QtCore.SIGNAL("Up_pop_msg"),self.ui.pop_up_msg)
        QtCore.QObject.connect(self,QtCore.SIGNAL("Identify_msg"),self.ui.identify_msg)
        QtCore.QObject.connect(self.ui.add,QtCore.SIGNAL("clicked()"),self.ui.face_add_show)
        QtCore.QObject.connect(self.ui.face_add.ok,QtCore.SIGNAL("clicked()"),self._face_add)
        QtCore.QObject.connect(self.ui.identify,QtCore.SIGNAL("clicked()"),self._face_identify)
        QtCore.QObject.connect(self.ui.check,QtCore.SIGNAL("clicked()"),self._face_check)
        QtCore.QObject.connect(self,QtCore.SIGNAL("Check_msg"),self.ui.face_check_show)
        QtCore.QObject.connect(self.ui.face_check.deleteButton,QtCore.SIGNAL("clicked()"),self._face_delete)
    def _cam_preview(self):
        if not self.per.pre_success:
            self.per.ShowwithMultiprocess()
            s_time = time.time()
            while not self.per.pre_success:
                if time.time()-s_time > 0.5:
                    print "camera open fail"
                    break
            if self.per.pre_success:
                self.ui.take_photo.setEnabled(True)
    def _cam_takephoto(self):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.per.take_photo = True
        finally:
            lock.release()
        s_time = time.time()
        while not self.per.photo_success:
            #print time.time() - s_time
            if time.time()-s_time > 0.5:
                print "take photo fail"
                break
        if self.per.photo_success:
            self.ui.up_load.setEnabled(True)
            self.ui.add.setEnabled(True)
            self.ui.identify.setEnabled(True)
            self.per.photo_success = False
            self.face.photo_name = self.per.photo_name
        png = QtGui.QPixmap(self.per.photo_name).scaled(self.ui.photo.width(),self.ui.photo.height())
        self.ui.photo.setPixmap(png)
    def _face_detect(self):
        result = self.face.face_detect()
        self.emit(QtCore.SIGNAL("Up_pop_msg"),result,self.per.photo_name)
    def _face_check(self):
        self.check_result = self.face.get_groupuser(self.face.group)
        self.emit(QtCore.SIGNAL("Check_msg"),self.check_result)
    def _face_add(self):
        result = self.face.face_add(self.face.group,self.ui.face_add.name_edit_text)
        if result:
            if len(result)==1:
                self.ui.face_add.show_msg()
    def _face_identify(self):
        result = self.face.face_recognize(self.face.group)
        if result['result']:
            if result['result'][0]['scores'][0]>90:
                self.emit(QtCore.SIGNAL("Identify_msg"), result['result'])
            else:
                self.ui.identify_fail()
        else:
            self.ui.identify_fail()
    def _face_delete(self):
        delete_data = []
        for data in self.ui.face_check.checkedrow:
            if self.ui.face_check.checkedrow[data] == True:
                delete_data.append(self.check_result['result'][data]['uid'])
        for uid in delete_data:
            self.face.del_user(uid)
        self.ui.face_check.close()
    def _exit(self):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.per.stop = True
        finally:
            lock.release()
        s_time = time.time()
        while not self.per.exit:
            if time.time()-s_time > 0.5:
                print "camera exit fail"
                break
        self.ui.close()
        for photo in self.per.history_photoname:
            os.remove(photo)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my = my_client()
    my.ui.show()
    sys.exit(app.exec_())



