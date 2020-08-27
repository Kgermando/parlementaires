from django.contrib.sitemaps import Sitemap

from app.models import Home, Lois, ContactForm
from actualite.models import Actualite
from ourteam.models import OurTeam
from sondage.models import Sondage

class HomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Home.objects.all()
    
    def lastmod(self, obj):
        return obj.updated

class LoisSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Lois.objects.all()

class ContactFormSitemap(Sitemap):


    def items(self):
        return ContactForm.objects.all()

class ActualiteSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Actualite.objects.all()

class OurTeamSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return OurTeam.objects.all()


class SondageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Sondage.objects.all()