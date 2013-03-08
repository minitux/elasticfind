from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=255)

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    reponse = models.CharField(max_length=255)
    poll = models.ForeignKey('Poll')

    def __unicode__(self):
        return "%s - [%d]" % (self.reponse, self.poll.id)
