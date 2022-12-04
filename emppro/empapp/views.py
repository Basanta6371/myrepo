from django.shortcuts import render
from .models import EmpData
from .form import EmpForm


def empdata(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request,'empdata.html',{'form':form})
    else:
      form= EmpForm(request.POST)
      if form.is_valid():
          EmpData(
          name = request.POST.get('name'),
          salary = request.POST.get('salary'),
          company = request.POST['company']
          ).save()
          form = EmpForm()
          return render(request, 'empdata.html',{'form': form})
      else:
          return HttpResponse("Invalid Form")