import datetime

from django.db import models
class Department(models.Model):
    title = models.CharField(verbose_name="部门名称",max_length=32)
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(max_length=32,verbose_name="姓名")                        # primary_key = True
    password = models.CharField(verbose_name="密码",max_length=64)                    # 修改表的时候，可以直接添加一行或去掉。
    age = models.IntegerField(verbose_name="年龄")    # 默认为2
    count = models.DecimalField(verbose_name="余额",max_digits=10,decimal_places=2,null=True)
    create_time = models.DateField(verbose_name="入职时间",auto_now=False,null=True)
    # depart_id = models.BigIntegerField(verbose_name="部门id")
    #设置外键
    # deaprt = models.ForeignKey(to="Department",to_fields="id",on_delete=models.CASCADE,null=True,blank=True)
    deaprt = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE,null=True,verbose_name="所属部门")
    gener_choice = (
        (1,"男"),
        (2,"女")
    )
    #在django中进行约束
    gender = models.SmallIntegerField(verbose_name="性别",choices=gener_choice,null=True)

class Adminuser(models.Model):
    name = models.CharField(max_length=64,verbose_name="用户名")
    password = models.CharField(verbose_name="密码",max_length=128)
    create_time = models.DateField(verbose_name="入职时间",auto_now=False,null=True)
    class Meta():
        db_table = "admin"
        unique_together = (("name","password"))

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

# Create your models here.
