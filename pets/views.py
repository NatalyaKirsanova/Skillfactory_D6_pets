from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView,DetailView)
from pets.models import Pet, Animal

class AnimalListView(ListView):
    model = Animal


class IndexPageView(TemplateView):
    template_name = 'index.html'


class PetListView(ListView):
    model = Pet
    def get_queryset(self):
        qs = super(PetListView,self).get_queryset()
        get_params = self.request.GET.dict()
        # search
        if get_params.get('q'):
            qs = qs.filter(type_animal__type=get_params.get('q'))
        return qs
# class EditorManager(models.Manager):
#     def get_queryset(self):
#         return super(EditorManager, self).get_queryset().filter(role='E')

class PetView(DetailView):
    model = Pet

class ContactsView(TemplateView):
    template_name = 'contacts.html'


