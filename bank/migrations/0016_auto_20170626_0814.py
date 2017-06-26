# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0015_subject_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_image',
            field=models.FileField(blank=True, default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subject',
            name='question_image',
            field=models.FileField(blank=True, default=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_image',
            field=models.FileField(blank=True, default=False, upload_to=''),
        ),
    ]
