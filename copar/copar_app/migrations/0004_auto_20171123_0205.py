# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copar_app', '0003_auto_20171123_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresarialquest',
            name='data_fund_emp',
            field=models.CharField(max_length=15),
        ),
    ]
