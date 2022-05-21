from django.contrib.postgres.fields import ArrayField
from django import forms

class LearningSpaceForm(forms.Form):
  title = forms.CharField(max_length=100)
  overview = forms.CharField(max_length=1000)
  prerequisites = ArrayField(forms.CharField(max_length=100), blank=True)
  keywords = ArrayField(forms.CharField(max_length=100), blank=True)
  thumbnail = forms.FileField()
