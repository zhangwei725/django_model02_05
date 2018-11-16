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

    def __str__(self):
        return self.info_id


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


#  ==============一对多==============

# 主表的一条记录对应子表的多条记录
# .all()
class UserManager(models.Manager):
    def all(self):
        return super().all().filter(is_delete=False)

    def add_guest(self, *kwarg):
        user = User(kwarg, is_delete=True)
        user.save()
        return user


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    is_delete = models.BooleanField(default=False)
    test = UserManager()

    class Meta:
        db_table = 'user'


class Address(models.Model):
    aid = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=255)
    # address_set
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='addresses')

    class Meta:
        db_table = 'address'
        # default_related_name


# 多对多
#  权限   增 删 改 查
#  角色  超级管理员 管理员  普通用户


class Per(models.Model):
    per_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    roles = models.ManyToManyField('Role')

    # roles = models.ManyToManyField('Role', through='RolePerRelation', through_fields=['role', 'per'])

    class Meta:
        db_table = 'per'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    # 角色的名称
    name = models.CharField(max_length=30)
    # 角色说明
    desc = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'role'

# class RolePerRelation(models.Model):
#     role = models.ForeignKey('Role', on_delete=models.DO_NOTHING)
#     per = models.ForeignKey('Per', on_delete=models.DO_NOTHING)
