# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170928_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Paid'), ('C', 'Canceled'), ('I P', 'In Process')], default=3, max_length=1),
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=4561619632, on_delete=django.db.models.deletion.CASCADE, to='api.Categories'),
        ),
    ]
