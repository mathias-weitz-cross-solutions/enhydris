from django.contrib import admin
from hydroscope.dbsync.models import Database

class DatabaseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Database._meta.fields]

admin.site.register(Database, DatabaseAdmin)
