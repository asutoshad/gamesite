# Generated by Django 4.2.1 on 2023-09-09 16:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0006_alter_gamedb_cover_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedb',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
