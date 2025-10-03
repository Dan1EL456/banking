from django.urls import path
from . import views

app_name = 'authentication_app'


urlpatterns = [
    path("", views.index, name="index"),
    path('countries/', views.country_list, name='country_list'),
    path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
    #path("countries", views.Country, name="country"),
    #path("deparments", views.Department, name="department"),
    #path("cities", views.City, name="city"),
    #path("users", views.User, name="user"),
]