# Generated by Django 5.0.3 on 2024-07-19 05:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0015_category_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل کاربر')),
                ('phone', models.IntegerField(max_length=12, verbose_name='شماره تماس')),
                ('address', models.CharField(max_length=400, verbose_name='ادرس کاربر')),
                ('is_paid', models.BooleanField(default=False, verbose_name='بررسی پرداخت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_activate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'سفارش کاربر',
                'verbose_name_plural': 'سفارش ها ثبت شده',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=2, verbose_name='سایز سفارش')),
                ('color', models.CharField(max_length=12, verbose_name='رنگ')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'ایتم سفارش',
                'verbose_name_plural': 'ایتم های سفارش',
            },
        ),
    ]
