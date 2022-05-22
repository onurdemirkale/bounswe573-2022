from django.contrib.postgres.forms import SimpleArrayField
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

class SignInForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))