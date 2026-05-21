from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContatcAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','create_date',)
    ordering = ('-id',)
    # list_filter = ('create_date',)
    search_fields = 'id','first_name','last_name',
    list_per_page = 10
    list_max_show_all= 200