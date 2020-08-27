from django.contrib import admin

from sondage.models import Sondage, Vote
# Register your models here.
admin.site.register(Sondage)
admin.site.register(Vote)