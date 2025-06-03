from django.shortcuts import render,redirect
from .models import Userdata,Doctorinfo
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'king.html')

def signup_page(request,method= ['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        print(email,password,confirm_password)
        user=Userdata.objects.filter(email=email)
        if user.exists():
            messages.error(request,"user is already taken")
        elif password!= confirm_password:
            messages.error(request,"password is not matching")
        else:
            Userdata.objects.create(email=email,password=password)
            return render(request,'login.html')        
        
    return render(request,'signup.html')

def login_page(request,method= ['GET','POST']):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=Userdata.objects.filter(email=email,password=password)
        if user.exists():
            return redirect('/home/')
        else:
            messages.error(request,'email and password are incorrect')

    return render(request,'login.html')
def home(request):
    doctor_info= Doctorinfo.objects.all()
    return render(request,'home.html',{'doctors':doctor_info})
