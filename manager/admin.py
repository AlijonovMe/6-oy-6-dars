from django.contrib import admin
from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'year', 'price', 'brand')
    list_display_links = ('id', 'name')
    list_editable = ('year', 'price', 'brand')
    list_filter = ('id', 'name')
    list_per_page = 10
    actions_on_top = False
    search_fields = ('name', 'year')

admin.site.register(Brands)
admin.site.register(Cars, CarsAdmin)