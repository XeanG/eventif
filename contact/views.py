from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import Contact_model


def contact(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        # Extrai dados do formulário
        nome = form.cleaned_data['name']
        telefone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['message']
        
        # Salva os dados no banco de dados
        contato = Contact_model.objects.create(
            name=nome,
            phone=telefone,
            email=email,
            message=mensagem
        )

        # Configuração para envio do email
        assunto = 'Contato do site'
        remetente = settings.DEFAULT_FROM_EMAIL
        lista_destinatarios = ['contato@eventif.com.br', email]
        
        # Conteúdo do email
        conteudo_email = render_to_string('contact/contact_email.txt', {
            'name': nome,
            'phone': telefone,
            'email': email,
            'message': mensagem
        })
        
        # Envia o email
        send_mail(assunto, conteudo_email, remetente, lista_destinatarios)
        
        # Adiciona uma mensagem de sucesso
        messages.success(request, 'Mensagem enviada com sucesso')
        
        # Redireciona para a página de contato
        return HttpResponseRedirect('/contact/')
    
    # Se o formulário não for válido, renderize o formulário novamente com erros.
    return render(request, 'contact/contact_form.html', {'form': form})

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})


def send_mail_contact(dados_contato):
    assunto = 'Contato Eventif'
    email_origem = settings.DEFAULT_FROM_EMAIL
    email_destino = dados_contato['email']
    nome_template = 'contact/contact_email.txt'
    contexto = dados_contato

    corpo_email = render_to_string(nome_template, contexto)
    send_mail(assunto, corpo_email, email_origem, [email_origem, email_destino], fail_silently=False)


