from django.db import models


class Request(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=256)
    group = models.CharField(max_length=256)
    date = models.DateTimeField()
    email = models.CharField(max_length=60)
    social = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s. %s' % (self.id, self.topic)
