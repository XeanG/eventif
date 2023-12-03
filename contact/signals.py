from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .models import Contact_model

@receiver(post_save, sender=Contact_model)
def enviar_resposta(sender, instance, **kwargs):
    if instance.response:
        assunto = 'Resposta ao seu contato'
        email_origem = settings.DEFAULT_FROM_EMAIL
        email_destino = instance.email

        contexto = {
            'name': instance.name,
            'email': instance.email,
            'phone': instance.phone,
            'message': instance.message,
            'response': instance.response,
        }

        corpo_mensagem = render_to_string('contact/contact_response.txt', contexto)

        send_mail(assunto, corpo_mensagem, email_origem, [email_origem, email_destino], fail_silently=False)


def send_response_email(sender, instance, **kwargs):
    enviar_resposta(sender, instance, **kwargs)