# Generated by Django 3.0.5 on 2022-12-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20221209_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
