from django.http import HttpResponseRedirect
from django.shortcuts import render 
from subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string 

def subscribe(request):
   if request.method == 'POST':
      body = render_to_string('subscriptions/subscription_email.txt')
      mail.send_mail('Confirmação de Inscrição',body,'contato@eventif.com.br',['contato@eventif.com.br', 'jeanpr667@gmail.com'])
      return HttpResponseRedirect('/inscricao/')
   context = {"form":SubscriptionForm()}
   return render(request, 'subscriptions/subscription_form.html', context)

