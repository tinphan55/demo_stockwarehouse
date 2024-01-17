# Generated by Django 4.1.5 on 2023-12-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpartnerinfo',
            name='commission',
            field=models.FloatField(default=0.3, verbose_name='Tỷ lệ chia hoa hồng'),
        ),
        migrations.AlterField(
            model_name='clientpartnerinfo',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Công ty'),
        ),
    ]