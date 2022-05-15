from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import LearningSpace

def learningSpace(request, learning_space_id):

  learningSpace = LearningSpace.objects.get(pk=learning_space_id)

  context = {
    'title' : learningSpace.title,
    'overview' : learningSpace.overview,
    'prerequisities' : learningSpace.prerequisites
  }

  return render(request, 'learning_space.html', context)
