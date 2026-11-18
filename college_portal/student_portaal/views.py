from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data={
        'name':"abc",
        'age':19,
        'department':"BCA"
    }
    marks=[100,98,97]
    return render(request,'/student_portal/home.html',{''})
def about(request):
    return HttpResponse("Welcome to About page")
def contact(request):
    return HttpResponse("Welcome contact page")
