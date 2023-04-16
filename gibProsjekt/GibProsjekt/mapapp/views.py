from django.shortcuts import render, redirect
from django.contrib.auth import login
from mapapp import forms

# Create your views here.
def first_view(request):
    return render(request, 'StartPage.html')

def home(request):
    return render(request, 'HomePage.html')

def registration_view(request):
    print('hallo1')
    if request.method == "POST":
        form = forms.RegisterNewUser(request.POST)
        print('hallo')
        if form.is_valid():

            form.save()

            print('hallo3')

        return redirect("/home")
    else:
        print('hallo2')
        form = forms.RegisterNewUser()


        return render(request, "registration/registration.html", {"form": form})