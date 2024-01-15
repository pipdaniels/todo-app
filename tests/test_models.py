from rest_framework.test import APITestCase
from authentication.models import User
class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('seun', 'seun@gmail.com', 'Password@1')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEquals(user.email,'seun@gmail.com')

