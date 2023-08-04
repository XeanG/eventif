from django.http import HttpResponseRedirect
from django.shortcuts import render 
from subscriptions.forms import SubscriptionForm

def subscribe(request):
   if request.method == 'POST':
      mail.send_mail('Confirmação de Inscrição',MESSAGE,'contato@eventif.com.br',['contato@eventif.com.br', 'jeanpr667@gmail.com'])
      return HttpResponseRedirect('/inscricao/')
   context = {"form":SubscriptionForm()}
   return render(request, 'subscriptions/subscription_form.html', context)

MESSAGE = """
Olá! Tudo bem?

Muito obrigado por se inscrever no Eventif.

Estes foram os dados que vocẽ enviou na sua
inscrição.

Nome: Jean Pierre
CPF: 12345678901
Email: jeanpr667@gmail.com
Telefone: 53 991561217

Em até 48h úteis alguem da nossa equipe entrará em contato com você para concluirmos a sua
inscrição.

Atenciosamente,
Equipe EventIF
"""