from django.test import TestCase

class SubscribeTest(TestCase):
    def test_get(self):
        """"GET /inscricao/ must return status_code 200"""
        response = self.client.get('/inscricao/')
        self.assertEqual(200, response.status_code)

def test_template(self):
    """Must use subscripitions/subscripition_form.html"""
    response = self.client.get('/inscricao/')
    self.assertTemplateUsed(response, 'subscriptions/subscripition_form.html')