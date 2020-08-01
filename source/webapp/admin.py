from django.contrib import admin
from .models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_filter = ('created_time',)
    list_display = ('pk', 'name', 'email', 'text', 'created_time')
    list_display_links = ('pk', 'name')
    search_fields = ('created_time',)


admin.site.register(GuestBook, GuestBookAdmin)
