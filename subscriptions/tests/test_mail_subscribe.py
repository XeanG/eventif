from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail

class MailTest(TestCase):
    def setUp(self):
        data = dict(name='Jean Pierre', cpf='1234567890', email='jeanpr667@gmail.com', phone='53991561217')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = 'jeanpr667@gmail.com'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['jeanpr667@gmail.com', 'jeanpr667@gmail.com']  # Atualize os endereços de e-mail aqui
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Jean Pierre','1234567890', 'jeanpr667@gmail.com', '53991561217']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)