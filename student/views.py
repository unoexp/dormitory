import datetime

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from management import models

from django.http import HttpResponse, HttpResponseRedirect
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
            try:
                user = models.学生.objects.get(学号=username)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})
            if user.密码 == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.学号
                request.session['user_name'] = user.姓名
                request.session['user_room'] = user.寝室号

                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})

    return render(request, 'login/login.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        sex = request.POST.get('sex')
        d_id = request.POST.get('dormitory_num')
        tel = request.POST.get('phone')
        if password != password2:
            message = '两次输入密码不相同'
            return render(request, 'login/register.html', {'message': message})
        try:
            models.学生.objects.get(学号=username)
            message = '学号已注册'
            return render(request, 'login/register.html', {'message': message})
        except:
            try:
                models.寝室.objects.get(寝室号=d_id)
            except:
                obj = {
                    '寝室号': d_id,
                    '水费余额': 0,
                    '电费余额': 0,
                    '入住人数': 1
                }
                models.寝室.objects.create(**obj)
            d = models.寝室.objects.get(寝室号=d_id)
            obj = {'姓名': name,
                   '性别': sex,
                   '学号': username,
                   '密码': password,
                   '联系方式':tel,
                   '寝室号': d
                   }
            models.学生.objects.create(**obj)
            message = '注册成功'
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/student/")
    request.session.flush()
    return redirect("/student/")


def info(request):
    mistake = request.session.get('user_id')
    mistake_list = models.学生.objects.filter(学号=mistake)
    return render(request,'index/info.html', {"mistake_list": mistake_list})

def pay(request):
    room = request.session.get('user_room')
    message = ''
    if request.method == 'POST':
        try:
            water = float(eval(request.POST.get('water')))
        except:
            water = 0
        try:
            elec = float(eval(request.POST.get('elec')))
        except:
            elec = 0
        try:
            obj = models.寝室.objects.get(寝室号=room)
            obj.水费余额 += water
            obj.电费余额 += elec
            obj.save()
            if water > 0:
                obj = {
                    '充值类型': '水费余额',
                    '充值金额': water
                }
                models.充值记录.objects.create(**obj)
            if elec > 0:
                obj = {
                    '充值类型': '电费余额',
                    '充值金额': elec
                }
                models.充值记录.objects.create(**obj)
            message = "缴费成功"
        except:
            message = "缴费失败"
    resources_list = models.寝室.objects.filter(寝室号=room)
    return render(request, 'index/pay.html', {"resources_list": resources_list, "message": message})


def repair(request):
    room = request.session.get('user_room')
    message = ''
    if request.method == 'POST':
        obj = {
            "报修信息": request.POST.get('optionsRadios') + request.POST.get('data'),
            "日期": datetime.datetime.now(),
            "寝室号": room
        }
        models.报修记录.objects.create(**obj)
        message = "提交成功"
    return render(request, 'index/repair.html', {"message": message})


def pw(request):
    uid = request.session.get('user_id')
    user = models.学生.objects.filter(学号=uid)
    if request.method == "POST":
        # 判断两次密码是否一致
        message = '请检查填写的内容！'
        pwd1 = request.POST.get('pw1', '')  # 与html中name值一样
        pwd2 = request.POST.get('pw2', '')
        if pwd1 != pwd2:
            message = '密码不正确！'
            return render(request, 'index/pw.html', {'message': message, 'info': user})
        else:
            user.update(密码=pwd1)
            message = '密码修改成功'
            return render(request, 'index/pw.html', {'message': message, 'info': user})
    return render(request, 'index/pw.html', {'info': user})

def change_info(request):
    uid = request.session.get('user_id')
    user = models.学生.objects.filter(学号=uid)
    if request.method == "POST":
        name = request.POST.get('name')
        id = request.POST.get('username')
        d_id = request.POST.get('dormitory_num')
        tel = request.POST.get('phone')
        try:
            user.update(寝室号=d_id)
        except:
            message = '寝室不存在'
            return render(request, 'index/pw.html', {'message': message, 'info': user})
        user.update(联系方式=tel)
        request.session['user_room'] = d_id
        message = '信息修改成功'
        return render(request, 'index/pw.html', {'message': message, 'info': user})
    return render(request, 'index/pw.html', {'info': user})

def dormitory(request):
    request.session.flush
    room = request.session.get('user_room')
    data_list = models.学生.objects.filter(寝室号=room)
    return render(request, 'index/dormitory.html', {'data_list': data_list})

def visit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        rea = request.POST.get('rea')
        date = request.POST.get('date')
        sex = request.POST.get('sex')
        obj = {
            '访客姓名': name,
            '性别': sex,
            '联系方式': tel
        }
        models.访客.objects.create(**obj)
        obj = {
            '访问原因': rea,
            '访问日期': date
        }
        models.访问.objects.create(**obj)
        message = '提交成功'
        return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/visit.html')