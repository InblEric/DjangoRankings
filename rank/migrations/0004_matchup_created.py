# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0003_auto_20141023_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='created',
            field=models.DateField(default=datetime.datetime(2014, 10, 25, 23, 10, 1, 141513)),
            preserve_default=False,
        ),
    ]
