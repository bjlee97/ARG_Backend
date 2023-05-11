# Generated by Django 3.2.9 on 2021-11-08 20:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('arg_backend', '0007_puzzle_completion_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=100)),
                ('discord_username', models.CharField(max_length=100, unique=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='arg_backend.teams')),
            ],
        ),
    ]