# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_category_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zidingyi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u81ea\u5b9a\u4e49\u5185\u5bb9')),
                ('beizhu', models.CharField(max_length=100, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u81ea\u5b9a\u4e49\u6a21\u5757',
                'verbose_name_plural': '\u81ea\u5b9a\u4e49\u6a21\u5757',
            },
        ),
    ]
