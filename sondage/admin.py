from django.contrib import admin

from sondage.models import Sondage, Vote

admin.site.site_header = 'JEUNES PARLEMENTAIRES ADMIN'
admin.site.site_title = "Interface d'administration des données"
# Register your models here.

class SondageAdmin(admin.ModelAdmin):
    list_display = (
        'sondage_title',
        'propostion_nom',
        'vote_yes',
        'vote_no',
        'vote_null',
        'total',
        'created',
    )

    list_filter = (
        'sondage_title',
        'propostion_nom',
        'vote_yes',
        'vote_no',
        'vote_null',
        'created',
        )

    search_fields = ['lois_title', 'propostion_nom', 'created',]

    list_per_page = 50

class VoteAdmin(admin.ModelAdmin):
    list_display = (
        'sondageID',
        'userID',
    )

    list_filter = (
      'sondageID',
        'userID',
        )

    search_fields = ['sondageID', 'userID',]

    list_per_page = 50


admin.site.register(Sondage, SondageAdmin)
admin.site.register(Vote, VoteAdmin)