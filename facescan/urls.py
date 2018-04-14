"""djangofypproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    ItemListView,
    ItemCreateView,
    ItemDetailView,
    ItemUpdateView,

)


urlpatterns = [
    url(r'create/$', ItemCreateView.as_view(), name='create'),
    # url(r'(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='update'),
    url(r'(?P<slug>[\w-]+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'^$', ItemListView.as_view(), name='list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
