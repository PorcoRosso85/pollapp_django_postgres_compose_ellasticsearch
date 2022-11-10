from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    return HttpResponse("Looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse("Looking at the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s" % question_id)
