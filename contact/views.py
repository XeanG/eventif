from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from django.shortcuts import render

def contact_view(request):
    if request.method == 'POST':
        return criar_contato(request)
    else:
        return novo_contato(request)

def criar_contato(request):
    formulario_contato = ContactForm(request.POST)
    if not formulario_contato.is_valid():
        return render(request, 'contact/contact_form.html', {'form': formulario_contato})

    nome_contato = formulario_contato.cleaned_data['nome']
    telefone_contato = formulario_contato.cleaned_data['telefone']
    email_contato = formulario_contato.cleaned_data['email']
    mensagem_contato = formulario_contato.cleaned_data['mensagem']
    assunto_email = 'contato@eventif.com.br'
    remetente_email = email_contato
    destinatarios_email = ['contato@eventif.com.br', email_contato]
    conteudo_email = render_to_string('contact/contact_email.txt', {'nome': nome_contato, 'telefone': telefone_contato, 'email': email_contato, 'mensagem': mensagem_contato})

    send_mail(assunto_email, conteudo_email, remetente_email, destinatarios_email)
    messages.success(request, 'Mensagem enviada com sucesso')
    return HttpResponseRedirect('/contact/')

def novo_contato(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})
