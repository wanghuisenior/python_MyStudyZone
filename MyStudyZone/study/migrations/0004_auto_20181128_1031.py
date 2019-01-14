# Generated by Django 2.1.3 on 2018-11-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_user_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['update_time']},
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='photos/default_user.jpg', upload_to='photos'),
        ),
    ]