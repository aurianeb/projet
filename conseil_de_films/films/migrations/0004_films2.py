# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films2',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('provenance', models.CharField(max_length=200)),
                ('photographie', models.CharField(max_length=100)),
                ('musique', models.CharField(max_length=100)),
            ],
        ),
    ]
