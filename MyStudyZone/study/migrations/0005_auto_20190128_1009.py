# Generated by Django 2.1.3 on 2019-01-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_auto_20181128_1031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-update_time']},
        ),
    ]