"""parlementaires URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from .sitemaps import HomeSitemap, LoisSitemap, ContactFormSitemap, ActualiteSitemap, OurTeamSitemap, SondageSitemap

sitemaps = {
    'home-view': HomeSitemap,
    'lois-view' : LoisSitemap,
    'contact-form'  : ContactFormSitemap,
    'actualite-view' : ActualiteSitemap,
    'team' : OurTeamSitemap,
    'sondage-view' : SondageSitemap,
    }

sitemap_urls = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    ]

urlpatterns = [
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('actualite/', include('actualite.urls')),
    path('ourteam/', include('ourteam.urls')),
    path('sondage/', include('sondage.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += sitemap_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
