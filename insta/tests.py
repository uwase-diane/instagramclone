from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):

        self.profile_test = Profile(id = 1, name = 'image', profilepic = 'books.png', bio = 'happy new year', user = self.user)

        def test_instance(self):s
            self.assertTrue(isinstance(self.profile_test, Profile))

        def test_save_profile(self):
            self.profile_test.save_profile()
            profiles = Profile.objects.all()
            self.assertTrue(len(after) > 0)

