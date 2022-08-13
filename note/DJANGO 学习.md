# *DJANGO* 学习

## 1.安装django

```python
pip install django
```

## 2.创建项目

django项目中会有一些默认的文件和默认的文件夹

## 2.1在终端

在项目路径下

```
django-admin startproject projectname
```

```
│  manage.py 	[项目的管理，启动项目，创建app，数据管理]
│
└─mydj
        asgi.py		[接受网络请求]
        settings.py		[项目配置 ]
        urls.py		[路径函数的对应关系]
        wsgi.py		[接受网络请求]
        __init__.py
```

## 3.APP

```
-项目
	-app,	用户管理【表结构、函数、HTML模板、CSS】
	-app,	订单管理【表结构、函数、HTML模板、CSS】
	-app,	后台管理【表结构、函数、HTML模板、CSS】
	-app,	网站【表结构、函数、HTML模板、CSS】
	-app,	API【表结构、函数、HTML模板、CSS】
	..
	注意 我们开发变焦简介，用不到多app
```

创建app

```python
python manage.py startapp appname
#文件结构如下图
│  manage.py
│
├─app01
│  │  admin.py 【django默认提供了后台管理】
│  │  apps.py
│  │  models.py
│  │  tests.py	【单元测试文件】
│  │  views.py	【视图函数】
│  │  __init__.py
│  │
│  └─migrations
│          __init__.py
│
└─mydj
    │  asgi.py
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py

```

## 4.快速上手

### 在setting.py文件当中注册app

![](https://cdn.jsdelivr.net/gh/mrthere3/typora_note/img/js/202208051521176.png)



### 编写url和视图函数关系

![](https://cdn.jsdelivr.net/gh/mrthere3/typora_note/img/js/202208051528185.png)

### 编写视图函数views.index

![](https://cdn.jsdelivr.net/gh/mrthere3/typora_note/img/js/202208051530473.png)

### 项目启动命令

+ 命令行启动

  ```python
  python manage.py runserver
  ```

### 模板文件templates目录

```python
def user_list(request):
	return render(request,"user_list.html") #在app目录下的templates目录下寻找该HTML文件
#优先在templates目录下寻找
#根据app的注册顺序，在每个app下的templates目录中去寻找
```

![](https://cdn.jsdelivr.net/gh/mrthere3/typora_note/img/js/202208051602276.png)

### 静态文件路径static目录下

+ CSS
+ 图片
+ JS

默认存放在static目录下，在进行调用时候，进行/static加完整路径进行调用

也可在setting.py文件中自行设置

![](https://cdn.jsdelivr.net/gh/mrthere3/typora_note/img/js/202208051712055.png)

## 5. *DJANGO* 模板语法

本质上：在html中写一些占位符，由数据对这些占位符进行替换和处理。 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        {% for i in data_list %}
            <li>{{ i }}</li>
        {% endfor %}
    </ul>

</body>
</html>
```

模板中使用特定的模板语法

```python
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html',{'data_list':['发票', '海关缴款书', '代扣代缴', '农产品加计扣除发票信息', '农产品加计扣除海关文书', '异常发票']})
```

$\color{red}{在视图函数，使用json格式进行前后端的交互}$

## 6.交互与响应

```html
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("返回内容
```





 
