# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160415_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='en_title',
        ),
    ]
