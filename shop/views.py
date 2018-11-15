import datetime

from django.shortcuts import render
from django.http import HttpResponse

# 增删改查的操作
#  注意:主表添加数据跟单表操作一样      往子表添加数据的时候,主表的数据一定要存在
from shop.models import *

"""
多个sql操作 事务的概念
"""


def add(request):
    """
    模型的id有两种写法
    模型实例.主键字段
    模型实例.pk
    """
    # 主表id
    # 保存主表数据
    info = GroupInfo(title='小甜甜2号', img='/img/xxx.png', current_price=99.00, original_price=998.00, count=50,
                     is_delete=False)
    info.save()
    # 子表外键字段 可以设置对象,也可以设置主键
    #
    # INSERT INTO  Group_Detail(description,end_time='2018-11-16 18:20:20',info_id=2)
    detail = GroupDetail(description='白天么么哒,晚上啪啪啪!!!',
                         end_time=datetime.datetime.strptime('2018-11-16 18:20:20', '%Y-%m-%d %H:%M:%S'),
                         info_id=info.info_id)
    detail.save()
    return HttpResponse('一对一添加数据')


"""
正向查询  通过子表模型查询主表
反向查询  通过主表模型查子表  
"""

# 显示,商品的名称,商品的价格,商品的图片,商品的详情,商品的结束时间
""""
SELECT d.d ,d.end_time,   
FROM  group_detail d,group_info i
WHERE d.info_id = i.info_id
"""

"""
# SELECT  *  FROM   group_detail
# SELECT  *  FROM  group_info  where  info_id = 1
# SELECT  *  FROM  group_info  where  info_id = 2
"""


def find(request):
    # 通过子表模型查询主表数据
    detail_list = GroupDetail.objects.all()
    for detail in detail_list:
        print(detail.description)
        # 如果想获取主表的数据  可以直接通过 子表的外键属性获取相关主表的信息
        print(detail.info.title)
    return render(request, 'shops.html', context={'detail_list': detail_list})


# __有两个关联的表  通过主表的某个条件 查询子表的数据
#  限定符

def find1(request):
    # 通过主表模型查询子表数据
    infos = GroupInfo.objects.all()
    # 如果想通过主表模型对象获取子表的相关信息
    # 主表模型对象.子表模型类名小写
    for info in infos:
        print(info.title)
        print(info.groupdetail.description)
    return HttpResponse('通过主表查询')

# class Person:
#     def __init__(self, detail, addresses):
#         # 一对一
#         self.detail = detail
#         # 一对多
#         self.addresses = addresses


# class Detail:
#     pass
#
#
# class Address:
#     def __init__(self, name):
#         self.name = name
#
#
# if __name__ == '__main__':
#     detail = Detail()
#     addresses = [Address(f'武汉市{i}') for i in range(10)]
#
#     p = Person(detail=detail, addresses=addresses)
#
#     for address in p.addresses:
#         print(address.name)
