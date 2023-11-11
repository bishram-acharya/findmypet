from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')
def howitworks(request):
    return render(request, 'howitworks.html')
def contact(request):
    return render(request, 'contact.html')
def findmypet(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')