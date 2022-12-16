# Generated by Django 4.1.3 on 2022-11-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omg', '0002_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=25)),
                ('image', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
