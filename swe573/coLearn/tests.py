from django.test import TestCase
from django.contrib.auth import get_user_model
from coLearn.models import CoLearnUser

User = get_user_model()

class UserTestCase(TestCase):

  def setUp(self): 
    # Set user variables.
    self.username='unit'
    self.email='unit@test.com'
    self.user_password='test_1234!'

    # Set coLearnUser variables.
    self.bio = 'Example bio. Born in 1996.'
    self.background = 'Example background. Interested in software engineering and unit tests.'
    self.interests = ['Unit Tests', 'Software Engineering']

    # Create a User and set username, email and password.
    user_t = User(username=self.username, email=self.email)
    user_t.is_staff = True
    user_t.is_superuser = True
    user_t.set_password(self.user_password)
    user_t.save()
    self.user_t = user_t

    # Create a CoLearnUser and set bio, background and interests.
    # Note: When a User object is created, a coLearnUser is also created
    # through a receiver that is called on User save. 
    coLearnUser_t = CoLearnUser.objects.get(pk=self.user_t.id)
    coLearnUser_t.bio = self.bio
    coLearnUser_t.background = self.background
    coLearnUser_t.interests = self.interests
    coLearnUser_t.save()
    self.coLearnUser_t = coLearnUser_t


  
