from rest_framework.test import APITestCase
from authentication.models import User
class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('seun', 'seun@gmail.com', 'Password@1')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEquals(user.email,'seun@gmail.com')

    def test_Create_Super_user(self):
        user=User.objects.create_superuser('cryce', 'crycetruly@gmail.com', 'Password@1')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEquals(user.email, 'crycetruly@gmail.com')

    def test_raise_value_error_when_username_not_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='' ,email='crycetruly@gmail.com', password='Password@1' )

    def test_raise_value_error_when_email_not_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='cryce', email='', password='crycetruly@gmail.com')

    def test_raise_value_error_when_username_not_supplied_for_create_super_user(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='', email='crycetruly@gmail.com', password='Password@1')

    def test_raise_value_error_when_email_not_supplied_for_create_super_user(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='cryce', email='', password='Password@1')

    def test_raise_value_error_for_createsuperuser_with_is_staff_False(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='Cryce', email='crycetruly@gmail.com', password='Password@1', is_staff=False)

    def test_raise_value_error_for_createsuperuser_with_is_superuser_False(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username='Cryce', email='crycetruly@gmail.com', password='Password@1', is_superuser=False)