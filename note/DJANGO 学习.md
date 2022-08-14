*DJANGO* 学习

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

~~~html
{#<p>过滤器:(|)  将管道符左边的数据当做第一个参数传入过滤器中如果需要第二个参数 则名称后冒号</p>#}
<p>统计长度:{{ l|length }}</p>
<p>加法运算:{{ i|add:123 }}</p>
<p>默认值:{{ b|default:'布尔值为False' }}</p>
<p>时间格式:{{ ctime|date:'Y-m-d H:i:s' }}</p>
<p>截取字符(包含三个点):{{ ss|truncatechars:10 }}</p>
<p>截取单词(不包含三个点):{{ ss|truncatewords:3 }}</p>
<p>文件大小:{{ file_size|filesizeformat }}</p>
<p>转义:{{ s1|safe }}</p>
<p>标签:其实就是流程控制 if判断  for循环</p>
{% for foo in s %}
    {% if forloop.first %}
        <p>这是第一次循环</p>
    {% elif forloop.last %}
        <p>这是最后一次</p>
    {% else %}
        <p>继续!!!</p>
    {% endif %}
    {% empty %}
        <p>传递过来的数据是空的</p>
{% endfor %}
~~~

以下三张

![](https://img-blog.csdnimg.cn/65ead6b1b4b74f5f8450fbb495ffc2fc.png)

![](https://img-blog.csdnimg.cn/c847a5f7347745bfbaab0cf3f2e91e37.png)

![](https://img-blog.csdnimg.cn/c64b5070d7714ea59433c874987e2a82.png)

## 6.交互与响应

### request交互对象详解

~~~tcl
Request
　　我们知道当URLconf文件匹配到用户输入的路径后，会调用对应的view函数，并将 HttpRequest对象 作为第一个参数传入该函数。

我们来看一看这个HttpRequest对象有哪些属性或者方法：
1 HttpRequest.scheme 　 请求的协议，一般为http或者https，字符串格式(以下属性中若无特殊指明，均为字符串格式)

2 HttpRequest.body 　　 http请求的主体，二进制格式。

3 HttpRequest.path 所请求页面的完整路径(但不包括协议以及域名)，也就是相对于网站根目录的路径。

4 HttpRequest.path_info 获取具有 URL 扩展名的资源的附加路径信息。相对于HttpRequest.path，使用该方法便于移植。

if the WSGIScriptAlias for your application is set to “/minfo”, then path might be “/minfo/music/bands/the_beatles/” and path_info would be “/music/bands/the_beatles/”.
5 HttpRequest.method 获取该请求的方法，比如： GET POST …

6 HttpRequest.encoding 获取请求中表单提交数据的编码。

7 HttpRequest.content_type 获取请求的MIME类型(从CONTENT_TYPE头部中获取)，django1.10的新特性。

8 HttpRequest.content_params 获取CONTENT_TYPE中的键值对参数，并以字典的方式表示，django1.10的新特性。

9 HttpRequest.GET 返回一个 querydict 对象(类似于字典，本文最后有querydict的介绍)，该对象包含了所有的HTTP GET参数

10 HttpRequest.POST 返回一个 querydict ，该对象包含了所有的HTTP POST参数，通过表单上传的所有 字符 都会保存在该属性中。

11 HttpRequest.COOKIES 　 返回一个包含了所有cookies的字典。

12 HttpRequest.FILES 　　 返回一个包含了所有的上传文件的 querydict 对象。通过表单所上传的所有 文件 都会保存在该属性中。

key的值是input标签中name属性的值，value的值是一个UploadedFile对象

13 HttpRequest.META 返回一个包含了所有http头部信息的字典

View Code
14 HttpRequest.session 中间件属性

15 HttpRequest.site　　 中间件属性

16 HttpRequest.user　　 中间件属性，表示当前登录的用户。
~~~

### 响应的方式

```python
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("返回内容")
#HttpResponse 将后面的内容返回

def index(request):
    return redirect ("https://baidu.com")
#redirect 重定向到别的网址
def _get_queryset(klass):
	"""
	从模型、管理器或QuerySet中返回一个QuerySet。为了使get_object_or_404和get_list_or_404更加DRY(代码不重复)。
	如果klass不是Modle、Manager或QuerySet，那么就会产生一个ValueError。
	"""
def get_object_or_404(klass, *args, **kwargs):
	"""
	使用get()返回一个对象如果对象不存在返回Http404异常。
	klass可能是一个Model、Manager或QuerySet对象; get()查询中使用了参数和关键字参数。
	注意: 就像get()一样，如果有多个返回对象，则返回多个对象。
	"""
def get_list_or_404(klass, *args, **kwargs):
	"""
	使用filter()返回一个对象列表,如果列表为空则返回一个Http404异常
	klass可能是一个Model、Manager或QuerySet对象。
	filter()查询中使用了参数和关键字参数。
	"""
def resolve_url(to, *args, **kwargs):
	"""
	返回一个与所传递参数相对应的URL。
	参数可以是:
	*模型:模型的get_absolute_url()函数将被调用。
	*视图名称，可能带有参数:' urlresolvers.reverse()将用于反向解析名称。
	*一个URL，它将按原样返回。
	"""
```

### 登录案例

登陆界面

~~~python
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        print(request.POST)
        return HttpResponse("登陆成功")
~~~

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {% csrf_token %}
    <form  method="post" action="/login/" >
        <input name="用户名" type="text" placeholder="用户名">
        <input name="密码" type="password" placeholder="密码">
        <input value="提交" type="submit" >
    </form>

</body>
</html>
~~~

django和flask不同，在进行表单校验，多一个{% csrf_token %}安全机制校验，不加校验，无法实现登陆成功的响应。

## 7.*DJANGO* ORM

~~~python
pip install mysqlclient==1.4.1 
~~~

#### 1修改配置文件

~~~python
#在sentting.py
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'django_db',
        'USER' : 'root',
        'PASSWORD' : '123456',
        'HOST' : '127.0.0.1',
        'POST' : '3306',
    }
}
~~~

#### 2.在models.py创建表类

~~~python

#django底层会根据类，来生成对应的表和字段from django.db import models #继承models.Model
class UserInfo(models.Model):
    name = models.CharField(max_length=32)                        # primary_key = True
    password = models.CharField(max_length=64)                    # 修改表的时候，可以直接添加一行或去掉。 
    age = models.IntegerField(default=2)                          # 默认为2
    # data = models.IntegerField(null=True, blank=True)           # 允许为空
    # account = models.DecimalField(max_digits=10, decimal_places=2， default = 0)  # 总长度10位， 小数2位, 默认0.
    # create_time = models.DateTimeField()                        # 时间 
    # on_delete=models.CASCADE 级联删除， models.SET_NULL 设置为空。
    # depart = models.ForeignKey(to='Department', to_field='id')  # 生成depart_id字段，和Department的to_field关联
    # gender_choices = (
    #    (1, "男"),
    #    (2, "女"),)
    # gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)  # 选着约束
#django底层会根据类，来生成对应的表和字段
~~~

#### 3.执行数据初始化脚本

~~~python
python manage.py makemigrations
python manage.py migrate
~~~

#### 4.使用orm操作数据库表的数据

##### 1.orm用法与字段类型

~~~python
1.orm用法：属性名 = models.字段类型()
 
2.常见字段类型
    (1)AutoField：    自动增长的IntegerField, 不指定时Django会自动创建属性名为id的自动增长属性
    (2)IntegerField： 整数
    (3)FloatField（）：浮点数
    (4)DecimalField(max_digits=None, decimal_places=None)：可以指定精度的十进制浮点数
                                                        max_digits：总位数
                                                        decimal_places：小数位数
    (5)CharField(max_length=20)：字符串（max_length：最大字符个数）
                                 必须要指定max_length参数 不指定会直接报错
    (6)TextFiled：         大文本字段，一般超过4000个字符时使用
    (7)BooleanField：      布尔字段，值为True或False
    (8)NullBooleanField：  支持Null、True、False三种值                                       
    (9)DateField(auto_now=False, auto_now_add=False)：日期
                参数auto_now：每次保存对象时，自动设置该字段为当前时间，
                              用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false
                参数auto_now_add：当对象第一次被创建时自动设置当前时间，
                              用于创建的时间戳，它总是使用当前日期，默认为false
                注意：参数auto_now_add和auto_now是相互排斥的，组合将会发生错误
    (10)TimeField(auto_now=False, auto_now_add=False)：时间
    (11)DateTimeField：日期时间
    (12)FileField：上传文件字段，以二进制的形式
    (13)ImageField：继承于FileField，对上传的内容进行校验，确保是有效的图片
 
 
3.常见字段属性(选项)
    (1)null：如果为True，表示允许为空，默认值是False
    (2)blank：如果为True，则该字段允许为空白，默认值是False    
             对比：null是数据库范畴的概念，blank是表单验证范畴的
    (3)db_column：字段的名称，如果未指定，则使用属性的名称
              （只限于数据库表中的名字，操作数据库还是类属性的名字）
    (4)db_index：若值为True, 则在表中会为此字段创建索引，默认值是False（为了优化查询速度 ）
    (5)default：默认值，这可以是值或可调用对象。如果可调用，则每次创建新对象时都会调用它。
    (6)primary_key：若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用
    (7)unique：如果为True, 这个字段在表中必须有唯一值，这个值不能重复，默认值是False
    (8)verbose_name:该参数是所有字段都有的 就是用来对字段的解释
 
 
4.关系字段类型(用法与普通字段类型一样)
    关系型数据库的关系包括三种类型：
        ForeignKey：        一对多，将字段定义在多的一端中
        ManyToManyField：   多对多，将字段定义在任意一端中
        OneToOneField：     一对一，将字段定义在任意一端中
 
 
5.字段的的增删改(记得执行数据库迁移的两条命令)：
    (1)字段的增加
	    a.可以在终端内直接给出默认值
        b.该字段可以为空
            info = models.CharField(max_length=32,verbose_name='个人简介',null=True)
        c.直接给字段设置默认值
            hobby = models.CharField(max_length=32,verbose_name='兴趣爱
好',default='study')
        然后执行数据库迁移的两条命令
    (2)字段的修改
	   直接修改代码然后执行数据库迁移的两条命令即可！
    (3)字段的删(慎重)
	   直接注释对应的字段然后执行数据库迁移的两条命令即可！
       注意：执行完毕之后字段对应的数据也都没有了
~~~

##### 2.ORM之查询操作(查询集、过滤器)

~~~tcl
1.基本概念
    (1)查询集：表示从数据库中获取的模型对象集合(objects.),在管理器上调用过滤器方法会返回查询集
               查询集可以含有0个、一个或多个过滤器
       查询集特点:a.惰性执行：创建查询集不会访问数据库，直到在模板中调用数据时，才会访问数据库
                             调用数据的情况包括迭代、序列化、与if合用
                 b.缓存：查询集的结果被存下来之后，再次查询相同数据时会使用之前缓存的数据
    (2)过滤器：基于所给的参数限制查询的结果
 
 
 
2.过滤器分两类
    (1)返回列表数据的过滤器：
        all()：       返回所有的数据(以对象形式)
        filter()：    返回满足条件的数据，括号内可以携带多个参数，参数与参数之间默认是and关系
        exclude()：   返回满足条件之外的数据，相当于sql语句中where部分的not关键字
        order_by()：  返回排序后的数据
        注意：返回的是列表对象，即[数据对象1,数据对象2...]，
              获取对象，它支持索引取值和切片操作，但是不支持负数索引
              获取第一个对象filter().first()
    (2)返回单个对象的过滤器:
        get()：       返回单个满足条件的对象
                      # 如果未找到会引发"模型类.DoesNotExist"异常
                      # 如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常
        count()：     返回当前查询的总条数
        aggregate()： 聚合
        exists()：    判断查询集中是否有数据，如果有则返回True，没有则返回False
    (3)常见过滤器查询：
        a.查询id为1的用户名(用exact：判断是否相等)
            usernames = models.User.objects.filter(id__exact=1)
 
        b.查询姓名中包含'张'的名字(用contains：是否包含)
            usernames = models.User.objects.filter(username__contains='张')
 
        c.查询姓名中以‘欣’结尾的名字(用startswith/endswith：以什么开头/以什么结尾)
            usernames = models.User.objects.filter(username__endswith='欣')
 
        d.查询姓名不为空的成员(用isnull : 是否为null)
            usernames = models.User.objects.filter(username__isnull=False)
 
        e.查询编号为2或4的成员(pk:主键/id) (用in：是否包含在范围内)
            usernames = models.User.objects.filter(pk__in=[2,4])
 
        f.查询编号大于2的成员（gt:大于、gte:大于等于、lt:小于、lte:小)
            usernames = models.User.objects.filter(id__gt=2)
 
        g.查询id不等于３的成员(exclude:条件以外的数据)
            usernames = models.User.objects.exclude(id=3)
 
        h.查询2020年注册的成员(year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算)
            usernames = models.User.objects.filter(pub_date__year=2020)
 
        i.查询2020年1月1日后注册的成员
            from datetime import date
            usernames = models.User.objects.filter(pub_date__gt=date(2020,1,1))
~~~

~~~python
在views.py中对数据库数据的增删改查
from app01 import models
1.查数据
    # 方式一
        res = models.User.objects.filter(username=username)
            """
            返回值你先看成是列表套数据对象的格式
            它也支持索引取值，切片操作，但是不支持负数索引
            它也不推荐你使用索引的方式取值
            user_obj = models.User.objects.filter(username=username).first()
            filter括号内可以携带多个参数 参数与参数之间默认是and关系
            """
        return render(request,'userlist.html',{'user_queryset':user_queryset})    # 指定返回
    # 方式二
        user_queryset = models.User.objects.all()
        return render(request,'userlist.html',locals())    # 全部返回
 
 
2.增数据
    # 方法一：
    res = models.User.objects.create(username=username,password=password)  # 返回值就是当前被创建的对象本身
    # 方法二：
    user_obj = models.User(username=username,password=password)
    user_obj.save()              # 保存数据/对象调用save方法
 
 
3.删数据
    models.User.objects.filter(id_user=1).delete()    # 指定删除id_user=1的数据
 
 
4.改数据
    # 方式一：
    models.User.objects.filter(id=edit_id).update(username=username,password=password)
        # 将filter查询出来的列表中所有的对象全部更新，批量更新操作，只修改被修改的字段
    # 方式二：
    edit_obj.username = username
    edit_obj.password= password
    edit_obj.save()
        # 用重新赋值方式，全部逐一更换当字段特别多的时候效率会非常的低
        # 因为从头到尾，无论该字段是否被修改都将数据的所有字段全部更新一边 
~~~



 
