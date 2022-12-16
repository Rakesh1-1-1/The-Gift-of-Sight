import re
from datetime import date

from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def regview(request):
    name = request.POST['name']
    age = request.POST['age']
    image = request.FILES['image']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    data = Register(name=name, age=age, image=image, address=address, phone=phone, email=email, username=username)
    data.save()
    data1 = Login(username=username, password=password, type=1)
    data1.save()
    return render(request, "finish.html")


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request, "register.html")


def finish(request):
    return render(request, "finish.html")


def check(request):
    username = request.POST['username']
    password = request.POST['password']
    data1 = Login.objects.get(username=username, password=password)
    if data1.type == 1:
        request.session['username'] = data1.username
        data3 = Product.objects.all()
        return render(request, "user.html", {"pr": data3})
    elif data1.type == 0:
        request.session['username'] = data1.username
        return render(request, "adm.html")
    elif data1.type == 2:
        request.session['username'] = data1.username
        return render(request, "ow.html")


def login(request):
    return render(request, "login.html")


def user(request):
    return render(request, "user.html")


def adm(request):
    return render(request, "adm.html")


def table(request):
    return render(request, "table.html")


def userview(request):
    value = Register.objects.all()
    value1 = Login.objects.all()
    return render(request, "table.html", {"re": value, "lo": value1})


def own(request):
    ownername = request.POST['ownername']
    companyname = request.POST['companyname']
    companyaddress = request.POST['companyaddress']
    contactno = request.POST['contactno']
    username = request.POST['username']
    password = request.POST['password']
    value2 = Owner(ownername=ownername, companyname=companyname, companyaddress=companyaddress, contactno=contactno,
                   username=username, password=password)
    value2.save()
    return render(request, "login.html")


def owner(request):
    return render(request, "owner.html")


def ow(request):
    return render(request, "ow.html")


def ownview(requset):
    value3 = Owner.objects.all()
    return render(requset, "otable.html", {"owne": value3})


def otable(request):
    return render(request, "otable.html")


def pro(request):
    pname = request.POST['pname']
    model = request.POST['model']
    image = request.FILES['image']
    price = request.POST['price']
    value4 = Product(pname=pname, model=model, image=image, price=price)
    value4.save()
    return render(request, "finish.html")


def product(request):
    return render(request, "product.html")


def prview(request):
    value5 = Product.objects.all()
    return render(request, "ptablle.html", {"pr": value5})


def ptablle(request):
    return render(request, "ptablle.html")


def delete(request, id):
    value6 = Product.objects.get(id=id)
    value6.delete()
    return HttpResponseRedirect(reverse("prview"))


def buy(request):
    username = request.session['username']
    pname = request.POST['pname']
    today = date.today()
    user = Register.objects.get(username=username)
    prod = Product.objects.get(id=pname)
    value6 = Buy(username=user, pname=prod, date=today)
    value6.save()
    value7 = Product.objects.all()
    return render(request, "user.html", {"pr": value7})


def show(request):
    value8 = Buy.objects.all()
    return render(request, "btable.html", {"by": value8})


def btable(request):
    return render(request, "btable.html")


def pf(request):
    user = request.session['username']
    reg = Register.objects.get(username=user)

    return render(request, "pftable.html", {"re": reg})


def pftable(request):
    return render(request, "pftable.html")


def order(request):
    use = request.session['username']
    regi = Register.objects.get(username=use)
    bu = Buy.objects.filter(username=regi)
    return render(request, "ortable.html", {'by': bu})


def ortable(request):
    return render(request, "ortable.html")


def logout(request):
    return render(request, "logout.html")


def about(request):
    return render(request, "about.html")


def glasses(request):
    return render(request, "glasses.html")


def con(request):
    name = request.POST['name']
    phonenumber = request.POST['phonenumber']
    email = request.POST['email']
    message = request.POST['message']
    co = Contact(name=name, phonenumber=phonenumber, email=email, message=message)
    co.save()
    return render(request, "finish.html")


def contact(request):
    return render(request, "contact.html")
