# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-18 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
