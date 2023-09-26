from django.urls import path
from contact import views # Geila - Está importanto da views que acabei de criar

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]