from django.test import TestCase

# Create your tests here.

from .models import CustomUser


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customuser = CustomUser.objects.create(
            name='Davlat',
            username='Davlat',
            email="dushurbakiev@gmail.com",
            password="qwerty1234!"
        )

    def test_model_content(self):
        self.assertEqual(self.customuser.name, "Davlat")
        self.assertEqual(self.customuser.username, "Davlat")
        self.assertEqual(self.customuser.email, "dushurbakiev@gmail.com")
        self.assertEqual(self.customuser.password, "qwerty1234!")
