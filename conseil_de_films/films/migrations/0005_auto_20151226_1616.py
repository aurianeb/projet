# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_films2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Films2',
            new_name='Film',
        ),
        migrations.DeleteModel(
            name='Films',
        ),
    ]
