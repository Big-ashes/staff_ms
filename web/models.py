from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题",max_length=32)



class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name='账户余额',decimal_places=2,default=0,max_digits=10)
    # account = models.DecimalField(verbose_name='账户余额',max_length=10,decimal_places=2,default=0,max_digits=10)
    #数字长度是10，小数位占3

    creat_time = models.DateTimeField(verbose_name='入职时间')
    # 无约束
    # department_id = models.BigIntegerField(verbose_name='部门id')

    # 有约束
    # to和department关联，to_field连接id那一列，Django会自动加id

    #级联删除
    depart = models.ForeignKey(verbose_name='部门id',to="Department",to_field="id",on_delete=models.CASCADE)

    #置空
    # depart = models.ForeignKey(verbose_name='部门id', to="Department", to_field="id", null=True, blank=True,on_delete=models.CASCADE)
    gender_choices=(
        (1,"男"),
        (2,"女"),
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)