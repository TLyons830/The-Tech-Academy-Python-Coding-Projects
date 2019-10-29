from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from ..checkbook import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('CreateNewAccount/', views.CreateNewAccount, name="CreateNewAccount"),
    path('AddTransaction/', views.AddTransaction, name="AddTransaction"),
    path('BalanceSheet/', views.BalanceSheet, name="BalanceSheet"),
]

