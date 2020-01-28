# Generated by Django 3.0.2 on 2020-01-27 22:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200127_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='author',
            new_name='author_id',
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 27, 22, 35, 5, 10596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 27, 22, 35, 5, 10007, tzinfo=utc)),
        ),
    ]