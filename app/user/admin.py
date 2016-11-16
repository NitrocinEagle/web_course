from app.user.tasks.models import Task, TaskAnswer
from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(TaskAnswer)
