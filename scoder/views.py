from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title': 'Sourabh HomePage'
    }
    return render(request,"index.html", data)

def about(request):
    data={
        'title': 'Sourabh About-Us'
    }
    return render(request,"about.html", data)

def contact(request):
    data={
        'title': 'Sourabh Contact'
    }
    return render(request,"contact.html", data)

def aboutus(request):
    return HttpResponse("welcome to Sourabh")