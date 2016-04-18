# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160411_0115'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Peizhi',
        ),
    ]
