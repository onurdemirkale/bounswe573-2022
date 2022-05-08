from django.contrib import admin

from coLearn.models import Sample
from coLearn.models import CoLearnUser
from coLearn.models import Topic
from coLearn.models import LearningSpace
from coLearn.models import Chat
from coLearn.models import ChatMessage
from coLearn.models import Post
from coLearn.models import Reply
from coLearn.models import Quiz
from coLearn.models import Question


admin.site.register(Sample)
admin.site.register(CoLearnUser)
admin.site.register(Topic)
admin.site.register(LearningSpace)
admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Quiz)
admin.site.register(Question)






