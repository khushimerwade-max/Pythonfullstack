from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student_table
from .forms import Student_form_data
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def forms1(request):
    return render(request,'Student_form.html')
def student_form_dj(request):
    if request.method=="POST":
        form=Student_form_data()
        if form.is_valid():
            reg_no1=form.cleaned_data['reg_no1']
            name1=form.cleaned_data['name1']
            email1=form.cleaned_data['email1']
            return HttpResponse("Saved successfully")
        else:
            return HttpResponse("Invalid data")
    else:
        form=Student_form_data()
        return render(request,'student_form_data.html',{'form':form})
def user_login(request):
    if request.method=='POST': 
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid username or password")
    return render(request,'login.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')
def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponse("You have logged out successfully")
    return HttpResponse("Invalid request")
       
 

# Create your views here.
