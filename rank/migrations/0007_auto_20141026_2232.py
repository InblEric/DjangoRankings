# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0006_auto_20141025_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='elo',
            field=models.FloatField(default=750.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchup',
            name='created_at',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
