from django.contrib import admin
from django.forms import ModelForm

from .models import Registration, Animal, Pet

class RegistrationForm(ModelForm):
    pass


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass