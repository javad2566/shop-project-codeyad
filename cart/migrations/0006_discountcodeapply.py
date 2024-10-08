# Generated by Django 5.0.3 on 2024-07-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCodeApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام تخفیف')),
                ('discount', models.SmallIntegerField(default=0, verbose_name='درضد')),
                ('quantity', models.SmallIntegerField(default=5, verbose_name='تعداد')),
            ],
            options={
                'verbose_name': 'تخفیف',
                'verbose_name_plural': 'تخفیف ها ',
            },
        ),
    ]
