# i have created this file - raja
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>HOME</h1>")

def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punc")

def capitalizefirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("New line remove")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("char count")
