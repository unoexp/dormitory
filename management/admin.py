from django.contrib import admin
from .models import *


# Register your models here.
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('宿舍楼号', '宿管姓名', '宿管电话')
    search_fields = ['宿舍楼号']


class RoomAdmin(admin.ModelAdmin):
    list_display = ('寝室号', '宿舍楼号', '水费余额', '电费余额', '入住人数')
    search_fields = ['寝室号']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('学号', '姓名', '性别', '密码', '寝室号', '联系方式', '专业班级', '违纪信息')
    search_fields = ['学号', '姓名']


class RepairAdmin(admin.ModelAdmin):
    list_display = ('工号', '姓名', '性别', '联系方式')
    search_fields = ['工号', '姓名']


class RepairRegionAdmin(admin.ModelAdmin):
    list_display = ('工号', '宿舍楼号')
    search_fields = ['工号', '宿舍楼号']


class DepositAdmin(admin.ModelAdmin):
    list_display = ('充值类型', '充值金额')


class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('寝室号', '工号', '报修信息', '日期')
    search_fields = ['寝室号', '工号']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('访客姓名', '性别', '联系方式')
    search_fields = ['访客姓名']


class VistAdmin(admin.ModelAdmin):
    list_display = ('访问原因', '访问日期')


admin.site.site_header = '学生宿舍管理'

admin.site.register(宿舍楼, BuildingAdmin)
admin.site.register(寝室, RoomAdmin)
admin.site.register(学生, StudentAdmin)
admin.site.register(维修人员, RepairAdmin)
admin.site.register(维修人员负责区域, RepairRegionAdmin)
admin.site.register(充值记录, DepositAdmin)
admin.site.register(报修记录, RepairRequestAdmin)
admin.site.register(访客, VisitorAdmin)
admin.site.register(访问, VistAdmin)