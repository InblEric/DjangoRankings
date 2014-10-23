# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0002_matchup_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchup',
            name='week',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
