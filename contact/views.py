from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            
            # Configurar o email
            assunto = 'Contato do Site Eventif'
            remetente = email
            destinatarios = ['contato@eventif.com.br', email]
            conteudo_email = f'Nome: {nome}\nTelefone: {telefone}\nEmail: {email}\nMensagem: {mensagem}'

            # Enviar o email
            send_mail(assunto, conteudo_email, remetente, destinatarios)
            
            messages.success(request, 'Mensagem enviada com sucesso')
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact_form.html', {'form': form})
