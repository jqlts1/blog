# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_delete_zidingyi'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='info',
            field=models.CharField(default=datetime.datetime(2016, 4, 17, 6, 2, 32, 619497, tzinfo=utc), max_length=500, verbose_name='\u7b80\u4ecb'),
            preserve_default=False,
        ),
    ]
