# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 13:38
from __future__ import unicode_literals

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cryptofolio', '0007_auto_20171019_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeaccount',
            name='passphrase',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, default=None, help_text='<ul><li>Optional</li></ul>', null=True),
        ),
    ]