__author__ = 'Badmuthafucker'
from ..models import Card, Player, WarGame
import factory

class WarGameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cards.WarGame'


    def test_get_losses(self):
        user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
        WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
        self.assertEqual(user.get_losses(), 3)