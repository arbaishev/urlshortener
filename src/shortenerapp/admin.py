from django.contrib import admin
from .models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcode', 'updated', 'created', 'count')
    list_filter = ('created',)


admin.site.register(URL, URLAdmin)
