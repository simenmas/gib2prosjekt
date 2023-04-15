from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(request, 'StartPage.html') # Startpage when you open the browser

# Homepage:
def homepage(request):
    return render(request, 'HomePage.html') # Homepage when you are logged in