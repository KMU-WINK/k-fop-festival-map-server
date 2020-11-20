from django.contrib import admin
from .models import *

@admin.register(BoothCategory)
class BoothCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    #    list_filter = ['']
    search_fields = ['name']


admin.site.register(Region)
admin.site.register(Booth)
admin.site.register(Review)
admin.site.register(Like)
admin.site.register(Notice)
admin.site.register(HashTag)
admin.site.register(Stamp)

