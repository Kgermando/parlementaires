from django.contrib import admin

from app.models import Home, Lois, ReseauSociaux, ContactForm, Comment

admin.site.site_header = 'JEUNES PARLEMENTAIRES'
admin.site.site_title = "Interface d'administration des données"
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'home_title',
        'home_image',
    )

    list_filter = (
        'home_title',
        )

    search_fields = ['home_title',]

    list_per_page = 50
    
class LoisAdmin(admin.ModelAdmin):
    list_display = (
        'lois_title',
        'propostion_nom',
        'created',
    )

    list_filter = (
        'lois_title',
        'propostion_nom',
        'created',
        )

    search_fields = ['lois_title', 'propostion_nom', 'created',]

    list_per_page = 50

class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name',
        'objet_name',
        'last_name',
        'email_id',
        'phone_num',
        'created',
    )

    list_filter = (
        'first_name',
        'objet_name',
        'email_id',
        'phone_num',
        'created',
        )

    search_fields = ['first_name',
        'objet_name',
        'email_id',
        'phone_num',]

    list_per_page = 50

class CommentFormAdmin(admin.ModelAdmin):
    list_display = (
        'comment_title',
        'created',
    )

    list_filter = (
        'comment_title',
        'created',
        )

    search_fields = ['comment_title','created',]

    list_per_page = 50

admin.site.register(Home, HomeAdmin)
admin.site.register(Lois, LoisAdmin)
# admin.site.register(ReseauSociaux)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Comment, CommentFormAdmin)
