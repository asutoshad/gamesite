# Generated by Django 4.2.1 on 2023-10-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0013_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AddField(
            model_name='gamedb',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
