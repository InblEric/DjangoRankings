# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0004_matchup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchup',
            name='created',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
