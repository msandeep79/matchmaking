# Create your views here.
from django.contrib import messages
from django.shortcuts import render_to_response,RequestContext,Http404, HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Answer, Question

def all_questions(request):
    questions = Question.objects.all()
    return render_to_response('questions/all.html',locals(),context_instance=RequestContext(request))