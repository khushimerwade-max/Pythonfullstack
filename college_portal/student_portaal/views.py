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
    return render(request,'home.html',{'data1':data,'marks1':marks})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def forms1(request):
    if request.method=="POST":
        reg_no==request.POST.get('reg_no')
        name==request.POST.get('name')
        marks==request.POST.get('marks')
        email==request.POST.get('email')
        dob==request.POST.get('dob')
        return render(request,'Student_form.html',{'message':"saved successfully"})
    return render(request,'Student_form.html')
    return HttpResponse("saved successfully")

