# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_peizhi'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=datetime.datetime(2016, 4, 15, 15, 14, 54, 617080, tzinfo=utc), max_length=40, verbose_name='\u7f51\u5740'),
            preserve_default=False,
        ),
    ]
