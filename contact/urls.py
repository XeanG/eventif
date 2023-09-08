from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.contact_view, name='contact_view'),
]
