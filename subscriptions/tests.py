from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.shortcuts import render

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
    def test_get(self):
        """"GET /inscricao/ must return status_code 200"""
        self.assertEqual(200, self.response.status_code)

def test_template(self):
    """Must use subscripitions/subscripition_form.html"""
    self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

def test_html(self):
    """HTML must contain input tags"""
    self.assertContains(self.response, "<form")
    self.assertContains(self.response, "<input", 6)
    self.assertContains(self.response, 'type="text"', 3)
    self.assertContains(self.response, 'type="email"')
    self.assertContains(self.response, 'type="submit"')

def test_csrf(self):
    """HTML must contain csrf"""
    self.assertContains(self.response, "csrfmiddlewaretoken")

def test_has_form(self):
    """Context must have subscription form"""
    form = self.response.context["form"]
    self.assertIsInstance(form,SubscriptionForm)

def test_form_has_fields(self):
    form = self.response.context['form']
    self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form,fields))

class SubscribeTestPost(TestCase):
    def test_post(self):
        data = dict(name="Jean Pierre", cpf="12345678901", email="jeanpr667@gmail", phone="53 991561217")
    self.response = self.client.post('/inscricao/', data)

def test_post(self):
    self.assertEqual(302, response.status_code)

def test_send_subscribe_email(self):
    self.assertEqual(1, len(mail.outbox))

def test_subscription_email_subject(self):
    email = mail.outbox[0]
    expect = "Confirmação de Inscrição"
    self.assertEqual(expect, email.subject)

def test_subscription_email_sender(self):
    email = mail.outbox[0]
    expect = "contato@eventif.com.br"
    self.assertEqual(expect, email.from_email)

def test_subscription_email_to(self):
    email = mail.outbox[0]
    expect = ['contato@eventif.com.br', 'jeanpr667@gmail.com']
    self.assertEqual(expect, email.to)

def test_subscription_email_body(self):
    email = mail.outbox[0]
    self.assertIn('Jean Pierre', email.body)
    self.assertIn('12345678901', email.body)
    self.assertIn('jeanpr667@gmail.com',email.body)
    self.assertIn('53 991561217', email.body)