from django.shortcuts import render
from django.http import HttpResponse
from products.models import Contact

def index(request):
    context = {
        "var":"variable msg"
    }
    #return HttpResponse("Hello django")
    return render(request,'index.html',context)

def new(request):
    return HttpResponse("This is new Page")

def about(request):
    return HttpResponse("This is about Page")

def price(request):
    return HttpResponse("This is price Page")

def quantity(request):
    return HttpResponse("This is quantity Page")

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        message =request.POST.get('message')
        contact = Contact(name=name,email=email,message=message)
        contact.save()

    return render(request,'contact.html')
    

    

