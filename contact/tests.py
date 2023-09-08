from django.core import mail
from django.urls import reverse
from .forms import ContactForm
from django.test import TestCase

class TestesContato(TestCase):
    def setUp(self):
        self.dados_validos = {
            'nome': 'Whesley Souza', 'email': 'whesley.souza@aluno.riogrande.ifrs.edu.br', 'mensagem': 'TESTANDO'
        }
        self.resposta = self.client.post(reverse('contact_view'), data=self.dados_validos)

    def test_get(self):
        resposta = self.client.get(reverse('contact_view'))
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'contact/contact_form.html')

    def test_post_valido(self):
        self.assertEqual(self.resposta.status_code, 302)

    def test_post_invalido(self):
        dados_invalidos = {
            'nome': '', 'email': 'invalid-email', 'mensagem': 'invalido'
        }
        resposta_invalida = self.client.post(reverse('contact_view'), data=dados_invalidos)
        self.assertEqual(resposta_invalida.status_code, 200)

    def test_enviar_email(self):
        self.assertEqual(self.resposta.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'contato@eventif.com.br')