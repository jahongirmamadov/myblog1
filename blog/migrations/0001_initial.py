# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20, verbose_name=b'Author')),
                ('title', models.CharField(max_length=30, verbose_name=b'Title')),
                ('content', models.TextField(max_length=250, verbose_name=b'Content')),
            ],
        ),
    ]
