from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import LearningSpace

# Learning Space views.

def learning_space_view(request, learning_space_id):

  learningSpace = LearningSpace.objects.get(pk=learning_space_id)

  # Obtain quizzes and questions.
  quizzes = learningSpace.quizzes.all()
  questions = learningSpace.questions.all()

  # Obtain the subscribers using the LearningSpace model.
  subscribers = learningSpace.subscribers.all()

  # TODO: Dummy value until authenticated is implemented.
  user_authenticated = False

  relatedSpaces = LearningSpace.objects.filter(keywords=learningSpace.keywords)

  context = {
    'title' : learningSpace.title,
    'overview' : learningSpace.overview,
    'prerequisites' : learningSpace.prerequisites,
    'id': learningSpace.id,
    'quizzes': quizzes,
    'questions': questions,
    'subscribers': subscribers,
    'related_spaces': relatedSpaces,
    'user_authenticated': user_authenticated
  }

  return render(request, 'learningSpace/learning_space.html', context)

  def learning_space_create_view(request):
  # TODO: Enforce user authentication.

  context = {}
  return render(request, 'learningSpace/learning_space_create.html', context)

  def learning_space_edit_view(request , learning_space_id):
  learningSpace = LearningSpace.objects.get(pk=learning_space_id)

  context = {
    'title' : learningSpace.title,
    'overview' : learningSpace.overview,
    'prerequisites' : learningSpace.prerequisites,
    'keywords': learningSpace.keywords,
    'id': learningSpace.id
  }

  return render(request, 'learningSpace/learning_space_edit.html', context)

# Explore views.

def explore_view(request):

  learningSpaces = LearningSpace.objects.all()

  # TODO: Dummy value until authenticated is implemented.
  user_authenticated = False

  context = {
    'learning_spaces' : learningSpaces
    'user_authenticated': user_authenticated
  }

  return render(request, 'explore/explore.html', context)

# Authentication views.

def sign_up_view(request):
  return render(request, 'signUp/sign_up.html')

def sign_in_view(request):
  return render(request, 'signIn/sign_in.html')

# User Profile view.

def profile_view(request, user_id):

  coLearnUser = CoLearnUser.objects.get(pk=user_id)
  learningSpaces = LearningSpace.objects.filter(subscribers=coLearnUser)

  context = {
    'first_name' : coLearnUser.user.first_name,
    'last_name' : coLearnUser.user.last_name,
    'bio' : coLearnUser.bio,
    'background': coLearnUser.background,
    'interests': coLearnUser.interests,
    'user_id': coLearnUser.id,
    'learning_spaces': learningSpaces
  }

  return render(request, 'profile/profile.html', context)