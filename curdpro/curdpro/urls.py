"""curdpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from curdapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='main_page'),
    path('add_student',views.addstudent, name='add_student'),
    path('update_data/<id>',views.update_data,name='update_data'),
    path('save_update_data/<id>',views.save_update_data,name='save_update_data'),
    path('delete_data/<id>', views.delete_data, name='delete_data')
]
