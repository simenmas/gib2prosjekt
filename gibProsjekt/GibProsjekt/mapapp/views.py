from django.shortcuts import render, redirect
from django.contrib.auth import login
from mapapp import forms

# Create your views here.
def first_view(request):
    return render(request, 'StartPage.html')

def home(request):

    if request.method == "POST":
        print(request.POST)
        form = forms.PointForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            print('hallo')
            form.save()

    return render(request, 'HomePage.html')



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

def point_registration_view(request,lat,lng):
    if request.method == "POST":
        request.POST = request.POST.copy()
        form = forms.PointForm(initial={'lat': lat,'lng': lng})
        form = forms.PointForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("/home")
