# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug2',
            field=models.CharField(default=datetime.datetime(2016, 4, 15, 15, 17, 35, 161652, tzinfo=utc), max_length=50, verbose_name='\u7f51\u57402'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=50, verbose_name='\u7f51\u5740'),
        ),
    ]
