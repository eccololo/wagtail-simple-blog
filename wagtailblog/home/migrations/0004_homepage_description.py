# Generated by Django 5.1.5 on 2025-02-05 08:46

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_call_to_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
