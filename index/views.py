from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound


# Create your views here.

def Dynamic_link(request ,link):
    text_test = "index.html"
    if link == 'index':
        text_test="index.html"
    elif link == 'about':
        text_test ="about.html"
    elif link =='services':
        text_test="services.html"
    elif link == 'contact':
        text_test="contact.html"
    else:
        return HttpResponseNotFound("This page is not' find error 404")
    return render(request, text_test)