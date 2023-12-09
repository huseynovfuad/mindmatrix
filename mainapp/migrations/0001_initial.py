# Generated by Django 3.2 on 2023-12-09 17:21

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to=mainapp.models.upload_to_categories)),
                ('is_locked', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]