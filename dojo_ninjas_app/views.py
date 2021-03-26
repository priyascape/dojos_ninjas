from django.shortcuts import render, HttpResponse, redirect
from .models import  *


def index(request):
    context = {
        "all_the_dojos": Dojo.objects.all(),
        "all_the_ninjas":Ninja.objects.all(),
    }
    return render (request,'index.html', context)

def submit_dojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])

    print(request.POST)
    return redirect ("/")

def submit_ninja(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=request.POST['dojo'])
    
    print(request.POST)
    return redirect ("/")

def delete(request):
    Ninja.objects.all().delete(),
    Dojo.objects.all().delete()

    return redirect ("/")





