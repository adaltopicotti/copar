# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copar_app', '0005_empresarialquest_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresarialquest',
            name='insert_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]