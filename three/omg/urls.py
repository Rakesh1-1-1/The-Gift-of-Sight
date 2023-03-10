from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('register', views.register, name="register"),
    path('finish', views.finish, name="finish"),
    path('regview', views.regview, name="regview"),
    path('userview', views.userview, name="userview"),
    path('table', views.table, name="table"),
    path('adm', views.adm, name="adm"),
    path('user', views.user, name="user"),
    path('login', views.login, name="login"),
    path('check', views.check, name="check"),
    path('own', views.own, name="own"),
    path('owner', views.owner, name="owner"),
    path('ow', views.ow, name="ow"),
    path('otable', views.otable, name="otable"),
    path('ownview', views.ownview, name="ownview"),
    path('prview', views.prview, name="prview"),
    path('pro', views.pro, name="pro"),
    path('product', views.product, name="product"),
    path('ptablle', views.ptablle, name="ptablle"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('buy', views.buy, name="buy"),
    path('show', views.show, name="show"),
    path('btable', views.btable, name="btable"),
    path('pf', views.pf, name="pf"),
    path('pftable', views.pftable, name="pftable"),
    path('order', views.order, name="order"),
    path('ortable', views.ortable, name="ortable"),
    path('logout', views.logout, name="logout"),
    path('about', views.about, name="about"),
    path('glasses', views.glasses, name="glasses"),
    path('con', views.con, name="con"),
    path('contact', views.contact, name="contact"),

]
