from django.http import HttpResponse
from django.shortcuts import render 


def subscribe(request):
   return render(request, 'subscripitions/subscripition_form.html')