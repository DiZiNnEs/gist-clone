# Generated by Django 3.2.3 on 2021-05-26 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gist',
            options={'ordering': ['title'], 'verbose_name': 'gist', 'verbose_name_plural': 'gists'},
        ),
        migrations.AlterModelTable(
            name='gist',
            table='gist',
        ),
    ]
