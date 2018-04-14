from .views import ProfileView
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^random/$', RandomProfileDetailView.as_view(), name='random'),
    # url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
     url(r'^$', ProfileView.as_view(), name='profile_list'),
    # url(r'^$', TemplateView.as_view(template_name='profiles/profile_list.html'), name='profile'),
]
