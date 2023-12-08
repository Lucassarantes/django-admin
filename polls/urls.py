from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:dog_id>", views.detail, name="detail"),
    path("<int:dog_id>/results/", views.results, name="results"),
]