from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student, feedbackdata, servicedata, Curddata
import datetime
date1 = datetime.datetime.now()


def homepage(request):
    x = 'welcome to django session'
    return HttpResponse(x)


def contact(request):
    x = 'our contact no is 3637t7828760'
    return HttpResponse(x)


def services(request):
    x = 'WE propide all services'
    return HttpResponse(x)


def feedback(request):
    x = 'we have good feedback'
    return HttpResponse(x)


def homePage(request):
    return render(request, 'homepage.html')


def contactForm(request):
    if request.method == 'GET':
        return render(request, 'contactform.html')
    else:
        student(
            sname=request.POST.get('sname'),
            fee=request.POST.get('fee'),
            course=request.POST.get('course'),
            mobile=request.POST.get('mobile')

        ).save()
        return render(request, 'contactform.html')


def feedbackview(request):
    if request.method == 'GET':
        feedbacks = feedbackdata.objects.all()
        return render(request, 'feedback.html', {'feedbacks': feedbacks})
    else:
        feedbackdata(
            name=request.POST.get('name'),
            rating=request.POST.get('rating'),
            feedback=request.POST.get('feedback'),
            date=date1
        ).save()
        feedbacks = feedbackdata.objects.all()
        return render(request, 'feedback.html', {'feedbacks': feedbacks})


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def service(request):
    courses = servicedata.objects.all()
    return render(request, 'service.html', {'courses': courses})


def gallery(request):
    return render(request, 'gallery.html')


def curdpage(request):
    student = Curddata.objects.all()
    return render(request, 'curd.html', {'student': student})


def addStudent(request):
    if request.method == 'GET':
        return render(request, 'addstudent.html')
    else:
        Curddata(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            course=request.POST.get('course'),
            location=request.POST.get('loc'),
            assignment1=request.POST.get('a1'),
            assignment2=request.POST.get('a2'),
            assignment3=request.POST.get('a3'),
            assignment4=request.POST.get('a4'),
        ).save()
        return redirect('x')


def cupdate(request, id):
    student = Curddata.objects.get(id=id)
    return render(request,'update_data.html', {'student': student})


def save_data(request,id):
    student = Curddata.objects.get(id=id)

    student.first_name = request.POST.get('fname')
    student.lastname = request.POST.get('lname')
    student.email = request.POST.get('email')
    student.course = request.POST.get('course')
    student.location = request.POST.get('loc')
    student.mobile = request.POST.get('mobile')
    student.assignment1 = request.POST.get('a1')
    student.assignment2 = request.POST.get('a2')
    student.assignment3 = request.POST.get('a3')
    student.assignment4 = request.POST.get('a4')
    student.save()
    return redirect('x')


def delete_data(request, id):
    student = Curddata.objects.get(id=id)
    student.delete()
    return redirect('x')

