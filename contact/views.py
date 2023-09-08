from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        nome = form.cleaned_data['name']
        telefone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['message']
        
        assunto = 'Contato do site'
        remetente = settings.DEFAULT_FROM_EMAIL
        lista_destinatarios = ['contato@eventif.com.br', email]
        
        conteudo_email = render_to_string('contact/contact_email.txt', {
            'name': nome,
            'phone': telefone,
            'email': email,
            'message': mensagem
        })
        
        send_mail(assunto, conteudo_email, remetente, lista_destinatarios)
        messages.success(request, 'Mensagem enviada com sucesso')
        return HttpResponseRedirect('/contact/')
    
    # Se o formulário não for válido, renderize o formulário novamente com erros.
    return render(request, 'contact/contact_form.html', {'form': form})

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})
