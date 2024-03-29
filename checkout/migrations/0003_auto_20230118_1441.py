# Generated by Django 3.2.7 on 2023-01-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20230116_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentselections',
            options={'verbose_name': 'Payment Selection', 'verbose_name_plural': 'Payment Selections'},
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='delivery_method',
            field=models.CharField(choices=[('IS', 'In Store'), ('HD', 'Home Delivery'), ('DD', 'Digital Delivery')], help_text='Required', max_length=255, verbose_name='delivery_method'),
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='delivery_name',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='delivery_name'),
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='delivery_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99.'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='delivery price'),
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='delivery_timeframe',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='delivery timeframe'),
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='delivery_window',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='delivery window'),
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='deliveryoptions',
            name='order',
            field=models.IntegerField(default=0, help_text='Required', verbose_name='list order'),
        ),
        migrations.AlterField(
            model_name='paymentselections',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='paymentselections',
            name='name',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='name'),
        ),
    ]
