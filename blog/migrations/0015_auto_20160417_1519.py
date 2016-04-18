# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_category_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
