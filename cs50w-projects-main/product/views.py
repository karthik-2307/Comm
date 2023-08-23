from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, item, Category

def index(request):
    my_data = item.objects.all() #for all the records 
    one_data = item.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    allCategory = Category.objects.all()
    context={
      'my_data':my_data,
      'one_data':one_data,
      "categories": allCategory
    } 
    return render(request, "product/index.html", context)

def pay(request, id):
    my_data = item.objects.all() 
    one_data = item.objects.get(pk=id)
    context={
      'my_data':my_data,
      'one_data':one_data,
    } 
    return render(request, "product/payment.html", context)

# Create your views here.
def pricing(request):

    my_data = item.objects.all() #for all the records 
    one_data = item.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    context={
      'my_data':my_data,
      'one_data':one_data,
    } 
    return render(request, 'product/pricing.html', context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "product/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "product/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "product/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "product/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "product/register.html")
