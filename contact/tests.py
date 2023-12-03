# from django.test import TestCase
# from django.core import mail
# from .forms import ContactForm
# from django.urls import reverse

# class ContactTests(TestCase):
#     def setUp(self):
#         self.valid_data = {
#             'name': 'Jean Teixeira',
#             'phone': '53 991561217',
#             'email': 'jean.teixeira@aluno.riogrande.ifrs.edu.br',
#             'message': 'teste'
#         }
#         self.response = self.client.post("/contato/", data=self.valid_data)


#     def test_get(self):
#         response = self.client.get("/contato/")
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'contact/contact_form.html')

#     def test_post_valid(self):
#         self.assertEqual(self.response.status_code, 302)

#     def test_post_invalid(self):
#         invalid_data = {
#             'nome': '',
#             'email': 'invalid-email',
#             'mensagem': 'invalido'
#         }
#         response = self.client.post("/contato/", data=invalid_data)
#         self.assertEqual(response.status_code, 200)

#     def test_send_email(self):
#         self.assertEqual(len(mail.outbox), 1)
#         self.assertEqual('Contato do site', mail.outbox[0].subject)
