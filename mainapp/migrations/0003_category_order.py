# Generated by Django 3.2 on 2023-12-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_category_is_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]