from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from management import models

from django.http import HttpResponse,HttpResponseRedirect
from django import forms

from django.views.generic import ListView
# Create your views here.




def index(request):
    if not request.session.get('is_login', None):
        return redirect('/student/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:  # 确保用户名和密码都不为空
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.Student.objects.get(student_id=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html',{'message': message})
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.student_id
                request.session['user_name'] = user.student_name
                request.session['user_room'] = user.student_room

                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})

    return render(request, 'login/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            message = '两次输入密码不相同'
            return render(request, 'login/register.html', {'message': message})
        try:
            models.Student.objects.get(student_id=username)
            message = '学号已注册'
            return render(request, 'login/register.html', {'message': message})
        except:
            obj = { 'student_name': username,
                    'student_sex' : 'male',
                    'student_id'  : username,
                    'password'    : password,
                    'student_building_id' :'1',
                    'student_room_id' : '1'
            }
            models.Student.objects.create(** obj)
            print('ok')
            message = '注册成功'
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/student/")
    request.session.flush()
    return redirect("/student/")

def info(request):
    mistake = request.session.get('user_id')
    mistake_list = models.Mistake.objects.filter(mistake_id=mistake)
    return render(request,'login/info.html',{"mistake_list": mistake_list})

def pay(request):
    room = request.session.get('user_room')
    message = ''
    if request.method == "POST":
        try:
            water = float(eval(request.POST.get('water')))
        except:
            water = 0
        try:
            elec = float(eval(request.POST.get('elec')))
        except:
            elec = 0
        try:
            obj = models.Room.objects.get(room_id=room)
            obj.room_water = obj.room_water + water
            obj.room_electricity = obj.room_electricity + elec
            obj.save()
            message = "缴费成功"
        except:
            message = "缴费失败"
    resources_list = models.Room.objects.filter(room_id=room)
    return render(request,'login/pay.html',{"resources_list":resources_list, "message":message})

def repair(request):
    return render(request,'login/repair.html')

def pw(request):
    uid = request.session.get('user_id')
    user = models.Student.objects.filter(student_id=uid)
    if request.method == "POST":
    # 判断两次密码是否一致
        message = '请检查填写的内容！'
        pwd1 = request.POST.get('pw1','')  # 与html中name值一样
        pwd2 = request.POST.get('pw2','')  # 与html中name值一样
        if pwd1 != pwd2:
            message = '密码不正确！'
            return render(request, 'login/pw.html', {'message': message})
        # 密码加密保存
        else:
            user.update(password = pwd1)
            message = '密码修改成功'
            return render(request, 'login/pw.html', {'message': message})
    return render(request,'login/pw.html')





# class InfoListView(ListView):
#     """通用视图"""
#     models = Mistake    #指定类
#     context_object_name = 'mistake'    #courses被传到模板中
#     template_name = "student/info.html"  #渲染页面

