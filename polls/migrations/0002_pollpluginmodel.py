# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20161027_1312'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='polls_pollpluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
