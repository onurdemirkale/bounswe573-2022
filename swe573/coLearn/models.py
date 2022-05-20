import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Username, first name, last name, password and e-mail adress 
# is already handled by the django auth model. 
# The Profile Django model is used to store the extra information
# that relates to the built-in Django User model.
class CoLearnUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) # Used to extend the Auth User.
  interests = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  background = models.TextField(max_length=1000, blank=True)
  bio = models.TextField(max_length=1000, blank=True)
  birth_date = models.DateField(null=True, blank=True)

# Signal definition so that Profile model will be automatically 
# created/updated when User instances are created/updated.
@receiver(post_save, sender=User)
def create_colearn_user(sender, instance, created, **kwargs):
    if created:
        CoLearnUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_colearn_user(sender, instance, **kwargs):
    instance.colearnuser.save()

# Note: ForeignKey is used to define many-to-one relationships. 

# Chat Model that represents a conversation between two users.
class Chat(models.Model):
    initiator = models.ForeignKey(CoLearnUser, on_delete=models.CASCADE, related_name='chat_initiator')
    receiver = models.ForeignKey(CoLearnUser, on_delete=models.CASCADE, related_name='chat_participant')
    timestamp = models.DateTimeField(auto_now_add=True)

# ChatMessage Model that represents a message that is sent by any
# party during a chat.
class ChatMessage(models.Model):
    sender = models.ForeignKey(CoLearnUser, on_delete=models.PROTECT, related_name='message_sender')
    receiver = models.ForeignKey(CoLearnUser, on_delete=models.PROTECT, related_name='message_receiver')
    text = models.CharField(max_length=200) # Limited to 200 characters for now.
    file_attachment = models.FileField(blank=True) # For possible file/image attachments.
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

# Question Model used by Quiz to store a Question created by a user.
class Question(models.Model):
  question = models.CharField(max_length=500)
  answers = ArrayField(models.CharField(max_length=200))
  correct_answer = models.CharField(max_length=500)

# Model used for Quizzes created through Topics. 
class Quiz(models.Model):
  quiz_description = models.CharField(max_length=500)
  questions = models.ManyToManyField(Question)

# Reply Model used by Post to store a Reply created by a user.
class Reply(models.Model):
  sender = models.ForeignKey(CoLearnUser, on_delete=models.CASCADE, related_name='reply_sender')
  content = models.CharField(max_length=500, blank=True)

# Model used for Posts created through Topics.
class Post(models.Model):
  post_content = models.CharField(max_length=500)
  replies = models.ManyToManyField(Reply, blank=True)
 
# Types of topics that can be created.
TOPIC_TYPES = [
  ("quiz", "quiz"),
  ("post", "post"),
]

# The topics that are created in a LearningSpace.
class Topic(models.Model):
  topic_title = models.CharField(max_length=100)
  author = models.ForeignKey(CoLearnUser, on_delete=models.PROTECT)
  topic_content = models.CharField(max_length=500)
  topic_type = models.CharField(choices=TOPIC_TYPES, max_length=100)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True)

# Model used for Learning Spaces.
class LearningSpace(models.Model):
  overview = models.CharField(max_length=1000)
  thumbnail = models.FileField(blank=True)
  prerequisites = ArrayField(models.CharField(max_length=100), blank=True)
  title = models.CharField(max_length=100)
  keywords = ArrayField(models.CharField(max_length=100), blank=True)
  subscribers = models.ManyToManyField(CoLearnUser, blank=True)
  topics = models.ManyToManyField(Topic, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)