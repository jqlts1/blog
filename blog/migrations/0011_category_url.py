# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_article_en_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default=datetime.datetime(2016, 4, 16, 7, 14, 41, 520465, tzinfo=utc), max_length=40, verbose_name='\u7f51\u5740'),
            preserve_default=False,
        ),
    ]
