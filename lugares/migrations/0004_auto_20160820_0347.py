# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 06:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0003_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagem',
            old_name='title',
            new_name='titulo',
        ),
    ]