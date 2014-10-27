# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0007_auto_20141026_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchup',
            name='id',
        ),
        migrations.AddField(
            model_name='matchup',
            name='num',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
