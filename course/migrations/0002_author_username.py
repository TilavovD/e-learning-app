# Generated by Django 4.0.6 on 2022-07-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
