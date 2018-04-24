# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-20 07:11
from __future__ import unicode_literals

from django.db import migrations, models

from djangocms_moderation import conf


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_moderation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemoderation',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enable moderation for page'),
        ),
        migrations.AddField(
            model_name='pagemoderationrequest',
            name='reference_number',
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='workflow',
            name='reference_number_backend',
            field=models.CharField(choices=conf.REFERENCE_NUMBER_BACKENDS, default=conf.DEFAULT_REFERENCE_NUMBER_BACKEND, max_length=255),
        ),
    ]
