# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('titre_original', models.CharField(max_length=100)),
                ('titre_francais', models.CharField(max_length=100)),
                ('realisateur', models.CharField(max_length=100)),
                ('couleur', models.CharField(max_length=100)),
                ('annee', models.IntegerField()),
                ('pays', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('acteurs', models.CharField(max_length=1000)),
                ('actrices', models.CharField(max_length=1000)),
                ('appreciation', models.CharField(max_length=100)),
                ('scenario', models.CharField(max_length=100)),
                ('photographie', models.CharField(max_length=100)),
                ('musique', models.CharField(max_length=100)),
            ],
        ),
    ]
