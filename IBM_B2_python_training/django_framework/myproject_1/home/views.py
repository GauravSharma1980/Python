from django.shortcuts import render, HttpResponse

# Create your views here.
def myindexpage(request):
    return HttpResponse("Welcome")
