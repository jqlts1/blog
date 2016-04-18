# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160411_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peizhi',
            options={'verbose_name': '\u914d\u7f6e\u4fe1\u606f', 'verbose_name_plural': '\u914d\u7f6e\u4fe1\u606f'},
        ),
        migrations.AddField(
            model_name='peizhi',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 4, 10, 17, 6, 19, 315978, tzinfo=utc), help_text=b'\xe9\x9a\x8f\xe6\x84\x8f\xe5\xb0\xb1\xe5\x8f\xaf\xe4\xbb\xa5', max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
    ]
