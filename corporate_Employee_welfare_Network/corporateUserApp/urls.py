"""corporate_Employee_welfare_Network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from corporateUserApp import views

urlpatterns =[
    # path('admin/', admin.site.urls),
    # new registration for user
    path('newregistration/', views.newRegistration, name="newregistrationuser"),
    path('savereg/', views.saveregistration, name="save_reg"),
    path('userlogin_validate/', views.userlogin_validate, name="user_loginvalidate"),
    # thought
    path('Addthought/', views.addThought, name="addthought"),
    path('savethought/', views.saveThought, name="save_thought"),
    path('viewthought/', views.viewThought, name="viewthought"),
    # Events
    path('AddEvent/', views.addEvent, name="addEvent"),
    path('saveEvent/', views.saveEvent, name="save_Event"),
    path('viewEvents/', views.viewEvents, name="viewEvent"),
    # Technical
    path('Addtech/', views.addtechskills, name="addtech"),
    path('savetech/', views.savetechskills, name="savetech"),
    path('viewtech/', views.viewtechskills, name="viewtech"),
    # Work Experience
    path('Addworkexp/', views.addworkexp, name="addworkexp"),
    path('saveworkexp/', views.saveworkexp, name="saveworkexp"),
    path('viewworkexp/', views.viewworkexp, name="viewworkexp"),
    # Property
    path('Addproperty/', views.addPropertyDetails, name="addProperty"),
    path('saveproperty/', views.savePropertyDetails, name="saveProperty"),
    path('viewproperty/', views.viewPropertyDetails, name="viewProperty"),
    # share Market
    path('Addsharemarket/', views.addsharemarket, name="addsharemarket"),
    path('savesharemarket/', views.savesharemarket, name="savesharemarket"),
    path('viewsharemarket/', views.viewsharemarket, name="viewsharemarket"),
    # reference
    path('Addreference/', views.addreference, name="addreference"),
    path('savereference/', views.savereference, name="savereference"),
    path('viewreference/', views.viewreference, name="viewreference"),
    # celebrations
    path('Addcelebration/', views.addcelebration, name="addceleb"),
    path('savecelebration/', views.savecelebration, name="saveceleb"),
    path('viewcelebration/', views.viewcelebration, name="viewceleb"),
    # Travel
    path('AddTravel/', views.addTravel, name="addTravel"),
    path('saveTravel/', views.saveTravel, name="saveTravel"),
    path('viewTravel/', views.viewTravel, name="viewTravel"),
    # Matrimonial
    path('Addmatrimonial/', views.addmatrimonial, name="addmatrimonial"),
    path('savematrimonial/', views.savematrimonial, name="savematrimonial"),
    path('viewmatrimonial/', views.viewmatrimonial, name="viewmatrimonial"),
]
