from django.contrib import admin
from django.conf.urls import url

from shop import views
from other import views as v1

urlpatterns = [
    url('admin/', admin.site.urls),
    url('add/', views.add),
    url('find/', views.find),
    url('add1/', views.fk_add),
    url('find1/', views.fk_find),
    url('date/', v1.op_date),
    url('many/', views.many_to_many),
    url('delete/', views.delete),
]
