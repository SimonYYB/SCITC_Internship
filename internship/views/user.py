#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate, login, logout #user django already has auth
import json
import os
from model.mysql_con import sql
from model.teacher import teacher
from model.info import info
from model.bind import bind

mysql = sql()
myteacher = teacher()
myinfo = info()
mybind = bind()
def user_logout(request):
    logout(request)
    return redirect('/')

def user_info(request):
    try:
        is_login = request.session['username']
    except:
        return redirect('/')
    content = {}
    sql_order = "select * from user where stu={stu}".format(stu=request.session['username'])
    query_flag = mysql.cursor.execute(sql_order)
    if query_flag:
        ret = mysql.cursor.fetchone()
        key = ('stu', 'ID', 'email', 'name', 'School_TeacherDepartName', 'School_TeacherName', 'Tel', 'ShiXi_Company', 'ShiXi_Duty', 'ShiXi_Teacher', 'ShiXi_TeaTel', 's1', 's2', 's3', 'longitude', 'latitude', 'type', 'body', 'cont', 'switcher')
        for i,j in zip(key,ret):
            content[i] = j
    # print("content:",content)
    return render(request,'user.html',content)

def user_update(request):
    if request.method == 'POST' and request.session['is_login']:
        print('update')
        res_text = ""
        stu = request.session['username']
        ID = request.session['password']
        name = request.POST.get('name')
        email = request.POST.get('email')
        School_TeacherDepartName = request.POST.get('School_TeacherDepartName')
        School_TeacherName = request.POST.get('School_TeacherName')
        Tel = request.POST.get('Tel')
        ShiXi_Company = request.POST.get('ShiXi_Company')
        ShiXi_Duty = request.POST.get('ShiXi_Duty')
        ShiXi_Teacher = request.POST.get('ShiXi_Teacher')
        ShiXi_TeaTel = request.POST.get('ShiXi_TeaTel')
        s1 = request.POST.get('s1')
        s2 = request.POST.get('s2')
        s3 = request.POST.get('s3')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        _type = request.POST.get('type')
        body = request.POST.get('body')
        cont = request.POST.get('cont')
        switcher = request.POST.get('switcher')
        print([stu,email,name,School_TeacherDepartName,School_TeacherName,Tel,ShiXi_Company,ShiXi_Duty,ShiXi_Teacher,ShiXi_TeaTel,s1,s2,s3,longitude,latitude,_type,body,cont,switcher])
        flag_update = mysql.update(stu, email, name, School_TeacherDepartName, School_TeacherName, Tel, ShiXi_Company, ShiXi_Duty, ShiXi_Teacher, ShiXi_TeaTel, s1, s2, s3, longitude, latitude, _type, body, cont, switcher)
        if School_TeacherDepartName and School_TeacherName:
            teacher_flag = myteacher.bind_teacher(stu, School_TeacherDepartName, School_TeacherName)
            if teacher_flag:
                res_text = res_text + "<br>选择指导老师成功"
            else:
                res_text = res_text + "<br>选择指导老师失败"
                bind_flag = mybind.do_bind(stu,ID,False)
                if bind_flag:
                    res_text = res_text + "<br>重新绑定成功"
                else:
                    res_text = res_text + "<br>重新绑定失败"
                    
        if Tel and ShiXi_Company and ShiXi_Duty and ShiXi_Teacher and ShiXi_TeaTel and s1 and s2 and s3:
            info_flag = myinfo.do_info(stu, Tel, ShiXi_Company, ShiXi_Duty, ShiXi_Teacher, ShiXi_TeaTel, s1, s2, s3)
            if info_flag:
                res_text = res_text + "<br>信息修改成功"
            else:
                res_text = res_text + "<br>信息修改失败"
                bind_flag = mybind.do_bind(stu,ID,False)
                if bind_flag:
                    res_text = res_text + "<br>重新绑定成功"
                else:
                    res_text = res_text + "<br>重新绑定失败"

        if flag_update:
            res_text = "更新成功" + res_text
            return HttpResponse(json.dumps(res_text), content_type="application/json,charset=utf-8")
        else:
            res_text = "更新失败" + res_text
            return HttpResponse(json.dumps(res_text), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse(json.dumps("违规请求"), content_type="application/json,charset=utf-8")
