'''
Author: your name
Date: 2020-11-03 21:19:35
LastEditTime: 2020-11-05 00:30:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \campushoy\views\scitc_cam_login.py
'''
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
from model.mysql_con import sql
from model.bind import bind
import json

mysql = sql()
mybind = bind()
def mylogin(request):
    is_login = False
    try:
        is_login = request.session['username']
    except:
        pass
    if is_login:
         return redirect('/user')
    if(request.method == 'POST'):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print(username, password)
        login_flag = mysql.checkUser(username,password)
        if login_flag:
            request.session['username'] = username
            request.session['password'] = password
            request.session['is_login'] = True
            return HttpResponse(json.dumps(1), content_type="application/json,charset=utf-8")
        else:
            bind_flag = mybind.do_bind(username, password)
            if bind_flag:
                request.session['username'] = username
                request.session['password'] = password
                request.session['is_login'] = True
                return HttpResponse(json.dumps(1), content_type="application/json,charset=utf-8")
            else:
                return HttpResponse(json.dumps(0), content_type="application/json,charset=utf-8")   
    else:
        return render(request,'index.html')
