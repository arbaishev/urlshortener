# Generated by Django 3.0.3 on 2020-07-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='custom',
            field=models.BooleanField(default=False),
        ),
    ]
