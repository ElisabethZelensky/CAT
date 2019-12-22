from django.contrib.auth.models import User
from django.test import TestCase


class UsersTests(TestCase):

    def test_wrong_password(self):
        user = User.objects.create(username="test2", password='jopa')
        self.assertTrue(user.check_password("jopa"), True)


