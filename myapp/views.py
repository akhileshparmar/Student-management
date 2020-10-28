from django.shortcuts import render, redirect
from . models import Students
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q


#Students = Students()

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search').title()
        if len(search)!=0:
            user = Students.objects.filter(Q(Name__startswith = search)).order_by("Name")
            if user.exists():
                return render(request, 'search.html', {'search' : user})            
            else:
                messages.info(request, 'NOT FOUND')
                return render(request, 'search.html')
            
        else:
            messages.info(request, 'Please Enter any name')
            return render(request, 'search.html')         
            

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')   

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')
            
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, 'Register successfully')
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('/register')


    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(req):
	return render(req, "index.html")



def lists(request, str):
    if str=="IT":
        list = Students.objects.filter(Class="IT").order_by("Name")
    elif str=="CS":
        list = Students.objects.filter(Class="CS").order_by("Name")
    elif str=="ME":
        list = Students.objects.filter(Class="ME").order_by("Name")
    elif str=="EC":
        list = Students.objects.filter(Class="EC").order_by("Name")
    elif str=="CE":
        list = Students.objects.filter(Class="CE").order_by("Name")
    else:
        list = Students.objects.all()

    return render(request, "list.html", {'list':list})


def profile(request, Scholar_no):
    row = Students.objects.filter(Scholar_no=Scholar_no)
    return render(request, "profile.html", {'rows': row})

'''def result(request, Scholar_no):
    row = Students.objects.filter(Scholar_no=Scholar_no)
    return render(request, "result.html", {'rows': row})'''