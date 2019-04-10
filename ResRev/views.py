from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Reviewer, Restaurant, Review
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.http import HttpResponse, HttpResponseRedirect



def registering(request):
    if(request.POST['username']==""):
        return render(request, 'Register.html',{"err" : "Please Insert Username" },)
    elif(request.POST['password']!=request.POST['Cpassword']):
        return render(request, 'Register.html',{"err" : "Password is not correct" },)
    elif(request.POST['name']=="" or request.POST['contact']==""):
        return render(request, 'Register.html',{"err" : "Please Insert Name and Contact" },)
    else:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password']
        ,first_name=request.POST['name'])
        Reviewer.objects.create(user=user,contact=request.POST['contact'])
        return render(request,'FrontPage.html',{'err':"Register Success!"})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('/ResRev/home/')
    else:
        return render(request,'FrontPage.html',{'err': "Error, username or password is not correct"})

def logout(request):
    auth_logout(request)
    return render(request,'FrontPage.html',{'err': "Log Out Complete!"})


def add_rest(request):
    if(request.POST['name'] and request.POST['descrip'] and request.POST['contact'] and request.POST['cate']):
        Restaurant.objects.create(name=request.POST['name'],contact=request.POST['contact'],description=request.POST['descrip'],category=request.POST['cate'])
        return render(request, 'FrontPage.html',{'err': "Add Restaurant Success!"})
    else:
        return render(request,'new_rest.html',{'err': "Error, Please Fill all the Boxes below"})

def home(request):
    list_restau = Restaurant.objects.filter()
    return render(request,'home.html',{'list_restau':list_restau})

def restau(request,rest_id):
    rest_info = Restaurant.objects.get(id=rest_id)
    list_review = Review.objects.filter(restau=rest_id)
    return render(request,'restaurant_page.html',{'rest_info':rest_info,'list_review':list_review})

def add_review(request,rest_id):
    if(request.user.get_username() and request.POST['Rating']):
        rest = Restaurant.objects.get(id=rest_id)
        US = Reviewer.objects.get(user=request.user.get_username())
        Review.objects.create(restau=rest,reviewer=US,comment=request.POST['Rcomm'],rating=request.POST['Rating'])
        cal_rating = Review.objects.filter(restau=rest_id)
        rate = 0
        for i in range (Review.objects.filter(restau=rest_id,).count()) :
            rate = rate + fil[i].rating
        rest.rating=rate/Review.objects.filter(restau=rest_id,).count()
        rest.save()
        return HttpResponseRedirect(reverse('ResRev:restau', args=(rest_id,)))
    else:
        return render(request,'restaurant_page.html',{'rest_info':rest_info,'list_review':list_review,'err':"Please Fill all the information"})
