# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170928_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=4376128176, on_delete=django.db.models.deletion.CASCADE, to='api.Categories'),
        ),
    ]