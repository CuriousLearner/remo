# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from remo.reports import ACTIVITY_ROTM_NOMINATED


def create_ROTM_nominated_activity(apps, schema_editor):
    Activity = apps.get_model("reports", "Activity")
    Activity.objects.create(name=ACTIVITY_ROTM_NOMINATED)


def remove_ROTM_nominated_activity(apps, schema_editor):
    Activity = apps.get_model("reports", "Activity")
    Activity.objects.filter(name=ACTIVITY_ROTM_NOMINATED).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_ROTM_nominated_activity,
            reverse_code=remove_ROTM_nominated_activity
        ),
    ]
