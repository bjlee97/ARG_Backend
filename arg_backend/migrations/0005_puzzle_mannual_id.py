# Generated by Django 3.2.9 on 2021-11-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arg_backend', '0004_puzzle_puzzleanswermapping'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='mannual_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]