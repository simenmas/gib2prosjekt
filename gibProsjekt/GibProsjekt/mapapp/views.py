from django.shortcuts import render, redirect
from django.contrib.auth import login
from mapapp import forms

# Create your views here.
def first_view(request):
    return render(request, 'StartPage.html')

def home(request):

    if request.method == "POST":
        print(request.POST)
        copy = request.POST.copy()
        copy['user']=request.user
        form = forms.PointForm(copy)
        if form.is_valid():
            print(form.is_valid())
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
