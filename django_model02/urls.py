from django.contrib import admin
from django.conf.urls import url

from shop import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('add/', views.add),
    url('find/', views.find),
]
