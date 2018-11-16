from django.db.models import Q
import datetime
from django.http import HttpResponse
from django.shortcuts import render

# 双下划线
# 在查询条件封装限定符
# 多表查询的时候跨表查询
from shop.models import GroupInfo, Address, GroupDetail, User

"""
比较运算符  > < >= <= !=
逻辑运算符  and  or  [not] Q
范围判断   between  and  
包含      in
非空     is  null 
模糊  like

"""


# gt 大于
# lt  小于
# gte
# lte
# djano采用是双下划线

def op(request):
    info_list = GroupInfo.objects.filter(count__gt=30)
    info_list = GroupInfo.objects.filter(count__lt=30)
    info_list = GroupInfo.objects.filter(count__lte=30)
    info_list = GroupInfo.objects.filter(count__gte=30)

    # between  最小值 and 最大值   >>>  range

    addresses = Address.objects.filter(aid_range=[1, 10])

    #  in
    addresses = Address.objects.filter(aid__in=[5, 1, 10])
    # like '%关键字%'
    Address.objects.filter(Q(desc__contains='武汉') | Q(aid=1))
    # 忽略大小写
    Address.objects.filter(Q(desc__icontains='武汉') | Q(aid=1))
    # 以什么开头
    Address.objects.filter(Q(desc__startwith=''))
    Address.objects.filter(Q(desc__istartwith=''))
    # 以什么结尾
    Address.objects.filter(desc__endswith='')
    Address.objects.filter(desc__iendswith='')
    # 判断是否为null
    Address.objects.filter(desc__isnull=False)

    return HttpResponse()


# 不使用django的时区
# 将mysql的时区设置django的


def op_date(request):
    # 查询2018年的所有信息
    details = GroupDetail.objects.filter(end_time__year=2018)
    #     查询某个时间段的数据
    detail_list = GroupDetail.objects.filter(end_time__range=[datetime.datetime.strptime('2018-11-15', '%Y-%m-%d'),
                                                              datetime.datetime.strptime('2018-11-17', '%Y-%m-%d')])

    detail_list = GroupDetail.objects.filter(end_time__range=[datetime.date(2018, 11, 12),
                                                              datetime.date(2018, 11, 16)])

    detail_list = GroupDetail.objects.filter(end_time__lt=datetime.date(2018, 11, 12))

    for detail in details:
        print(detail.pk)

    return HttpResponse()


# 多表的时候进行跨表操作
# 外键属性名__关联表字段
def op_many(request):
    # 查询用户是娇娇的所有的地址信息
    Address.objects.filter(user__name__contains='娇娇')


def test(request):
    User.objects.all()
    User.objects.add_guest()
