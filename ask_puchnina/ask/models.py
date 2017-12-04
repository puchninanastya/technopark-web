# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''
class Profile(models.Model):
    user = models.OneToOneField(User)

class Question(models.Model):
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=80)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    #tags = models.ManyToManyField( todo tag )
    likes = models.IntegerField(default=0)

class QuestionManager(models.Manager):


class Tag(models.Model):
    title = models.CharField(max_length=100)

class TagManager(models.Manager):


class Answer(models.Model):
    author = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=50)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    correct = models.BooleanField(default=False)

class AnswerManager(models.Manager):
'''
