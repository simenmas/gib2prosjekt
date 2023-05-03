from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from mapapp import forms
from .models import Point
from django.db import connection



# Create your views here.
def first_view(request):
    if not request.user.is_authenticated:

        return render(request, 'StartPage.html')
    else:
        return redirect("/home")

def home(request):
    if request.user.is_authenticated:
        points = Point.objects.all()
        pointcor = list(points.values('lat','lon'))
        context = {'points': points, 'pointcor':pointcor}
        if request.method == "POST":  # request.POST is immutable, so we need a copy
            
            copy = request.POST.copy()
            copy['user']=request.user  # adds the user to the dictionary so all points registers which user made the point
            form = forms.PointForm(copy)
            if form.is_valid():
               
                form.save()

        return render(request, 'HomePage.html', context)
    else: 
        return redirect("/")

def search_and_find(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            criteria = request.POST.copy()  # declare a variable for the search criteria

        
            points = Point.objects.filter(name__contains=criteria['tittel'])  # Finds which points contains criteria
    
            
            if criteria['visibility'] != 'alle':  # alle is only to return all the points
                if criteria['visibility'] == 'privat':
                    filtered = Point.objects.filter(user=request.user)
                else:    
                    filtered = Point.objects.filter(visibility=criteria['visibility'])
            else:
                filtered = Point.objects.all()
            if criteria['category'] != 'alle':
                filtered = filtered.intersection(Point.objects.filter(category=criteria['category']))
            # intersection is used to find the elements that are in both querysets
            points = points.intersection(filtered)
            pointcor = list(points.values('lat', 'lon'))
            context = {'points': points, 'pointcor': pointcor}


        else:
            points = Point.objects.all()
            pointcor = list(points.values('lat', 'lon'))
            context = {'points': points, 'pointcor': pointcor}
            
        return render(request, 'Homepage.html', context)
    else:
        return redirect("/")


def closeTo(request):
    if request.method == 'POST':
        
        copy = request.POST.copy()

        lat = copy['lat']
        lon = copy['lon']
        # Finds the chosen point
        
        if copy['avstand']:
            radius = copy['avstand']
        else:
            radius = 0


        try:
            point = Point.objects.get(name=copy['tittel'])
            lat = point.lat
            lon = point.lon
        except:
            pass

        # If the user has written a name for the point, the point is updated to the searched point
        cursor = connection.cursor()

        cursor.execute(f"SELECT name, lat, lon FROM mapapp_point WHERE ST_DWithin('POINT({lon} {lat})'::geography, ST_MakePoint(lon,lat), {radius})")
        result = cursor.fetchall()
        lats = []
        lons = []
        
        for i in result:
            lats.append(i[1])
            lons.append(i[2])
        point_lat = Point.objects.filter(lat__in=lats)
        point_lon = Point.objects.filter(lon__in=lons)
        points = point_lat.intersection(point_lon)
        # Finds all the points that contain the coordinates that the points found in the query
        # It is a roundabout way of getting the points, but it works
        if copy['category'] != 'alle':
            points = points.intersection(Point.objects.filter(category=copy['category']))
        
        points = points.intersection(Point.objects.exclude(name=copy['tittel']))
        pointcor = list(points.values('lat', 'lon'))
        context = {'points': points, 'pointcor': pointcor}

    else:
        points = Point.objects.all()
        pointcor = list(points.values('lat', 'lon'))
        context = {'points': points, 'pointcor': pointcor}

    return render(request, 'CloseTo.html', context)


def profile(request):
    if request.user.is_authenticated:
            points = Point.objects.filter(user=request.user)
            pointcor = list(points.values('lat', 'lon'))
            context = {'points': points, 'pointcor': pointcor}
            return render(request, 'ProfilePage.html', context)
    else:
        return redirect("/")

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

