from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)


@admin.register(Organization)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


