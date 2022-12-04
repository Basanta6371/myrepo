from django.shortcuts import render
from .models import EmpData
from .forms import EmpForm


def empdata(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request,'empdata.html',{'form':form})
    else:
      form= EmpForm(request.POST)
      if form.is_valid():
          form.save()
          form = EmpForm()
          return render(request,'empdata.html',{'form':form})


      else:
          return HttpResponse("Invalid Form")
