from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user=models.ForeignKey(User)
    question = models.CharField(max_length=120)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self, ):
        return self.question
    
    
class Answer(models.Model):
    question=models.ForeignKey(Question)
    answer = models.CharField(max_length=120)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self, ):
        return self.answer