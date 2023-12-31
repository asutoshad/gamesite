# Generated by Django 4.2.1 on 2023-08-28 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0002_genre_platform_tag_remove_gamedb_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedb',
            name='cover_art',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gamedb',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gamedb',
            name='developer_publisher',
            field=models.CharField(max_length=30),
        ),
        migrations.RemoveField(
            model_name='gamedb',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='gamedb',
            name='platforms',
        ),
        migrations.AlterField(
            model_name='gamedb',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='gamedb',
            name='tags',
        ),
        migrations.AlterField(
            model_name='gamedb',
            name='title',
            field=models.CharField(max_length=5),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Platform',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='gamedb',
            name='genres',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='gamedb',
            name='platforms',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='gamedb',
            name='tags',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
