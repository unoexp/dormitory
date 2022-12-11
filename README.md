# 学生宿舍管理系统
## 环境部署
- python版本为3.7
- 使用requirements安装依赖
``` pip install -r requirements.txt ```
- 安装xadmin2.0
``` pip install git+https://github.com/sshwsfc/xadmin.git@django2 ```

## 配置数据库 
- dormitory/settings.py 第75行, 修改你的MySQL数据库配置

## 启动
- 运行服务
```
.\venv\Scripts\python.exe .\manage.py runserver
```
- 若允许其他主机访问 需改为
```
.\venv\Scripts\python.exe .\manage.py runserver 0.0.0.0:8000
```