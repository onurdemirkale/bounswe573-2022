from django.test import TestCase
from django.contrib.auth import get_user_model
from coLearn.models import CoLearnUser
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class UserTestCase(TestCase):

  def setUp(self): 
    # Set user variables.
    self.username='unit'
    self.email='unit@test.com'
    self.user_password='test_1234!'

    # Set up second user variables for testing sign up url.
    self.test_username = 'test'
    self.test_email='test@test.com'
    self.test_password='qwert_1234!'
    self.test_first_name='jane'
    self.test_last_name='doe'

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

  # Ensure that the user exists.
  def test_user_exists(self):
    user_count = User.objects.all().count()
    self.assertEqual(user_count, 1)

  # Ensure that the user password is set correctly.
  def test_user_password(self):
    self.assertTrue(self.user_t.check_password(self.user_password))

  # Ensure that the receiver is used correctly to create a coLearnUser.
  def test_coLearnUser_exists(self):
    coLearnUser_count = CoLearnUser.objects.all().count()
    self.assertEqual(coLearnUser_count, 1)
  
  # Ensure that the coLearnUser stores information correctly.
  def test_coLearnUser_information_valid(self):
    self.assertEqual(self.coLearnUser_t.background, self.background)
    self.assertEqual(self.coLearnUser_t.bio, self.bio)
    self.assertEqual(self.coLearnUser_t.interests, self.interests)

  # Ensure that a user can successfully sign in and is redirected correctly.
  def test_sign_in_url(self):
    sign_in_url=settings.LOGIN_URL
    data = {'username': self.username, 'password': self.user_password}
    response=self.client.post(sign_in_url, data, follow=True)
    status_code = response.status_code
    redirect_path = response.request.get('PATH_INFO')
    self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
    self.assertEqual(status_code, 200)

  # Ensure that a new user can sucessfully sign up and is redirected correctly.
  def test_sign_up_url(self):
    sign_up_url='/signup/'
    data = {'username': self.test_username, 
            'first_name': self.test_first_name,
            'last_name': self.test_last_name,
            'password': self.test_password,
            'confirm_password': self.test_password,
            'email': self.test_email}

    response=self.client.post(sign_up_url, data, follow=True)
    status_code = response.status_code
    redirect_path = response.request.get('PATH_INFO')
    self.assertEqual(redirect_path, '/explore/')
    self.assertEqual(status_code, 200)

  # Ensure that a user can successfully edit its profile.
  def test_edit_profile(self):
    self.client.force_login(self.user_t)
    edit_profile_url='/user/%d/edit' % self.user_t.id
    data = {'bio': self.coLearnUser_t.bio, 'background': self.coLearnUser_t.background, 'interests': self.coLearnUser_t.interests}
    response = self.client.post(edit_profile_url, data, follow=True)
    status_code = response.status_code
    redirect_path = response.request.get('PATH_INFO')
    self.assertEqual(redirect_path, '/user/%d/' % self.user_t.id)
    self.assertEqual(status_code, 200)

  # Ensure that a user can upload a profile picture.
  def test_upload_profile_picture(self):
    self.client.force_login(self.user_t)
    profile_url = '/user/%d' % self.user_t.id
    profile_picture = SimpleUploadedFile("pp.jpeg", b"file_content", content_type="image/jpeg")
    data = {'profile_picture': profile_picture}
    response = self.client.post(profile_url, data, follow=True)
    status_code = response.status_code
    redirect_path = response.request.get('PATH_INFO')
    self.assertEqual(redirect_path, '/user/%d/' % self.user_t.id)
    self.assertEqual(status_code, 200)
  