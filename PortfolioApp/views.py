from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    
    return render(request,'index.html')
def about(request):
    return render(request,'aboutme.html')
def services(request):
    return render(request,'contact.html')
def contact(request):
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')
def help(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')

        submit=Contact(name=name,email=email)
        submit.save()
    return render(request,'help.html')