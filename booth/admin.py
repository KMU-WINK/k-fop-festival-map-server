from django.contrib import admin
from booth.models import BoothCategory


# Register your models here.
@admin.register(BoothCategory)
class BoothCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    #    list_filter = ['']
    search_fields = ['name']