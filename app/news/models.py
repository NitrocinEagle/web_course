from django.db import models


class News(models.Model):
    topic = models.CharField(max_length=128)
    announce = models.TextField()
    text = models.TextField()

    def __str__(self):
        return '%s. %s' % (self.id, self.topic)
