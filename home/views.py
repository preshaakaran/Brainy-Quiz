from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # check if user has entered correct credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # A backend authenticated the credentials
            messages.success(request, "Successfully Logged In!")
            return render(request, 'login.html')
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid Credentials, Please try again!")

            return redirect("/")

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'index.html')







def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        add = request.POST.get('add')
        contact = Contact(email=email, password=password, add=add)
        contact.save()
        messages.success(request, 'Message sent!')
    
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # username.save()
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'signup.html')  # Redirect back to the signup page
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return render(request, 'signup.html')  # Redirect back to the signup page
        
        # Create a new User object with the provided data
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, 'Sign up successfull!.Click on login')
        return render(request, 'signup.html')
        
    
    return render(request, 'signup.html')


def science(request):
    # return HttpResponse("This is about page")
    return render(request, 'science.html')


def maths(request):
    return render(request, 'maths.html')
    # return HttpResponse("This is services page")


def gk(request):
    # return HttpResponse("This is about page")
    return render(request, 'gk.html')

def result(request):
    # return HttpResponse("This is about page")
    count = request.GET.get('count', 0)
    
    return render(request, 'result.html',{'count': count})

def get_result_view(request):
    count = request.GET.get('count', 0) # Retrieve the count from the request
    # Process the count or any other data as needed
    return JsonResponse({'status': 'success'})










    
