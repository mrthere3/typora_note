from django.db import models

# Create your models here.
class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="手机号",max_length=11)
    price = models.IntegerField(verbose_name="价格",default=0)
    level_chioce = {
        (1,"1级"),
        (2,"2级"),
        (3,"3级"),
        (4,"4级"),
    }
    level = models.SmallIntegerField(verbose_name="级别",choices=level_chioce,default=1)
    status_choices = {
        (1,"已占用"),
        (2,"未占用"),
    }
    status = models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=2)
    class Meta():
        db_table = "PrettyNum"
