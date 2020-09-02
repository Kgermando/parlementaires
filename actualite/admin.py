from django.contrib import admin

from actualite.models import Actualite

admin.site.site_header = 'JEUNES PARLEMENTAIRES ADMIN'
admin.site.site_title = "Interface d'administration des données"
# Register your models here.

class ActualiteAdmin(admin.ModelAdmin):
    list_display = (
        'actu_title',
        'propostion_nom',
        'created'
    )

    list_filter = (
        'propostion_nom',
        'created')

    search_fields = ['actu_title', 'propostion_nom', 'created']

    list_per_page = 50

admin.site.register(Actualite, ActualiteAdmin)
