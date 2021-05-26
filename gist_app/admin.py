from django.contrib import admin

from gist_app.models import Gist


@admin.register(Gist)
class GistAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('title', 'user', 'slug')
    prepopulated_fields = {'slug': ('title',), }
