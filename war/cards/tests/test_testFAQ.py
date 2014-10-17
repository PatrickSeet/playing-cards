from django.test import TestCase
from django.core.urlresolvers import reverse

class testFAQ(TestCase):

    def test_FAQ(self):
        response = self.client.get(reverse('faq'))
        self.assertIn('<p>Q: Can I win real money on this website?</p>', response.content)
        self.assertIn('<p>A: Nope, this is not real, sorry.</p>', response.content)