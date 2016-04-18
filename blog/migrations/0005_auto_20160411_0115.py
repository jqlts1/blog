# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160411_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peizhi',
            name='cidaoang',
            field=models.TextField(verbose_name='\u6b21\u5bfc\u822a'),
        ),
    ]
