from django.shortcuts import render, redirect
from django.contrib.auth import login
from mapapp import forms
from .models import Point

# Create your views here.
def first_view(request):
    return render(request, 'StartPage.html')

def home(request):

    points = Point.objects.all()
    pointcor = list(points.values('lat','lon'))
    context = {'points': points, 'pointcor':pointcor}
    if request.method == "POST":  # request.POST is immutable, so we need a copy
        print(request.POST)
        copy = request.POST.copy()
        copy['user']=request.user  # adds the user to the dictionary so all points registers which user made the point
        form = forms.PointForm(copy)
        if form.is_valid():
            print(form.is_valid())
            form.save()

    return render(request, 'HomePage.html', context)

def search_and_find(request):
    if request.method == "POST":
        criteria = request.POST.copy()  # declare a variable for the search criteria

    
        points = Point.objects.filter(name__contains=criteria['tittel'])
  
        
        if criteria['visibility'] != 'alle':
            filtered = Point.objects.filter(visibility=criteria['visibility'])
        else:
            filtered = Point.objects.all()
        if criteria['category'] != 'alle':
            filtered = filtered.intersection(Point.objects.filter(category=criteria['category']))
        
        points = points.intersection(filtered)
        pointcor = list(points.values('lat', 'lon'))
        context = {'points': points, 'pointcor': pointcor}


    else:
        points = Point.objects.all()
        pointcor = list(points.values('lat', 'lon'))
        context = {'points': points, 'pointcor': pointcor}
        
    return render(request, 'Homepage.html', context)


def closeTo(request):
    return render(request, 'CloseTo.html')

def profile(request):
    return render(request, 'ProfilePage.html')

def registration_view(request):
    if request.method == "POST":
        form = forms.RegisterNewUser(request.POST)
        if form.is_valid():
            print(form)
            form.save()
        return redirect("/home")
    else:
        form = forms.RegisterNewUser()
        return render(request, "registration/registration.html", {"form": form})
