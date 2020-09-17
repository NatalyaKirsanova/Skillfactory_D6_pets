import uuid
from django.utils.translation import gettext as _
from django.db import models
from django.core import validators

class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=256,
                            verbose_name="Вид животного")

    def __str__(self):
        return self.type


class Pet(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256, verbose_name=_("Кличка"))
    age = models.IntegerField(verbose_name=_("Возраст"),
                              validators=[validators.MaxValueValidator(100)])
    doc = models.ForeignKey('Registration', on_delete=models.CASCADE,
                            verbose_name=_("Регистрационный документ"),
                            related_name="pet_registration")
    photo = models.ImageField(upload_to='pets_photo', blank=True)
    type_animal = models.ForeignKey('Animal', on_delete=models.CASCADE,
                              verbose_name=_("Вид животного"),
                              related_name="pet_animal")
    breed = models.CharField(max_length=256,
                            verbose_name=_("Порода"))
    character = models.TextField(verbose_name=_("Характер"), blank=True)
    def make_word_end(self):
        word = "лет"
        n = self.age
        if n > 99:
            n = n % 100
        if n in range(5, 21):
            word = "лет"
        elif n % 10 == 1:
            word = "год"
        elif n % 10 in range(2, 5):
            word = "года"
        return "{} {}".format(self.age, word)


    def __str__(self):
        return "{} {} ({}, {})".format(self.type_animal, self.breed, self.make_word_end(),
                                    self.name)


class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(verbose_name=_("Дата регистрации"))
    reg_num = models.CharField(max_length=256, auto_created=True,
                               null=True, blank=True,
                               verbose_name=_("Регистрационный номер"))
    def __str__(self):
        return self.reg_num
            # if self.reg_num else self.date.strftime("%d-%m-%Y")




