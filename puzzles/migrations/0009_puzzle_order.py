# Generated by Django 3.2 on 2023-12-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0008_remove_puzzle_is_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]