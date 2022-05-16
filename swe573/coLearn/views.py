from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import LearningSpace

def learning_space_view(request, learning_space_id):

  learningSpace = LearningSpace.objects.get(pk=learning_space_id)
  topics = learningSpace.topics.all()

  context = {
    'title' : learningSpace.title,
    'overview' : learningSpace.overview,
    'prerequisites' : learningSpace.prerequisites,
    'topics': topics
  }

  return render(request, 'learningSpace/learning_space_unauth.html', context)

def explore_view(request):

  learningSpaces = LearningSpace.objects.all()

  context = {
    'learning_spaces' : learningSpaces
  }

  return render(request, 'explore/explore_unauth.html', context)