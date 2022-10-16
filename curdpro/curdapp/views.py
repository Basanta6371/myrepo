from django.shortcuts import render,redirect
from .models import StudentsData
from django.http import HttpResponse

def homepage(request):
    students =  StudentsData.objects.all()
    return render(request,'homepage.html',{'students':students})

def addstudent(request):
    if request.method == 'GET':
     return render(request,'addstudent.html')

    else:
        StudentsData(
        first_name  = request.POST.get('fname'),
        last_name = request.POST.get('lname'),
        email = request.POST.get('email'),
        mobile = request.POST.get('mobile'),
        course = request.POST.get('course'),
        location = request.POST.get('loc'),
        assigment1 = request.POST.get('a1'),
        assigment2 = request.POST.get('a2'),
        assigment3 = request.POST.get('a3'),
        assigment4 = request.POST.get('a4'),
        ).save()
        return redirect('main_page')

def update_data(request,id):
    student = StudentsData.objects.get(id=id)
    return render(request,'update_data.html',{'student':student})

def save_update_data(request,id):
    student = StudentsData.objects.get(id=id)
    student.first_name = request.POST.get('fname')
    student.last_name = request.POST.get('lname')
    student.email = request.POST.get('email')
    student.mobile = request.POST.get('mobile')
    student.course = request.POST.get('course')
    student.location = request.POST.get('loc')
    student.assigment1 = request.POST.get('a1')
    student.assigment2 = request.POST.get('a2')
    student.assigment3 = request.POST.get('a3')
    student.assigment4 = request.POST.get('a4')
    student.save()
    return redirect('main_page')

def delete_data(request,id):
    student = StudentsData.objects.get(id=id)
    student.delete()
