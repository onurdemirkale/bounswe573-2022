from django.urls import path

from . import views

urlpatterns = [
  path('<int:learning_space_id>/', views.learningSpace, name='learningspace'),
]