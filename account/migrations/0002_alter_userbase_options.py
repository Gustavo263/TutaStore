# Generated by Django 3.2.7 on 2022-10-18 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbase',
            options={'ordering': ('-created',), 'verbose_name': 'Accounts', 'verbose_name_plural': 'Accounts'},
        ),
    ]