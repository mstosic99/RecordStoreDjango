# Generated by Django 3.1.5 on 2021-01-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0002_auto_20210106_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.URLField(default=''),
        ),
    ]