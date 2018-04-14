from django.conf.urls import url
from recognition import views

urlpatterns = [
    url(r'^detect/$', views.detect, name='detect'),
    url(r'^train/$', views.train, name='train'),
    # url(r'^add/$', views.add, name='add'),
    # url(r'^$', image_create, name='create'),
    # url(r'^(?P<slug>[\w-]+)/$', ImageDetailView.as_view(), name='detail'),
]
