from datetime import datetime
from django.test import TestCase
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Jean Pierre",
            cpf="1234567890",
            email="jean.teixeira@aluno.riogrande.ifrs.edu.br",
            phone="53991561217"
        )
        self.obj.save()
        self.assertTrue(Subscription.objects.exists())

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Jean Pierre',str(self.obj))