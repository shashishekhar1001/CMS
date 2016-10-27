#-*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin

class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text

class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.poll.question