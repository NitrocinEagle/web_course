from django.db import models


class Lecture(models.Model):
    topic = models.CharField(max_length=128)
    about = models.TextField()

    def __str__(self):
        return '%s. %s' % (self.id, self.topic)
