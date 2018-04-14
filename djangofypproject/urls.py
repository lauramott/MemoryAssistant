from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from django.conf.urls import url, include

from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView

from profiles.views import RegisterView
# from recognition.views import detect
from recognition import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# urlpatterns += [
#     url(r'^api/facescan/', include('facescan.api.urls', namespace='api-facescan')),
#     # url(r'^api-token-auth/', obtain_jwt_token),
#     # url(r'^api-token-refresh/', refresh_jwt_token),
#     # url(r'^api-token-verify/', verify_jwt_token),
# ]

urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^recognition/', include('recognition.urls', namespace='recognition')),
    # url(r'^recognition/detect/$', 'recognition.views.detect'),
    url(r'^myprofile/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('facescan.urls', namespace='facescan')),
    url(r'^contact/', include('menu.urls', namespace='menu')),
    #url(r'^myprofile/', TemplateView.as_view(template_name='profile_list.html'), name='profile'),
    # url(r'^recognition/$', TemplateView.as_view(template_name='recognition.html'), name='recognition'),
    url(r'^add', views.add, name='add'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
