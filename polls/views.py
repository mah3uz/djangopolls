from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello dear. You're at the Poll Home page")
    
def detail(request,  poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)
    
def results(request,  poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)
    
def vote(request,  poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
