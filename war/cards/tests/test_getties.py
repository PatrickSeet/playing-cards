__author__ = 'Badmuthafucker'
from ..models import Card, Player, WarGame

def test_get_ties(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
    self.assertEqual(user.get_ties(), 4)

def test_get_record_display(self):
    user = Player.objects.create_user(username='test-user', email='test@test.com', password='password')
    WarGameFactory.create_batch(2, player=user, result=WarGame.WIN)
    WarGameFactory.create_batch(3, player=user, result=WarGame.LOSS)
    WarGameFactory.create_batch(4, player=user, result=WarGame.TIE)
    self.assertEqual(user.get_record_display(), "2-3-4")