from django.shortcuts import render
from django.contrib import messages
from .models import Appointment,Property
from .forms import AppointmentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    if request.method=="POST":
        form= AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Appointment created successfully.")
        else:
            print(form.errors.values())
            messages.error(request,form.errors)

    return render(request,template_name="main/index.html")

def contact(request):
    print("hey on")
    if request.method=="POST":
        form= AppointmentForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request,"Appointment created successfully.")
        else:
            print(form.errors.values())
            messages.error(request,form.errors)
        print(request.POST)


    return render(request,template_name="main/contact.html")

def about(request):
    return render(request,template_name="main/about.html")

def gallery(request):
    properties=Property.objects.all()
    print(properties)
    
    p = Paginator(properties, 4)
    page_number = request.GET.get('page')
    
    try:
        page = p.page(page_number)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    
    context={
        "properties":page,
    }

    return render(request,template_name="main/gallery.html",context=context)

def properties(request):
    properties=Property.objects.all()
    print(properties)
    context={
        "properties":properties,
        "name":"Eri"
    }
    p = Paginator(properties, 5)
    page_number = request.GET.get('page')
    
    try:
        page = p.page(page_number)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    
    context={
        "properties":page,
        "name":"Eri"
    }
    return render(request,template_name="main/properties.html",context=context)

def services(request):
    return render(request,template_name="main/service.html")
