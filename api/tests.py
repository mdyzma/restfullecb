"""Test suite for ECB restfull service"""
from django.test import TestCase
from models import Currency


class ModeltestCase(TestCase):
    """Class defines test suite for currency list model."""

    def setUP(self):
        """Basic model class setup for all test cases"""
        self.currency_symbol = "USD"
        self.currency = Currency(name=self.currency_symbol)

    def test_model_creates_currency_list(self):
        """Tests if model properly stores Curency lists"""
        old_count = Curency.objects.count()
        self.currency.save()
        new_cunt = Currency.objects.count()

        self.assertNotEquals(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.currency_data = {'symbol': 'USD'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")