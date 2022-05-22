from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.auth import get_user_model
from django import forms

class LearningSpaceCreateForm(forms.Form):
  title = forms.CharField(max_length=100)
  overview = forms.CharField(max_length=1000)
  prerequisites = SimpleArrayField(forms.CharField(max_length=100), delimiter=',')
  keywords = SimpleArrayField(forms.CharField(max_length=100), delimiter=',')
  thumbnail = forms.FileField()

class LearningSpaceEditForm(forms.Form):
  title = forms.CharField(max_length=100)
  overview = forms.CharField(max_length=1000)
  prerequisites = SimpleArrayField(forms.CharField(max_length=100), delimiter=',')
  keywords = SimpleArrayField(forms.CharField(max_length=100), delimiter=',')

User = get_user_model() # User model can't be imported. It has to be called through function instead.

class SignInForm(forms.Form):
  username = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

  def validate_username(self):
    username = self.clenaned_data.get("username")
    username_query = User.objects.filter(username_iexact=username)
    if not username_query.exists():
      raise forms.ValidationError('This username already exists.')
    return username

class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={"class": "form-control"}))