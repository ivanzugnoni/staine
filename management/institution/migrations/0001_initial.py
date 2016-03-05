# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import institution.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(default=institution.models.get_hash_id, max_length=16, serialize=False, editable=False, primary_key=True)),
                ('year', models.CharField(max_length=16, choices=[(b'primero', b'Primero'), (b'segundo', b'Segundo'), (b'tercero', b'Tercero')])),
                ('division', models.CharField(max_length=16, choices=[(b'a', b'A'), (b'b', b'B'), (b'economia', b'Economia'), (b'cs_naturales', b'Ciencias Naturales')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(default=institution.models.get_hash_id, max_length=16, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('dni', models.CharField(max_length=16)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=32)),
                ('course', models.ForeignKey(to='institution.Course')),
            ],
        ),
    ]
