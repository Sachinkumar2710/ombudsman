from django.http import HttpResponse
import datetime
from django.shortcuts import render,redirect

def home(request):
    date = datetime.datetime.now()
    print("test function is called from view")
    #return HttpResponse("<h1>Hello this is index page</h1>" + str(date))
    return render(request,"home.html",{})
    

def about(request):
    #return HttpResponse("<h1>Hello this is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("")
    return render(request,"services.html")

def careeroption(request):
    return render(request,"careeroption.html")

def helpdesk(request):
    return render(request,"helpdesk.html")

def section2(request):
    return render(request,"section2.html")

def login(request):
    return render(request,"login.html")
