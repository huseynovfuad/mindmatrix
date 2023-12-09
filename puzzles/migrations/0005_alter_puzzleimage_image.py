# Generated by Django 3.2 on 2023-12-09 10:36

from django.db import migrations, models
import puzzles.models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0004_alter_puzzleimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzleimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=puzzles.models.upload_to_puzzle_images),
        ),
    ]
