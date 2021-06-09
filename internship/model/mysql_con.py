'''
Author: YYB
Date: 2020-11-03 21:19:35
LastEditTime: 2020-11-05 20:21:46
'''
#encoding=utf-8
import MySQLdb
from apscheduler.schedulers.background import BackgroundScheduler

class sql():
    def __init__(self):
        self.db = MySQLdb.connect("120.78.162.170", "数据库用户名", "数据库密码", "internship", charset='utf8' )
        self.cursor = self.db.cursor()
        schedudler = BackgroundScheduler()
        schedudler.add_job(self.conn,'interval',seconds=7200)
        schedudler.start()
    
    def conn(self):
        self.db = MySQLdb.connect("120.78.162.170", "数据库用户名", "数据库密码", "internship", charset='utf8' )
        self.cursor = self.db.cursor()

    def createUser(self,stu,ID):
        sql_order = "INSERT INTO USER(stu,ID,email,name,School_TeacherDepartName,School_TeacherName,Tel,ShiXi_Company,ShiXi_Duty,ShiXi_Teacher,ShiXi_TeaTel,s1,s2,s3,longitude,latitude,type,body,content,switcher) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
        try:
            self.cursor.execute(sql_order,[stu,ID,'','','','','','','','','','','','','','','','','','0'])
            self.db.commit()
            print('创建新用户成功')
            return True
        except:
            print('创建新用户失败')
            return False

    def checkUser(self, stu, ID):
        sql_order = "SELECT * FROM user"
        query_flag = self.cursor.execute(sql_order)
        self.db.commit()
        sql_order = "SELECT * FROM user WHERE stu=(%s);"
        query_flag = self.cursor.execute(sql_order, [stu])
        self.db.commit()
        if query_flag:
            sql_order = "SELECT * FROM user WHERE stu=(%s) and ID=(%s);"
            exsit_flag = self.cursor.execute(sql_order, [stu, ID])
            self.db.commit()
            return exsit_flag
        else:
            return False
    
    def update(self, stu, email, name, School_TeacherDepartName, School_TeacherName, Tel, ShiXi_Company, ShiXi_Duty, ShiXi_Teacher, ShiXi_TeaTel, s1, s2, s3, longitude, latitude, _type, body, content, switcher):
        sql_order = "UPDATE user SET email=(%s),name=(%s),School_TeacherDepartName=(%s),School_TeacherName=(%s),Tel=(%s),ShiXi_Company=(%s),ShiXi_Duty=(%s),ShiXi_Teacher=(%s),ShiXi_TeaTel=(%s),s1=(%s),s2=(%s),s3=(%s),longitude=(%s),latitude=(%s),type=(%s),body=(%s),content=(%s),switcher=(%s) where stu=(%s);"
        try:
            self.cursor.execute(sql_order,[email,name,School_TeacherDepartName,School_TeacherName,Tel,ShiXi_Company,ShiXi_Duty,ShiXi_Teacher,ShiXi_TeaTel,s1,s2,s3,longitude,latitude,_type,body,content,switcher,stu])
            self.db.commit()
            return True
        except:
            return False
            
        

if __name__ == "__main__":
    mysql = sql()