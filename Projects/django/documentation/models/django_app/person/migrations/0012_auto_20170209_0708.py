# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_auto_20170209_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to='person.User'),
        ),
    ]
