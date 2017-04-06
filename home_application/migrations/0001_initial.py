# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tbl_zhihu',
            fields=[
                ('title', models.TextField()),
                ('link', models.TextField()),
                ('index', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='favourite',
            name='num',
            field=models.ForeignKey(to='home_application.tbl_zhihu'),
        ),
    ]
