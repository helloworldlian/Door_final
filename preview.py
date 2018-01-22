# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:46:20 2018
function 调用摄像头进行预览   摄像头采用单独的线程 进行图像的获取
@author: Mr.lian
"""
import cv2 as cv
import threading
import time
import os
from datetime import datetime
class Preview(object):
    def __init__(self):
        self.stop = False
        self.t_start = 0
        self.pre_success = False
        self.fps = 0
        self.camera = cv.VideoCapture(0)
        self.camera.set(3, 640)
        self.camera.set(4, 480)
        self.photo_name = ''
        "your path "
        self.__path = '*********'
        self.photo_success = False
        self.history_photoname = []
        #config to take photo
        self.take_photo = False
        self.exit = False
    def Show_video(self):
        lock = threading.Lock()
        while True:
            ret, frame = self.camera.read()
            #self.fps = self.fps + 1
            #sfps = self.fps / (time.time() - self.t_start)
            #cv.putText(frame,'FPS:'+str(int(sfps)),(10,10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            if ret:
                cv.imshow("Video",frame)
                self.pre_success = True
                lock.acquire()
                try:
                    if self.take_photo:
                        date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%ms')
                        self.photo_name = self.__path + date + '.jpg'
                        self.history_photoname.append(self.photo_name)
                        cv.imwrite(self.photo_name, frame)
                        self.photo_success = True
                        self.take_photo = False
                finally:
                    lock.release()
            key = cv.waitKey(1)
            if key == ord('q'):
                break
            if self.stop:
                self.exit = True
                break
        self.camera.release()
        cv.destroyAllWindows()
    def ShowwithMultiprocess(self):
        print threading.active_count()
        self.t_start = time.time()
        show_thread = threading.Thread(target= self.Show_video,name= "show")
        show_thread.start()
        #Show_thread.join()
    def Delete_photo(self):
        os.remove(self.photo_name)
    def Frame_face(self,area):
        Frame_image = cv.imread(self.photo_name)
        print(area)
        cropImg = Frame_image[area['top']:area['top']+area['height'],area['left']:area['width']+area['left']]
        cv.imshow('cropimage',cropImg)
        cv.waitKey(0)

