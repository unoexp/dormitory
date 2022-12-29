# 学生宿舍管理系统
## 环境部署
- python版本为3.7
- 使用requirements安装依赖
``` pip install -r requirements.txt ```
## 配置数据库 
- dormitory/settings.py 第75行, 修改你的MySQL数据库配置
- 执行以下代码生成数据库
```
python .\manage.py makemigrations
python .\manage.py migrate
```
## 启动
- 运行服务
```
python .\manage.py runserver
```
- 若允许其他主机访问 需改为
```
python.exe .\manage.py runserver 0.0.0.0:8000
```

## 创建超级管理员

- 输入命令

```
python .\manage.py createsuperuser
```

- 创建完成后可通过`127.0.0.1:8000/admin`进入管理员页面