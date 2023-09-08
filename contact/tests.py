from django.core import mail
from django.urls import reverse
from .forms import ContactForm
from django.test import TestCase

class TestesContatoPersonalizados(TestCase):
    def setUp(self):
        self.dados_validos_personalizados = {
            'nome_completo': 'Jean Teixeira', 'email_usuario': 'jean.teixeira@aluno.riogrande.ifrs.edu.br', 'mensagem_usuario': 'teste'
        }
        self.resposta_valida_personalizada = self.client.post(reverse('contact_view'), data=self.dados_validos_personalizados)

    def teste_requisicao_get(self):
        resposta_get = self.client.get(reverse('contact_view'))
        self.assertEqual(resposta_get.status_code, 200)
        self.assertTemplateUsed(resposta_get, 'contact/contact_form.html')

    def teste_requisicao_post_valida(self):
        self.assertEqual(self.resposta_valida_personalizada.status_code, 302)

    def teste_requisicao_post_invalida(self):
        dados_invalidos_personalizados = {
            'nome_completo': '', 'email_usuario': 'email-invalido', 'mensagem_usuario': 'invalido'
        }
        resposta_invalida_personalizada = self.client.post(reverse('contact_view'), data=dados_invalidos_personalizados)
        self.assertEqual(resposta_invalida_personalizada.status_code, 200)

    def teste_envio_de_email(self):
        self.assertEqual(self.resposta_valida_personalizada.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'contato@eventif.com.br')
