from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignupForm

from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    return render(request, 'index.html')


# def login(request):
#      if request.method =="POST":
#         name = request.POST['username']
#         passw = request.POST['password']
#         user = authenticate(username = name, password = passw)
#         if user:
#             login(request, user)
#             messages.success(request, 'signin successful')
#             return redirect('index')
#         else:
#             messages.warning(request, 'username/password incorrect')
#             return redirect('index')    
#      return render(request, 'login.html')


# def signup(request):
#     regform = SignupForm()#instantiate the form for a GET request
#     if request.method == 'POST':
#         phone = request.POST['phone']
#         regform = SignupForm(request.POST)#instantiate the signup form for a POST request
#         if regform.is_valid():
#             newuser = regform.save()
#             newprofile = Profile(user = newuser)
#             newprofile.first_name = newuser.first_name
#             newprofile.last_name = newuser.last_name
#             newprofile.email = newuser.email
#             newprofile.phone = phone
#             newprofile.save()
#             login(request, newuser)
#             messages.success(request, 'Signup successful')
#             return redirect('index') 
#         else:
#             messages.error(request, regform.errors)
#             return redirect('signup') 
#     return render(request, 'signup.html')
# #authentication system done 

# def signup(request):
# #    if request.method == 'POST':
# #     uname = request.POST.get('username')
# #     fname = request.POST.get('firstname')
# #     lname = request.POST.get('lastname')
# #     email = request.POST.get('email')
# #     passw = request.POST.get('password1')
# #     passw2 = request.POST.get('password2')
# #     my_user=User.objects.create_user(uname,fname,lname,email,passw,passw2)
# #     my_user.save()
#     return redirect('index')

def signup(request):
    regform =SignupForm()
    if request.method == 'POST':
        if regform.is_valid():
            regform.save()
            return redirect(request,'index')
        else:
            messages.error(request, regform.errors)
    return render(request,'signup.html',{'regform':regform})


# def login(request):
#     # name = request.POST['username']
#     # passw = request.POST['password']
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, userneme= username, password=password)
#     if user is not None:
#         login(request, user)
#         messages.success(request, 'signin successful')
#         return redirect('index')
#     else:
#         messages.warning(request, 'username/password incorrect')
#         return redirect('signup')

def login(request):
    if request.method =="POST":
        name = request.POST['username']
        passw = request.POST['password']
        user = authenticate(username = name, password = passw)
        if user:
            login( request,user)
            messages.success(request, 'signin successful')
            return redirect('index')
        else:
            messages.warning(request, 'username/password incorrect')
            return redirect('login')
    return render(request, 'login.html')



