from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContatcAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','create_date',)
    ordering = ('-id',)
    # list_filter = ('create_date',)
    search_fields = 'id','first_name','last_name','category',
    list_per_page = 10
    list_max_show_all= 200
    list_display_links= 'first_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)