# Generated by Django 4.2.7 on 2023-11-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecheck',
            name='file',
            field=models.FileField(upload_to='text'),
        ),
    ]