# Generated by Django 4.2.1 on 2023-10-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0014_delete_blogpost_gamedb_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
