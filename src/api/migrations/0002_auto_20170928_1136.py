# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.IntegerField()),
                ('user', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default=4366478000, on_delete=django.db.models.deletion.CASCADE, to='api.Categories'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderList',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Dish'),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
    ]
