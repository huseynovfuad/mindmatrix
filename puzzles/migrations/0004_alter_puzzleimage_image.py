# Generated by Django 3.2 on 2023-12-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0003_alter_puzzleimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzleimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
