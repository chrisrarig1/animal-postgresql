from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Animal

class AnimalTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_animal = Animal.objects.create(name='rabbit', owner=testuser1,description='a fluffy hopper.')
        test_animal.save()

    def test_things_model(self):
        animal = Animal.objects.get(id=1)
        actual_owner = str(animal.owner)
        actual_name = str(animal.name)
        actual_description = str(animal.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rabbit')
        self.assertEqual(actual_description,'a fluffy hopper.')
