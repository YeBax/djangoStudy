# Generated by Django 2.2.4 on 2019-08-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
