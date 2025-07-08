from django.contrib import admin

# Register your models here.
from . models import Category, Item, Cover_Image

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    # prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name']

admin.site.register(Cover_Image)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Item)
