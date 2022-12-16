from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.FileField()
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=8)


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    type = models.IntegerField()


class Owner(models.Model):
    ownername = models.CharField(max_length=30)
    companyname = models.CharField(max_length=40)
    companyaddress = models.CharField(max_length=70)
    contactno = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)


class Product(models.Model):
    pname = models.CharField(max_length=30)
    model = models.CharField(max_length=25)
    image = models.FileField()
    price = models.IntegerField()


class Buy(models.Model):
    username = models.ForeignKey(Register, on_delete=models.CASCADE)
    pname = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.CharField(max_length=25)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phonenumber = models.IntegerField()
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=100)
