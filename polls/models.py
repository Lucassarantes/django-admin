from django.db import models
from django.contrib import admin

class Owner(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"

class Dog(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class DogInline(admin.TabularInline):
    model = Dog
    extra = 0
    
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'age', 'email', 'display_dogs')

    def display_dogs(self, obj):
        return ', '.join([dog.name for dog in obj.dog_set.all()])

    display_dogs.short_description = 'Dogs'

    inlines = [DogInline]