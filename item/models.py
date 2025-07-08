from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cover_Image(models.Model):
    image = models.ImageField(upload_to='cover_images', blank=True, null=True)

    class Meta:
        verbose_name = 'Cover Image'
        verbose_name_plural = 'Cover Images'
    
    def __str__(self):
        return f"Cover Image {self.id}"

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    descroption = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
