from models import UserProfile
from django.contrib import admin
from tasks.models import Task, TaskAnswer, UserTask

admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(UserTask)
admin.site.register(TaskAnswer)
