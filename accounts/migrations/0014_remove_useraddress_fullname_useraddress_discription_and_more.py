# Generated by Django 5.0.3 on 2024-07-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_useraddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='fullname',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='discription',
            field=models.CharField(blank=True, default='d', max_length=1000, null=True, verbose_name='توضیحات اضافی'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام شما'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی شما'),
        ),
    ]
