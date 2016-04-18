# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160417_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True, verbose_name='\u6458\u8981', blank=True),
        ),
    ]
