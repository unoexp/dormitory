import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class Mistake(models.Model):
#     mistake_id = models.ForeignKey(to='Student',verbose_name=' 学号',on_delete=models.CASCADE)
#     case = models.CharField(max_length=100,verbose_name='违纪原因')
#     date = models.DateTimeField('违纪时间')
#     class Meta:
#         verbose_name='违纪信息'
#         verbose_name_plural='违纪信息'
#

class 宿舍楼(models.Model):
    宿舍楼号 = models.CharField(max_length=128, verbose_name="宿舍楼号", primary_key=True)
    宿管姓名 = models.CharField(max_length=128, verbose_name='宿管姓名')
    宿管电话 = models.CharField(max_length=128, verbose_name='宿管电话')

    class Meta:
        verbose_name = '宿舍楼'
        verbose_name_plural = '宿舍楼'

    def __str__(self):
        return self.宿舍楼号


class 寝室(models.Model):
    寝室号 = models.CharField(max_length=128, verbose_name='寝室号', primary_key=True)
    宿舍楼号 = models.ForeignKey(to="宿舍楼", verbose_name='宿舍楼号', on_delete=models.CASCADE, null=True)
    水费余额 = models.FloatField(verbose_name='水费')
    电费余额 = models.FloatField(verbose_name='电费')
    入住人数 = models.IntegerField(verbose_name='入住人数')

    def __str__(self):
        return self.寝室号

    class Meta:
        verbose_name = '寝室房间'
        verbose_name_plural = '寝室房间'


class 学生(models.Model):
    姓名 = models.CharField(max_length=128, verbose_name='姓名')
    性别 = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    学号 = models.CharField(max_length=128, verbose_name='学号', primary_key=True)
    密码 = models.CharField(max_length=128, verbose_name='密码', default='123456789')

    寝室号 = models.ForeignKey(to="寝室", verbose_name='寝室编号', on_delete=models.SET_NULL, null=True)

    联系方式 = models.CharField(max_length=128, verbose_name='联系方式')
    专业班级 = models.CharField(max_length=128, verbose_name='专业班级')
    违纪信息 = models.CharField(max_length=512, verbose_name='违纪信息')

    def __str__(self):
        return self.学号

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'


class 维修人员(models.Model):
    工号 = models.CharField(max_length=128, verbose_name='维修人工号', primary_key=True)
    姓名 = models.CharField(max_length=128, verbose_name='维修人姓名')
    性别 = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别')
    联系方式 = models.CharField(max_length=128, verbose_name='联系方式')

    class Meta:
        verbose_name = '维修人员'
        verbose_name_plural = '维修人员'

    def __str__(self):
        return self.工号


class 维修人员负责区域(models.Model):
    工号 = models.ForeignKey(to='维修人员', verbose_name='维修人员工号', on_delete=models.CASCADE)
    宿舍楼号 = models.ForeignKey(to='宿舍楼', verbose_name='负责宿舍楼号', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('工号', '宿舍楼号')
        verbose_name_plural = '维修人员负责区域'

class 充值记录(models.Model):
    充值金额 = models.FloatField(verbose_name='充值金额')
    充值类型 = models.CharField(max_length=32, choices=(('水费余额', '水费'), ('电费余额', '电费')), default='电费', verbose_name='充值类型')

    class Meta:
        verbose_name = '充值记录'
        verbose_name_plural = '充值记录'


class 报修记录(models.Model):
    报修信息 = models.CharField(max_length=512, verbose_name='报修信息')
    日期 = models.DateTimeField(default=datetime.datetime.now(), verbose_name='报修日期')
    寝室号 = models.ForeignKey(to='寝室', verbose_name='寝室号', on_delete=models.CASCADE)
    工号 = models.ForeignKey(to='维修人员', verbose_name='工号', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = '报修记录'
        verbose_name_plural = '报修记录'


class 访客(models.Model):
    访客姓名 = models.CharField(max_length=128, verbose_name='访客姓名')
    性别 = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='访客性别')
    联系方式 = models.CharField(max_length=128, verbose_name='联系方式')

    class Meta:
        verbose_name = '访客'
        verbose_name_plural = '访客'


class 访问(models.Model):
    访问原因 = models.CharField(max_length=128, verbose_name='访问原因')
    访问日期 = models.DateTimeField(default=datetime.datetime.now(), verbose_name='访问日期')

    class Meta:
        verbose_name = '访问记录'
        verbose_name_plural = '访问记录'
