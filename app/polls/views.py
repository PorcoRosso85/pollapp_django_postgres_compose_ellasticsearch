from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html', {})

def detail(request, question_id):
    return HttpResponse("Looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse("Looking at the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s" % question_id)
