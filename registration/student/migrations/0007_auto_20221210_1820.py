# Generated by Django 3.0.5 on 2022-12-10 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20221210_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='file',
            field=models.FileField(default='settings.MEDIA_ROOT/images/software_9nCK3Z1.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 10, 18, 20, 22, 856873)),
        ),
    ]
