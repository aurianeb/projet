# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_auto_20151226_1616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Film',
            new_name='Films',
        ),
    ]
