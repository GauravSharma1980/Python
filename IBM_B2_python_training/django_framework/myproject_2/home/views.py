from django.shortcuts import render, HttpResponse

# Create your views here.
def myindexpage(request):
    # return HttpResponse("Hello")
    return render(request, 'index.html', {})

def myaboutpage(request):
    return render(request, 'about.html', {})