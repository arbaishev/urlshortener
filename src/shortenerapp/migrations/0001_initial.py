# Generated by Django 3.0.3 on 2020-07-27 19:53

from django.db import migrations, models
import shortenerapp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=220, validators=[shortenerapp.validators.validate_url])),
                ('shortcode', models.SlugField(max_length=6, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
