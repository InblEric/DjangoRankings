# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0005_auto_20141025_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchup',
            old_name='created',
            new_name='created_at',
        ),
    ]
