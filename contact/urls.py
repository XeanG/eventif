from django.urls import path
from . import views

urlpatterns = [
    # Outras URLs aqui
    path('contato/', views.contact_view, name='contact_view'),
]
