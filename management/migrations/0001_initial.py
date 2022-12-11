# Generated by Django 3.0.4 on 2022-11-25 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_name', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='楼栋')),
            ],
            options={
                'verbose_name': '宿舍楼',
                'verbose_name_plural': '宿舍楼',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=3, verbose_name='宿舍号')),
                ('room_water', models.FloatField(verbose_name='水费')),
                ('room_electricity', models.FloatField(verbose_name='电费')),
                ('room_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Building', verbose_name='宿舍楼')),
            ],
            options={
                'verbose_name': '宿舍房间',
                'verbose_name_plural': '宿舍房间',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('student_sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别')),
                ('student_id', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='学号')),
                ('password', models.CharField(default='123456789', max_length=20, verbose_name='密码')),
                ('student_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Building', verbose_name='宿舍楼')),
                ('student_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Room', verbose_name='宿舍房间')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.CreateModel(
            name='Mistake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=100, verbose_name='违纪原因')),
                ('date', models.DateTimeField(verbose_name='违纪时间')),
                ('mistake_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student', verbose_name=' 学号')),
            ],
            options={
                'verbose_name': '违纪信息',
                'verbose_name_plural': '违纪信息',
            },
        ),
    ]
