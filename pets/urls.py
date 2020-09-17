from django.urls import path
from .views import (IndexPageView, PetListView, ContactsView, PetView, AnimalListView)

urlpatterns = [
    path('', IndexPageView.as_view()),
    # path('pets/', PetListView.as_view()),
    path('pets/', AnimalListView.as_view()),
    path('pets/dog/', PetListView.as_view()),
    path('pets/cat/', PetListView.as_view()),
    path('pets/parrot/', PetListView.as_view()),
    path('pets/<str:pk>/', PetView.as_view()),
    path('contacts/', ContactsView.as_view()),
]