# Generated by Django 4.2.1 on 2023-08-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0003_alter_gamedb_cover_art_alter_gamedb_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedb',
            name='cover_art',
            field=models.ImageField(upload_to='game_covers/'),
        ),
    ]
