from django.test import TestCase
from django.core.urlresolvers import reverse
from ..utils import create_deck



class testFilter(TestCase):
    def setUp(self):
        create_deck()

    def test_card_filter(self):
        response = self.client.get(reverse('filters'))
        self.assertIn('Capitalized Suit: 0 <br>', response.content)
        self.assertIn('Uppercased Rank: TWO', response.content)
        self.assertEqual(response.context['cards'].count(), 52)