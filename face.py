# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:46:20 2018
function 调用百度api
@author: Mr.lian
"""
from aip import AipFace
class Face_id(object):
    def __init__(self):
        "your baidu ai APP_ID"
        self.APP_ID = '********'
        "your baidu ai API_KEY"
        self.API_KEY = '***************'
        "your baidu ai SECRET_KEY"
        self.SECRET_KEY = '*******************'
        self.aipFace = AipFace(self.APP_ID,self.API_KEY,self.SECRET_KEY)
        self.photo_name = ''
        self.group = 'Door'
    def get_file_content(self):
        with open(self.photo_name,'rb') as fp:
            return fp.read()
    def get_file_constcontent(self):
        with open('me.jpg','rb') as fp:
            return fp.read()
    def face_detect(self):
        options = {
                'max_face_num':1,
                'face_fields':'age,beauty,expression,faceshape,gender,glasses'
                }
        result = self.aipFace.detect(self.get_file_content(), options)
        return result
    def face_add(self,group = 'Door',uid = '',user_info ='person'):
        result=  self.aipFace.addUser(uid,user_info,group,self.get_file_content())
        return result
    def face_recognize(self,group):
        options = {
            'user_top_num':1
        }
        result = self.aipFace.identifyUser(group,self.get_file_content(),options)
        print result
        return result
    def get_user(self,uid = 'mrlian_door201',group = 'Door'):
        result = self.aipFace.getUser(uid)
        print result
    def get_group(self,start = 0,num = 100):
        options = {
            'start':start,
            'num':num
        }
        result = self.aipFace.getGroupList(options)
        print result
    def get_groupuser(self,group = '1',start = 0,num = 100):
        options = {
            'start':start,
            'num':num
        }
        result = self.aipFace.getGroupUsers(group,options)
        return result
    def del_user(self,uid):
        result = self.aipFace.deleteUser(uid)
        return result


if __name__=='__main__':
    face = Face_id()
    face.get_group()
    face.get_groupuser('Door')
