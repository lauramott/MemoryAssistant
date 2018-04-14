from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, ListView
from django.http import Http404
# Create your views here.
from menu.models import ContactDetails
from facescan.models import Item
from .forms import RegisterForm
from .models import Profile

# from .models import Profile

User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'


# class ProfileDetailView(DetailView):
#     template_name = 'profiles/user.html'
#
#     def get_object(self):
#         username = self.kwargs.get("username")
#         if username is None:
#             raise Http404
#         return get_object_or_404(User, username__iexact=username, is_active=True)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
#         user = context['user']
#         items_exists = Item.objects.filter(user=user).exists()
#         qs = ContactDetails.objects.filter(owner=self.get_object())
#         if items_exists and qs.exists():
#             context['contacts']=qs
#         return context


class ProfileView(ListView):
    template_name = 'profile_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context=super(ProfileView, self).get_context_data(*args, **kwargs)
    #     context['title'] = 'My Profile'
    #     return context

    def get_queryset(self):
        print('getting objs')
        return Profile.objects.all()
