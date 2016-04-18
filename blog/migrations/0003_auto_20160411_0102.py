# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160326_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peizhi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidaoang', models.TextField(max_length=100, verbose_name='\u6b21\u5bfc\u822a')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='en_title',
            field=models.CharField(max_length=100, null=True, verbose_name='\u82f1\u6587\u6807\u9898', blank=True),
        ),
    ]
