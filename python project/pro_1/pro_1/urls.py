"""pro_1 URL Configuration

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
from pro_1app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.homepage),
    path('c', views.contact),
    path('s', views.services),
    path('f', views.feedback),
    path('', views.homePage),
    path('contact', views.contactForm),
    path('feedback', views.feedbackview),
    path('ho/', views.home, name='home'),
    path('co/', views.contact, name='contact'),
    path('se/', views.service, name='service'),
    path('ge/', views.gallery, name='gallery'),
    path('cd/', views.curdpage, name='x'),
    path('add_student', views.addStudent, name='add_student'),
    path('update_data/<id>', views.cupdate, name='update_data'),
    path('save_update_data/<id>', views.save_data, name='save_update_data'),
    path('delete_data/<id>', views.delete_data, name='delete_data')

]
