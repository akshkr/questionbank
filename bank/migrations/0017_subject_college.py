# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0016_auto_20170626_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='college',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='bank.College'),
        ),
    ]
