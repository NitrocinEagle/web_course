from django.db import models


class News(models.Model):
    class Meta:
        ordering = ['-id']

    topic = models.CharField(max_length=128)
    announce = models.TextField()
    text = models.TextField()

    def __unicode__(self):
        return u'%s. %s' % (self.id, self.topic)
