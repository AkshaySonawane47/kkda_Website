from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'index.html')

def index(request):
    return HttpResponse("this is homepage")
def about(request):
    return HttpResponse("this is aboutpage")
    