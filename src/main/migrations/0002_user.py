# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 8 or more', regex='^.{8, }$')])),
                ('address', models.CharField(max_length=2000)),
            ],
        ),
    ]
