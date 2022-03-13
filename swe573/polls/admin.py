from django.contrib import admin

# Registers the Question model to be modifiable through the admin framework.
from .models import Question

admin.site.register(Question)