# Generated by Django 3.2.7 on 2023-01-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20230106_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line',
            field=models.CharField(max_length=255, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line2',
            field=models.CharField(max_length=255, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='address',
            name='delivery_instructions',
            field=models.CharField(max_length=255, verbose_name='Delivery Instructions'),
        ),
        migrations.AlterField(
            model_name='address',
            name='full_name',
            field=models.CharField(max_length=150, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=50, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='address',
            name='town_city',
            field=models.CharField(max_length=150, verbose_name='Town/City/State'),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
