from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')
    # return HttpResponse('Homepage')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('About')

def contact(request):
    # return HttpResponse('Contact Us')
    return render(request,'contact.html')
