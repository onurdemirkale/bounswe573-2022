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