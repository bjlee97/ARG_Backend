# Generated by Django 3.2.9 on 2021-11-09 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arg_backend', '0008_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='hints',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='possible_answers',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='current_hint',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='current_puzzle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='arg_backend.puzzle'),
        ),
    ]