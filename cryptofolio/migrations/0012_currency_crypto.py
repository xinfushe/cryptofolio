# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptofolio', '0011_manualinput'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='crypto',
            field=models.BooleanField(default=False),
        ),
    ]
