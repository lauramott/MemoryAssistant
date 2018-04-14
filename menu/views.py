from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import request
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DetailView
# Create your views here.
# function based view
from .forms import ContactCreateForm, ContactImageCreateForm
from .models import ContactDetails
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


class ContactListView(ListView):
    def get_queryset(self):
        return ContactDetails.objects.all()


class RecognizedContactDetailView(DetailView):
    def get_queryset(self):
        return ContactDetails.objects.all() # filter(owner=self.request.user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return ContactDetails.objects.filter(owner=self.request.user)


class ContactCreateView(LoginRequiredMixin, CreateView):
    form_class = ContactImageCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    # success_url = '/contact/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        # pre save signal
        instance.owner = self.request.user
        # instance.save()
        return super(ContactCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context=super(ContactCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Contact'
        return context


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'menu/detail-update.html'
    form_class = ContactImageCreateForm
    login_url = '/login/'

    # success_url = '/contact/'

    def get_context_data(self, *args, **kwargs):
        context= super(ContactUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = 'Update Contact: {name}'.format(name=name)
        return context

    def get_queryset(self):
        return ContactDetails.objects.filter(owner=self.request.user)

    def get_name(self):
        return self.get_object().name
