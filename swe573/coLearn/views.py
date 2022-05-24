from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import LearningSpace, CoLearnUser, Question, Answer
from .forms import LearningSpaceCreateForm, LearningSpaceEditForm, SignInForm, SignUpForm, UserProfileForm, ProfilePictureForm, AnswerForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required

# Learning Space views.

def learning_space_view(request, learning_space_id):

  learningSpace = LearningSpace.objects.get(pk=learning_space_id)

  # Obtain quizzes and questions.
  quizzes = learningSpace.quizzes.all()
  questions = learningSpace.questions.all()

  # Obtain the subscribers using the LearningSpace model.
  subscribers = learningSpace.subscribers.all()

  user_authenticated = False
  
  user_id = None
  
  if request.user.is_authenticated:
    user_authenticated = True
    user_id = request.user.id


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
    'user_authenticated': user_authenticated,
    'user_id': user_id
  }

  return render(request, 'learningSpace/learning_space.html', context)

@login_required
def learning_space_create_view(request):
  if request.method == "POST":
    form = LearningSpaceCreateForm(request.POST, request.FILES or None)
    if form.is_valid():
      space_created = LearningSpace.objects.create(**form.cleaned_data)
      if(space_created):
        return redirect('/learningspace/%d' % space_created.id )
  else:
    context = {}
    return render(request, 'learningSpace/learning_space_create.html', context)

@login_required
def learning_space_edit_view(request , learning_space_id):
  learningSpace = LearningSpace.objects.get(pk=learning_space_id)
  if request.method == "POST":
    form = LearningSpaceEditForm(request.POST, request.FILES or None)
    if form.is_valid():
      result = LearningSpace.objects.filter(pk=learning_space_id).update(**form.cleaned_data)
      if(result):
        return redirect('/learningspace/%d' % learning_space_id )

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

  user_authenticated = False
  user_id = None
  
  if request.user.is_authenticated:
    user_authenticated = True
    user_id = request.user.id

  context = {
    'learning_spaces' : learningSpaces,
    'user_authenticated': user_authenticated,
    'user_id': user_id
  }

  return render(request, 'explore/explore.html', context)

# Authentication views.

User = get_user_model()

def sign_up_view(request):
  signUpForm = SignUpForm(request.POST or None)
  if signUpForm.is_valid():
    username = signUpForm.cleaned_data.get('username')
    first_name = signUpForm.cleaned_data.get('first_name')
    last_name = signUpForm.cleaned_data.get('last_name')
    email = signUpForm.cleaned_data.get('email')
    password = signUpForm.cleaned_data.get('password')
    confirm_password = signUpForm.cleaned_data.get('confirm_password') 
    try: 
      user = User.objects.create_user(username, email, password)
      user.first_name = first_name
      user.last_name = last_name
      user.save()
    except:
      user = None
    if user != None:
      login(request, user)
      return redirect('/explore')
    else:
      request.session['sign_up_failed'] = 1
  return render(request, 'signUp/sign_up.html', {'form':signUpForm})

def sign_in_view(request):
  signInForm = SignInForm(request.POST or None)
  if signInForm.is_valid():
    username = signInForm.cleaned_data.get('username')
    password = signInForm.cleaned_data.get('password')
    user = authenticate(request, username=username, password=password)
    if user != None:
      login(request, user)
      return redirect('/explore/')
    else:
      request.session['authentication_failed'] = 1
  return render(request, 'signIn/sign_in.html', {'form':signInForm})

def logout_view(request):
  logout(request)
  return redirect('/explore')

# User Profile view.

def profile_view(request, user_id):
  coLearnUser = CoLearnUser.objects.get(pk=user_id)
  learningSpaces = LearningSpace.objects.filter(subscribers=coLearnUser)

  profilePictureForm = ProfilePictureForm(request.POST,request.FILES or None)
  if profilePictureForm.is_valid():
    coLearnUser.profile_picture = profilePictureForm.cleaned_data.get('profile_picture_upload')
    coLearnUser.save()    

  context = {
    'first_name' : coLearnUser.user.first_name,
    'last_name' : coLearnUser.user.last_name,
    'bio' : coLearnUser.bio,
    'background': coLearnUser.background,
    'interests': coLearnUser.interests,
    'user_id': coLearnUser.id,
    'learning_spaces': learningSpaces,
    'profile_picture': coLearnUser.profile_picture
  }

  return render(request, 'profile/profile.html', context)

@login_required
def profile_edit_view(request, user_id):
  coLearnUser = CoLearnUser.objects.get(pk=user_id)
  learningSpaces = LearningSpace.objects.filter(subscribers=coLearnUser)

  userProfileForm = UserProfileForm(request.POST or None)

  if userProfileForm.is_valid():
    coLearnUser.bio = userProfileForm.cleaned_data.get('bio')
    coLearnUser.background = userProfileForm.cleaned_data.get('background')
    coLearnUser.interests = userProfileForm.cleaned_data.get('interests')

    coLearnUser.save()
    
    return redirect('/user/%d' % user_id )

  context = {
    'first_name' : coLearnUser.user.first_name,
    'last_name' : coLearnUser.user.last_name,
    'bio' : coLearnUser.bio,
    'background': coLearnUser.background,
    'interests': coLearnUser.interests,
    'user_id': coLearnUser.id,
    'learning_spaces': learningSpaces,
    'profile_picture': coLearnUser.profile_picture
  }

  return render(request, 'profile/profile_edit.html', context)

# Quizzes views.

@login_required
def quiz_view(request, learning_space_id, quiz_id):

    context = {}

    return render(request, 'quiz/quiz.html', context)

@login_required
def quiz_create_view(request, learning_space_id):

    context = {}

    return render(request, 'quiz/quiz_create.html', context)

# Questions views.

@login_required
def question_view(request, learning_space_id, question_id):
  question = Question.objects.get(pk=question_id)
  answers = question.answers.all()

  answerForm = AnswerForm(request.POST or None)
  if(answerForm.is_valid()):
    coLearnUser = CoLearnUser.objects.get(pk=request.user.id)
    answer = Answer.objects.create(sender=coLearnUser, content=answerForm.cleaned_data.get('content'))
    question.answers.add(answer)

    return redirect('/learningspace/%d/question/%d' % (learning_space_id,question_id))
  
  context = {
    'learning_space_id': learning_space_id,
    'question_id': question_id,
    'question': question,
    'answers': answers
  }

  return render(request, 'question/question.html', context)

@login_required
def question_create_view(request, learning_space_id):

    context = {}

    return render(request, 'question/question_create.html', context)