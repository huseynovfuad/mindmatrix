from django.db import models
from django.utils.text import slugify

# Create your models here.

def upload_to_categories(instance, filename):
    return f"categories/{slugify(instance.name)}/{filename}"

class Category(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to=upload_to_categories)
    order = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"