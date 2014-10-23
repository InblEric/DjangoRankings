# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=100)),
                ('p1Votes', models.IntegerField()),
                ('p2Votes', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='matchup',
            name='player1',
            field=models.ForeignKey(related_name='player_1', to='rank.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchup',
            name='player2',
            field=models.ForeignKey(related_name='player_2', to='rank.Player'),
            preserve_default=True,
        ),
    ]
