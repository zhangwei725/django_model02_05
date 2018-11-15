from django.db import models


class GroupInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    img = models.CharField(max_length=100)
    # max_digits 表示数字长度(整数位数+ 小数位数 = 长度) decimal_places 表示小数的位数
    # 现价
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 原价
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 对应数据库的int类型
    count = models.IntegerField()
    # 假删除
    is_delete = models.BooleanField(default=False)

    #     元信息
    class Meta:
        db_table = 'group_info'


class GroupDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    end_time = models.DateTimeField()
    """
     1> to, 对应主表类
     2> on_delete=None,(2.0版本中强制要求重写改属性)
        当主表里的数据删除时候,子表如果操作关联数据
        可选值 
                 models.CASCADE  cascade (级联删除) 当主表的记录删除时,子表关联数据也删除
                 models.CASCADE  models.SET_NULL 当主表的记录删除时 子表的关联的外键字段设null   注意一定要在外键字段设置一下null=True
                 models.DO_NOTHING   当主表数据删除时,子表不做任何操作
    
    to_field=None 参照主表的字段 默认是主表主键
    """
    # info = models.OneToOneField('GroupInfo', on_delete=models.DO_NOTHING,to_field='title' null=True)
    # 外键的名称默认情况 外键字段_id
    #
    info = models.OneToOneField('GroupInfo', on_delete=models.DO_NOTHING,
                                null=True)

    class Meta:
        db_table = "group_detail"


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'


class Address(models.Model):
    aid = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'address'
