# Generated by Django 5.0.1 on 2024-01-22 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realstockaccount', '0004_rename_realcashtransfer_realstockaccountcashtransfer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realbankcashtransfer',
            options={'verbose_name': 'Sao kê tiền TKNH', 'verbose_name_plural': 'Sao kê tiền TKNH'},
        ),
        migrations.AlterModelOptions(
            name='realstockaccountcashtransfer',
            options={'verbose_name': 'Sao kê tiền TKCK', 'verbose_name_plural': 'Sao kê tiền TKCK'},
        ),
        migrations.AlterModelOptions(
            name='realtradingpower',
            options={'verbose_name': 'Sức mua tài khoản', 'verbose_name_plural': 'Sức mua tài khoản'},
        ),
    ]
