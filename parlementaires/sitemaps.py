from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from app.models import Home, Lois, ContactForm
from actualite.models import Actualite
from ourteam.models import OurTeam
from sondage.models import Sondage


class LoisSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Lois.objects.all()

class ActualiteSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Actualite.objects.all()

class OurTeamSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return OurTeam.objects.all()


class SondageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return Sondage.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['app:home', 'ourteam:about', 'app:contact', 'login', 'register']

    def location(self, item):
        return reverse(item)
