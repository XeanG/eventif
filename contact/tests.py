from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm
from .views import contact_view 


class TestesContato(TestCase):
    def test_get(self):
        response = self.client.get(reverse('contact_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

    def test_post_valido(self):
        dados_validos = {
            'nome': 'Exemplo', 'email': 'exemplo@email.com', 'mensagem': 'Mensagem de teste'
        }
        response = self.client.post(reverse('contact_view'), data=dados_validos)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após o envio

    def test_post_invalido(self):
        dados_invalidos = {
            'nome': '', 'email': 'invalid-email', 'mensagem': ''
        }
        response = self.client.post(reverse('contact_view'), data=dados_invalidos)
        self.assertEqual(response.status_code, 200)  # Página de formulário deve ser recarregada

    def test_enviar_email(self):
        # Simular o envio de um email aqui e verificar se ele foi enviado corretamente
        # Este teste pode ser mais complexo e envolver um mock para enviar email.
        pass
