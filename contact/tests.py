from django.test import TestCase
from django.core import mail
from .forms import ContactForm
from django.urls import reverse

class ContactTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'nome': 'Jean Teixeira',
            'email': 'jean.teixeira@aluno.riogrande.ifrs.edu.br',
            'mensagem': 'teste'
        }
        self.response = self.client.post(reverse('contact_view'), data=self.valid_data)

    def test_get(self):
        response = self.client.get(reverse('contact_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

    def test_post_valid(self):
        self.assertEqual(self.response.status_code, 302)

    def test_post_invalid(self):
        invalid_data = {
            'nome': '',
            'email': 'invalid-email',
            'mensagem': 'invalido'
        }
        response = self.client.post(reverse('contact_view'), data=invalid_data)
        self.assertEqual(response.status_code, 200)

    def test_send_email(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Contato do site')
